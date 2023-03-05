import json
from typing import Union
from fastapi import FastAPI
import uuid
import io
from functions import *
from fastapi import Response, Request
from starlette.middleware.cors import CORSMiddleware
# import openai

app = FastAPI()

origins = ["http://localhost:5173", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# NEED OPENAI API KEY


@app.get("/")
def index():
    return {"Hello": "World"}

# @app.get("/get_uuid")
# def generate_uuid():
#     #! this makes a new user in the db
#     return make_uuid()


@app.post("/submit_form")
async def update_user_data(request: Request):
    # * given a user's form data,
    user_data = await request.json()
    update_form_data(user_data)


@app.post("/start_chatbot")
async def begin_chatbot(request: Request):
    # * given a user's form data,
    user_data = await request.json()
    preprompt = generate_survey_paragraph(user_data['survey'])
    messages = start_chatbot(preprompt)
    return messages


@app.post("/chat_with_bot")
async def talk_to_bot(request: Request):
    # * given a user's form data,
    user_data = await request.json()
    messages = get_completion(user_data)
    return messages


@app.get("/profile")
def generate_profile():
    image_path, name = create_profile()
    return {"image_path": image_path, "username": name}


@app.post("/get_partner")
async def get_partner(request: Request):
    # * Get a partner from a users UUID
    user_data = await request.json()
    print(user_data)
    partner = choose_partner(user_data)
    return partner


@app.get("/end_chat")
async def end_chat(request: Request):
    # * Updates the users chat availability to "available"
    user_data = await request.json()
    return on_chat_end(user_data)
