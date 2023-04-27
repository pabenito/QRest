from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app import database, entities, web

app = FastAPI()

app.include_router(
    entities.router,
    prefix="/entities"
)

app.include_router(
    web.router,
    tags=["web"]
)


@app.on_event("startup")
def startup_db_client():
    app.mount("/static", StaticFiles(directory="static"), name="static")

    app.db_client = database.db_client
    app.db = database.db
    try:
        app.db_client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


@app.on_event("shutdown")
def shutdown_db_client():
    app.db_client.close()
