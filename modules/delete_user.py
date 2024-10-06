import json
import requests
import logging
from modules.common_functions import get_ms_graph_token


def delete_user(user_id):
    # Get Access Token
    logging.info("Get Access Token")
    access_token = get_ms_graph_token()
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    logging.info(f'Making Authenticated Call to Endpoint {url}')
    response = requests.delete(url, headers=headers)
    return response.status_code
