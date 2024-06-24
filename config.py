import os
from dotenv import load_dotenv

load_dotenv()  # load .env vars

class Config:
    PORT = int(os.environ.get('PORT', 3000))
    HANA = {
        'host': os.environ.get('HANA_HOST'),
        'port': int(os.environ.get('HANA_PORT')),
        'user': os.environ.get('HANA_USER'),
        'password': os.environ.get('HANA_PASSWORD'),
        'certificate': os.environ.get('HANA_CERTIFICATE')
    }
    XSUAA = {
        'clientid': os.environ.get('XSUAA_CLIENTID'),
        'clientsecret': os.environ.get('XSUAA_CLIENTSECRET'),
        'url': os.environ.get('XSUAA_URL')
    }