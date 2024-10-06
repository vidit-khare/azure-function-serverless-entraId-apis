# Azure Function Serverless Entra ID APIs

This repository contains Python code for Azure Functions to manage **Entra ID (Azure Active Directory)** APIs. The functions are designed to be serverless, leveraging Azure's cloud infrastructure to handle user management tasks such as adding, updating, listing and deleting users.

## Features

- **Serverless Architecture**: Utilizes Azure Functions for a scalable, cost-effective solution.
- **User Management**: Provides APIs to list, add, update and delete users in EntraID.
- **Secure Authentication**: Uses `DefaultAzureCredential` for secure access to Azure resources.

## Prerequisites

- **Azure Subscription**: An active Azure subscription.
- **Python 3.8+**: Ensure you have Python installed.
- **Azure Functions Core Tools**: For local development and testing.
- **Azure CLI**: To manage Azure resources from the command line.

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/vidit-khare/azure-function-serverless-entraId-apis.git
    cd azure-function-serverless-entraId-apis
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Azure Functions Core Tools**:
    Follow the instructions here to install Azure Functions Core Tools.

## Configuration

1. **Azure Credentials**:
    Ensure your environment is configured to use `DefaultAzureCredential`. This can be done by setting up environment variables or using managed identities if running in Azure.

2. **Local Settings**:
    Create a `local.settings.json` file in the root directory with the following content:
    ```json
    {
        "IsEncrypted": false,
        "Values": {
            "AzureWebJobsStorage": "UseDevelopmentStorage=true",
            "FUNCTIONS_WORKER_RUNTIME": "python",
            "AZURE_TENANT_ID": "",
            "AZURE_CLIENT_ID": "",
            "AZURE_CLIENT_SECRET": ""
        }
    }
    ```

## Usage

### Adding a User

To add a user, send a POST request to the `/api/users` endpoint with the user details in the request body. Example:

```
curl -X POST \
  http://localhost:7071/api/users/ \
   -d '{
    "accountEnabled": true,
    "displayName": "John Doe",
    "mailNickname": "johndoe",
    "userPrincipalName": "johndoe@yourdomain.com",
    "passwordProfile": {
        "forceChangePasswordNextSignIn": true,
        "password": "Password123!"
    }
}

```

### Updating a User

To update a user, send a PATCH request to the `/api/users/{user_id}` endpoint with the feilds to be updated details in the request body. Example:

```
curl -X PATCH \
    https://<yourapp>.azurewebsites.net/api/users/<user_id> \
    -d '{  "accountEnabled": false }'
```

### Deleting a User

To delete a user, send a DELETE request to the `/api/users/{user_id}` endpoint. 

```
curl -X https://<yourapp>.azurewebsites.net/api/users/<user_id>

```

### Listing a User

To list a user, send a GET request to the `/api/users/` endpoint. 

```
curl -X https://<yourapp>.azurewebsites.net/api/users/

```
## Deployment

### Deploy to Azure:

```bash
func azure functionapp publish <FunctionAppName>
```

## Monitor and Manage: 
Use the Azure portal to monitor and manage your functions.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Azure Functions
- Microsoft Graph API