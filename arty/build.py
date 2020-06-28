"""
Needed to setup the user -> channel dict

```tsv
name    slack_name  id  channel
name    slack_name  id  channel
```
"""
import os
from .main import make_slack_api
from .utils import read_tsv, write_tsv
from .constants import USERS_FILE

ID=2

def build():
    slack_api = make_slack_api()
    user_to_list = make_user_to_list(slack_api)
    users = slack_api.get_users()
    processed_users = process_users(users)
    if os.path.exists(USERS_FILE):
        #update data
        data = read_tsv(USERS_FILE)
        update_users(data, processed_users)
        write_tsv(USERS_FILE, data)
    else:
        write_tsv(USERS_FILE, processed_users)

def update_users(data, processed_users):
    """
        add processed users to data in not already in it
    """
    registered_user_ids = set([user[ID] for user in data])
    for user in processed_users:
        if user[ID] not in registered_user_ids:
            data.append(user)

def process_users(users):
    processed_users = []
    for user in users:
        if user is_not_bot():
            try:
                processed_user = user_to_list(user)
            except AssertionError:
                print("Warning: Failed to register user:{}".format(user["name"]))
                continue
            processed_users.append(processed_user)
    return processed_users

def is_not_bot(user):
    return not user["is_bot"]

def make_user_to_list(slack_api):
    def user_to_list(user):
        name = user["name"]
        id = user["id"]
        channel = slack_api.get_dm_channel(id)
        user_data =[None, name, id, channel]
        return user_data
    return user_to_list
