from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import db
from app.api import backend, frontend

app = FastAPI()

app.include_router(
    backend.router,
    prefix="/backend"
)

app.include_router(frontend.router)


@app.on_event("startup")
def startup_db_client():
    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.db_client = db.db_client
    app.db = db.db
    try:
        app.db_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


@app.on_event("shutdown")
def shutdown_db_client():
    app.db_client.close()
