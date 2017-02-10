# Determine if in Development or Production
import os
FLASK_CONFIG = os.environ.get('FLASK_CONFIG')


# Configuration Variable - Secret Key for root admin user. Not needed at the moment.
SECRET_KEY = 'p9Bv<3Eid9%$i01'


# Use Localhost if connected locally in development or JAWS_DB if in production
if (FLASK_CONFIG == 'production'):
    SQLALCHEMY_DATABASE_URI = 'mysql://v32slj6qn71ei419:aksjdk01livfeb5p@alv4v3hlsipxnujn.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/zrdbrnk8afyxyoev'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql://dt_admin:dt2016@localhost/dreamteam_db'