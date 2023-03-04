import json 
from typing import Union
from fastapi import FastAPI
import uuid
import io
from functions import *
from fastapi import Response, Request


app = FastAPI()

@app.get("/")
def index():
    return {"Hello": "World"}

@app.get("/get_uuid")
def generate_uuid():
    #! this makes a new user in the db
    return make_uuid()

@app.get("/submit_form")
async def update_user_data(request: Request):
    #* given a user's form data,
    user_data = await request.json()
    update_form_data(user_data)

@app.get("/profile")
def generate_profile():
    image_path, name = create_profile()
    return {"image_path":image_path, "username": name}

@app.get("/get_partner")
async def get_partner(request : Request):
    #* Get a partner from a users UUID
    user_data = await request.json()
    partner = choose_partner(user_data)
    return partner

@app.get("/end_chat")
async def end_chat(request: Request):
    #* Updates the users chat availability to "available"
    user_data = await request.json()
    return on_chat_end(user_data)


