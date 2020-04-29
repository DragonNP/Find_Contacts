import os

MODE = os.getenv("MODE")
TOKEN = os.getenv("TOKEN")

if MODE == 'prod':
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME")
    PORT = os.environ.get("PORT", "8443")
else:
    REQUEST_KWARGS = {'proxy_url': 'https://134.122.31.84:8080/'}
