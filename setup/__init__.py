from flask import Flask

app = Flask(__name__)
app.secret_key = "0942"

from setup.controllers import default
