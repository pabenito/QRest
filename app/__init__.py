from contextlib import asynccontextmanager

from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, RedirectResponse

from app import db
from app import api
from app.core.exceptions import InvalidInputException
from app.db.exceptions import AlreadyExistsException, NotFoundException, OperationFailedException
from app import config


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mount("/static", StaticFiles(directory="static"), name="static")
    db.configure_db()
    app.db_client = db.get_client()
    app.db = db.get_db()
    try:
        app.db_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    yield
    db.close()


app = FastAPI(lifespan=lifespan)

app.include_router(api.router)


@app.get("/")
async def redirect_to_carta():
    return RedirectResponse(url="/carta")


@app.exception_handler(NotFoundException)
async def db_not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": NotFoundException.__name__,
            "message": str(exc)},
    )


@app.exception_handler(AlreadyExistsException)
async def db_already_exists_exception_handler(request: Request, exc: AlreadyExistsException):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "error": AlreadyExistsException.__name__,
            "message": str(exc)},
    )


@app.exception_handler(OperationFailedException)
async def db_operation_failed_exception_handler(request: Request, exc: OperationFailedException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": OperationFailedException.__name__,
            "message": str(exc)},
    )


@app.exception_handler(InvalidInputException)
async def invalid_input_exception_handler(request: Request, exc: InvalidInputException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "error": InvalidInputException.__name__,
            "message": str(exc)},
    )
