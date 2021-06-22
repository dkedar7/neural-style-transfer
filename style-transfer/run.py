import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from urllib.parse import quote as urlquote
import flask
from flask import Flask, send_from_directory, send_file, request, session, _request_ctx_stack
import requests

import base64
import datetime
import io
import os
import string
import random
import re

from layout import layout as layout
# from mobile_layout import _apply_mobile_layout
from callbacks import *
from app import app, server, cache, register_before_request

app.layout = layout


if __name__ == '__main__':
    app.server.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))