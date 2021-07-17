import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask
from flask import request

import re
from layout import layout
# from mobile_layout import _apply_mobile_layout

external_stylesheets = [dbc.themes.BOOTSTRAP,
"https://use.fontawesome.com/releases/v5.9.0/css/all.css"]

server = flask.Flask(__name__)

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,
                server=server,
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.8    , minimum-scale=0.5,'}]
                )
cache = Cache(app.server)
app.title = "Style Transfer"