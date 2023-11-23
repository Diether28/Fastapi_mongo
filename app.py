from fastapi import FastAPI
from routes.user import user
from routes.vet import vet

app = FastAPI()

app.include_router(user)
app.include_router(vet)