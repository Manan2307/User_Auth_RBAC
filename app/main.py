from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn):
    return user

class AdminIn(BaseModel):
    Adminname: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class AdminOut(BaseModel):
    Adminname: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/Admin/", response_model=AdminOut)
async def create_Admin(Admin: AdminIn):
    return Admin

class SuperAdminIn(BaseModel):
    SuperAdminname: str
    password: str
    email: EmailStr
    full_name: Union[str, None] = None


class SuperAdminOut(BaseModel):
    SuperAdminname: str
    email: EmailStr
    full_name: Union[str, None] = None


@app.post("/SuperAdmin/", response_model=SuperAdminOut)
async def create_SuperAdmin(SuperAdmin: SuperAdminIn):
    return SuperAdmin