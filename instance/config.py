# Determine if in Development or Production
import os
FLASK_CONFIG = os.environ.get('FLASK_CONFIG')


# Configuration Variable - Secret Key for root admin user. Not needed at the moment.
SECRET_KEY = 'p9Bv<3Eid9%$i01'


# Use Localhost if connected locally in development or JAWS_DB if in production
if (FLASK_CONFIG == 'production'):
    SQLALCHEMY_DATABASE_URI = 'mysql://<USER_NAME>:<PASSWORD>@<HOST_NAME>/<DATABASE_NAME>'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@localhost/dreamteam_db'