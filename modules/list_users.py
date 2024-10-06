import json
import requests
import logging
from modules.common_functions import get_ms_graph_token

def list_users():
    # Get Access Token
    logging.info("Get Access Token")
    access_token = get_ms_graph_token()
    url = "https://graph.microsoft.com/v1.0/users"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    logging.info(f'Making Authenticated Call to Endpoint {url}')
    response = requests.get(url, headers=headers)
    users = response.json()
    pretty_users = json.dumps(users, indent=4)  # Pretty format the JSON response
    return pretty_users, response.status_code
