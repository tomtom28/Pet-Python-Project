import os
FLASK_CONFIG = os.environ.get('FLASK_CONFIG')

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':

    # Production vs. Local Host  
    PORT = int(os.environ.get("PORT", 5000))
    HOST = '0.0.0.0'

    app.run(host=HOST, port=PORT)
