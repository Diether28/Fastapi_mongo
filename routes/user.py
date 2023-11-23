from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.user import userEntity,usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()

@user.get("/user",response_model=list[User], tags=["Users"])
async def get_users():
    return usersEntity(conn.uri.user.find())

@user.post("/user", response_model=list[User], tags=["Users"])
async def create_users(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])#encripte la contraseña de usuario
    del new_user["id"]
    id = conn.uri.user.insert_one(new_user).inserted_id
    user = conn.uri.user.find_one({"_id": id})
    return userEntity(user)

@user.get("/user/{id}", response_model=list[User], tags=["Users"])
async def get_id(id: str):
    return userEntity(conn.uri.user.find_one({"_id": ObjectId(id)}))

@user.put("/user/{id}", response_model=User, tags=["Users"])
async def update_users(id: str, user: User):
    conn.uri.user.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.uri.user.find_one({"_id":ObjectId(id)}))

@user.delete("/user/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
async def delete_users(id: str):
    userEntity(conn.uri.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)