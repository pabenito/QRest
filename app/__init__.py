from fastapi import FastAPI
from app import database
from app import entities

app = FastAPI()

app.include_router(
    entities.router,
    prefix="/entities",
    tags=["entities"]
)

@app.on_event("startup")
def startup_db_client():
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