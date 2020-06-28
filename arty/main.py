import requests
from .constants import BASE_URL, TOKEN

class WebAPI():
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.token = token
    @property
    def base_args(self):
        return {"token":self.token}

    def api_call(self, api, method="post", **kwargs):
        if method == "get":
            return requests.get(self.base_url+api, {**self.base_args, **kwargs})
        if method == "post":
            return requests.post(self.base_url+api, {**self.base_args, **kwargs})

def make_web_api(base_url=None, token=None):
    base_url = BASE_URL if base_url is None else base_url
    token = TOKEN if token is None else token
    return WebAPI(base_url, token)

class SlackAPI():
    def __init__(self, web_api):
        self.web_api = web_api
    def get_users(self):
        response = self.web_api.api_call("users.list","get").json()
        assert response["ok"], "Bad Response: " + str(response)
        users = response["members"]
        return users
    def get_dm_channel(self, user_id):
        response = self.web_api.api_call("conversations.open","post").json()
        assert response["ok"], "Bad Response: " + str(response) + "User: " + user_id
        channel = response["channel"]["id"]
        return channel
    def post_message(self, channel, text, **kwargs):
        response = self.web_api.api_call("chat.postMessage","post").json()
        assert response["ok"], "Bad Response: " + str(response)
        return response
    def dm_user(self, user_id, text):
        channel = self.get_dm_channel(user_id)
        self.post_message(channel, text)

def make_slack_api(base_url=None, token=None):
    web_api = make_web_api(base_url, token)
    slack_api = SlackAPI(web_api)
    return slack_api
