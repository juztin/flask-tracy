#!/usr/bin/env python

from flask import Flask
from flask.ext.tracy import Tracy

app = Flask(__name__)
tracy = Tracy(app)


# (OPTIONAL) Configuration options:
app.config['TRACY_REQURE_CLIENT'] = False
# ----------------------------------


@app.route('/')
def index():
    return "Hello World"


app.run(host="0.0.0.0", debug=True)
