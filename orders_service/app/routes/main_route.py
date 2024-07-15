from flask import Blueprint


# Create a blueprint object
main_route_blueprint = Blueprint('main_route', __name__)

# Define routes and their corresponding functions
@main_route_blueprint.route('/', methods=['GET'])
def index():
    """Returns a greeting message.
    
    ---
    tags:
      - Main Route
    responses:
        200:
            description: A greeting message.
    """
    return 'Hello, World!'



# You can add more routes and functions here
