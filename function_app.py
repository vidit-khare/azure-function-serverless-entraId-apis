import logging
import azure.functions as func
from modules.create_user import create_user
from modules.update_user import update_user
from modules.delete_user import delete_user
from modules.list_users import list_users

# Initialize the Function APP
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# The Function to list users available
# Endpoint: /api/users
# Method: GET
@app.function_name(name="ListUsers")
@app.route(route="users", methods=["GET"])
def list_users_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to list users.')
    try:
        response, status_code = list_users()
        logging.info(f'status code is {status_code}')
        return func.HttpResponse(str(response), status_code=status_code)
    except Exception as e:
        logging.error(f"Error listing users: {e}")
        return func.HttpResponse(str(e))

# The Function to create user
# Endpoint: /api/users
# Method: POST
@app.function_name(name="CreateUser")
@app.route(route="users", methods=["POST"])
def create_user_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to create user.')
    try:
        user_details = req.get_json()
        response, status_code = create_user(user_details)
        logging.info(f'status code is {status_code}')
        return func.HttpResponse(str(response), status_code=status_code)
    except Exception as e:
        logging.error(f"Error creating user: {e}")
        return func.HttpResponse(str(e))

# The Function to update user
# Endpoint: /api/users/<user_id>
# Method: PATCH
@app.function_name(name="UpdateUser")
@app.route(route="users/{user_id}", methods=["PATCH"])
def update_user_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to update user.')
    try:
        user_id = req.route_params.get('user_id')
        user_details = req.get_json()
        response = update_user(user_id, user_details)
        logging.info(f'status code is {response}')
        return func.HttpResponse(str(response))
    except Exception as e:
        logging.error(f"Error updating user: {e}")
        return func.HttpResponse(str(e))

# The Function to delete user
# Endpoint: /api/users/<user_id>
# Method: DELETE
@app.function_name(name="DeleteUser")
@app.route(route="users/{user_id}", methods=["DELETE"])
def delete_user_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing request to delete user.')
    try:
        user_id = req.route_params.get('user_id')
        logging.info(f'user id is {user_id}')
        response= delete_user(user_id)
        logging.info(f'status code is {response}')
        return func.HttpResponse(str(response))
    except Exception as e:
        logging.error(f"Error deleting user: {e}")
        return func.HttpResponse(str(e))
