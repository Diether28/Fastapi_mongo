from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.vet import vetEntity, vetsEntity
from models.vet import Vet
from passlib.hash import sha256_crypt
from bson import ObjectId

vet = APIRouter()

@vet.get("/vets", response_model=list[Vet], tags=["Vets"])
async def get_vet():
    return vetsEntity(conn.uri.vet.find())

@vet.post("/vets", response_model=list[Vet], tags=["Vets"])
async def create_users(vet: Vet):
    new_vet = dict(vet)
    new_vet["password"] = sha256_crypt.encrypt(new_vet["password"])#encripte la contraseña de usuario
    del new_vet["id"]
    id = conn.uri.vet.insert_one(new_vet).inserted_id
    vet = conn.uri.vet.find_one({"_id": id})
    return vetEntity(vet)

@vet.get("/vets/{id}", response_model=list[Vet], tags=["Vets"])
async def get_id(id: str):
    return vetEntity(conn.uri.vet.find_one({"_id": ObjectId(id)}))