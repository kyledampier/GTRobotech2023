import numpy as np
import uuid
from wonderwords import RandomWord
import random
import os
from PIL import Image
import json


word_generator = RandomWord()
animal_directory = os.getcwd() + "\pfps\\"

def make_uuid():
    uid = str(uuid.uuid4())
    #allocate space for this data in the db
    user_dict = get_available_partners()
    if not user_dict:
        user_dict = {uid: {"form_data":None,"available_to_chat":0}}
        
    else:
        user_dict[uid] = {"form_data":None,"available_to_chat":0}
    store_users(user_dict)
    return {"uid": uid}


def create_profile():
    adj = word_generator.word(include_parts_of_speech=["adjectives"], word_max_length=5)
    animal_files = os.listdir(animal_directory)
    animal_file = random.choice(animal_files)
    print(animal_directory + animal_file)
    # user_image = Image.open(animal_directory + animal_file).convert("RGB")
    # user_image = base64.encodebytes(user_image).decode('utf-8')
    username = f"{adj.capitalize()} {animal_file[:-4].lower().capitalize()}"

    return animal_directory + animal_file, username

def update_form_data(user_data):
    user_dict = get_available_partners()
    if not user_dict:
        return "Error reading database"
    uid = user_data['uid']
    answers = process_form_json(user_data)
    user_dict[uid]["form_data"] = answers
    user_dict[uid]["available_to_chat"] = 1
    store_users(user_dict)





def store_users(user_dict):
    with open('user_db.json', 'w') as fp:
        json.dump(user_dict, fp)

def get_available_partners():
    #! this will eventually query a db
    #! for now it just reads a json file into a dictionary
    try:
        user_dict = json.load(open("user_db.json","r"))
        return user_dict
        
    except Exception:
        print("Error reading database")
        return None


def choose_partner(user_data, distance_preference="closest"): #* Or farthest
    #TODO Rewrite to only take uuid
    user_dict = get_available_partners()
    if not user_dict:
        return "Error reading database"
    uid = user_data['uid']
    answers = user_dict[uid]["form_data"]

    distance_dict = {}
    for x in user_dict.keys():
        if user_dict[x]['available_to_chat'] == 1 and x!= uid:
            distance_dict[x] = np.linalg.norm(user_dict[x]['formdata']-answers)
    if len(distance_dict) == 0:
        return "No Users Available to Chat"
    sorted_dict = sorted(distance_dict, key=lambda x: distance_dict[x])
    user_dict[sorted_dict[0]]['uid'] = sorted_dict[0]

    #! set user as unavailable to chat
    partner_data = user_dict[sorted_dict[0]]
    user_dict[sorted_dict[0]]['available_to_chat'] = 0
    store_users(user_dict)
    return partner_data


def on_chat_end(user_data):
    user_id = user_data['uid']
    user_dict = get_available_partners()
    if not user_dict:
        return "Error reading database"
    if user_id not in user_dict:
        return False
    user_dict[user_id]["available_to_chat"] = 1
    store_users(user_dict)
    return True




#! for debugging users
def simulate_user_answers(num_users=10, num_questions=20):
    # * outputs numpy array in the form of N x R, N being users and R being response values
    user_dict = {}
    for x in range(num_users):
        user_dict[str(uuid.uuid4())] = {"formdata":np.random.randint(low=1, high=7, size=(20)).tolist(), "available_to_chat":1}
    
    return user_dict
# fake_users = simulate_user_answers(1)
# store_users(fake_users)