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
import callbacks
from app import app, server, cache, register_before_request

app.layout = layout

@app.callback(
    Output('original-image', 'src'),
    [Input('upload-image', 'contents')])
def update_original_image(contents):
    if contents:
        content_type, content_string = contents.split(',')
        processed_image_string = callbacks.stylize_image(content_string).decode("utf-8")
    src = 'data:image/png;base64,{}'.format(processed_image_string)
    
    return src


if __name__ == '__main__':
    app.server.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))