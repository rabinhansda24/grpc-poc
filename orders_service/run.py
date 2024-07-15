import os
from dotenv import load_dotenv

from app import create_app

load_dotenv()

config_name = os.getenv('FLASK_ENV')

app = create_app('config.Config')


if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_RUN_HOST'), port=os.getenv('FLASK_RUN_PORT'))