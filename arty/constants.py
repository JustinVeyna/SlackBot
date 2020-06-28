import os
BASE_URL = "https://slack.com/api/"
USERS_FILE = os.path.join(os.path.dirname(__file__), '../data/users.tsv')
TOKEN_FILE = os.path.join(os.path.dirname(__file__), '../data/token')
TOKEN = None
with open(TOKEN_FILE,"r") as f:
    TOKEN = f.read().strip()

WARNING_THRESHOLD = 3
