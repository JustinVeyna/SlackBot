from .file_handler import FileHandler
from .flagger import get_messages

"""
1. load xl data
2. compile message list
3. load slack ids
4. send messages
"""

def run():
    file = None
    handler = FileHandler(file)
    msgs = get_messages(handler)
    slack_api = make_slack_api()
    for name, msg in msgs:
        slack_id = name_to_slack_id(name)
        slack_api.dm_user(slack_id, msg)


def name_to_slack_id(name):
    slack_id = name
    return slack_id
