from flask import Flask

app = Flask(__name__)

import main.views
import main.models
