import json
import logging
import requests
from modules.common_functions import get_ms_graph_token

def create_user(user_details):
    # Get Access Token
    logging.info("Get Access Token")
    access_token = get_ms_graph_token()
    url = "https://graph.microsoft.com/v1.0/users"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    logging.info(f'Making Authenticated Call to Endpoint {url}')
    response = requests.post(url, headers=headers, data=json.dumps(user_details))
    return response.json(), response.status_code
