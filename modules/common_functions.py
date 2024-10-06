import os
import requests
import logging
from azure.identity import DefaultAzureCredential

# Replace with your Azure AD tenant ID
tenant_id = os.environ.get('AZURE_RM_TENANT')
client_id = os.environ.get('AZURE_CLIENT_ID')
client_secret = os.environ.get('AZURE_CLIENT_SECRET')

# For Security reasons, Disable INFO level logging for azure.identity, msal, urllib3, and azure.core.pipeline.policies.http_logging_policy
logging.getLogger("azure.identity").setLevel(logging.ERROR)
logging.getLogger("msal").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)
logging.getLogger("azure.core.pipeline.policies.http_logging_policy").setLevel(logging.ERROR)

def get_entra_id_credential() -> object:
    """ Get the Microsoft Entra Id Credential
    Return:
        MS Entra Id Credential
    """
    # Create an instance of DefaultAzureCredential
    logging.info("Getting Azure AD credential")
    credential = DefaultAzureCredential()
    return credential

def get_ms_graph_token() -> object:
    """ Get the Microsoft Graph Token
    Return:
        MS Graph Token
    """
    # Replace with the desired resource (e.g., "https://graph.microsoft.com")
    resource = "https://graph.microsoft.com/.default"
    # Create an instance of DefaultAzureCredential
    credential = get_entra_id_credential()
    # Acquire an access token
    logging.info('Using Entra Id credential to get token for scope: MS Graph')
    token = credential.get_token(resource)
    # Access the token
    access_token = token.token
    return access_token