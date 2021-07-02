import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from callbacks import map_style_model_path

theme_color_code = "#4052AB" #Indigo

### 1. Header
navbar = dbc.Row(
            dbc.Col(
                dbc.NavbarSimple(
                    children=[
                        html.Span(
                            [
                                html.A(
                                    html.I(className = "fa-2x fab fa-github", style={'color':'#ffffff'}),
                                href = "https://github.com/dkedar7/neural-style-transfer", target="_blank",
                                className="mr-3"
                                    ),
                                    html.A(
                                    html.I(className = "fa-2x fab fa-twitter-square", style={'color':'#ffffff'}),
                                href = "https://www.twitter.com/dkedar7/", target="_blank",
                                className="mr-3"
                                    ),
                                    html.A(
                                    html.I(className = "fa-2x fab fa-linkedin", style={'color':'#ffffff'}),
                                href = "https://www.linkedin.com/in/dkedar7/", target="_blank",
                                className="mr-3"
                                    )
                            ]
                        ),
                    ],
                    brand="Style Transfer",
                    brand_href=None,
                    color=theme_color_code,
                    dark=True,
                    style = {"font-size":"18", "padding":"2% 2% 0% 2%"}
                )
            )
    ,style ={"background-color":theme_color_code}
)

### 2. Body title
body_paragraph = dbc.Row(
    [
        dbc.Col(
                [
                    html.H4(
                        "Stylize your photos using popular styles",
                        style={'text-align':'center', "color":"white", "font-family": "Verdana; Gill Sans"}
                            ),
                    html.Br(),
                    html.H5(
                        "",
                        style={'text-align':'center', "color":"white", "font-family": "Verdana; Gill Sans"}
                            )
                ],
                style ={"padding":"2% 2% 3% 1%", "background-color":theme_color_code}
               )
    ],
    style = {'text-align':'center', "padding":"2% 2% 1% 1%", "background-color":theme_color_code}
)


### 3. Upload button
upload_button = dbc.Col(
    [
        dcc.Upload(id='upload-image',
                   children = dbc.Col(
                       [
                           'Drag and Drop or ',
                           html.A('Select Files')
                       ]
                   ),
                   style={
                       'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                        'margin': '10px'
                   }
            ),
        ]
)
        
### 4. Dropdown for selecting style
style_dropdown = dbc.Row(
    [
        dbc.Col(
            [
                html.P(html.B("Select a style")),
                dcc.Dropdown(
                    id='passage_dropdown',
                    options=[{'label':key, 'value' : key} for key in map_style_model_path],
                    placeholder = 'Passage suggestions'
            )
            ]
        )
    ]
)


### 5. Display original image
images = dbc.Row(
    [
        dbc.Container(dbc.Col(html.Img(id='original-image', style={'height':'10%'}))),
        dbc.Container(dbc.Col(html.Img(id='processed-image', style={'height':'10%'})))
    ]
)


# style_image = 

# processed_image = dbc.Row

####### Footer #######
footer = dbc.Row(
    [
        dbc.Col(
            [
                html.P(
                [
                """
                    This application uses open-source work from 
                """,
                html.A(
                    html.U("PyTorch tutorials"), 
                href = "https://github.com/pytorch/examples/tree/master/fast_neural_style/",
                target = "_blank",
                style = {"color":"white"}),
                """
                .
                """
                ],
                style = {"color":"white"}
            )
            ],
            className="footer-disclaimer-content ",
            width=8,
        ),
        dbc.Col(
            [
                html.Span(
                    html.A(
                        html.I(className="fa-2x fab fa-github", style={"color":"#ffffff"}),
                        href="https://github.com/dkedar7/neural-style-transfer",
                        target = "_blank"
                    ),
                ),
                html.Span(
                    "   Copyright 2020", style={"color":"white"}
                ),
            ],
            width={"size" : 3, "offset":1}
        ),
    ],
    style ={"background-color":theme_color_code, "padding" : "2% 0% 0% 2%"}
)
    

### Bring it together
top = dbc.Container(
    [
        dcc.Store(id='memory-output', storage_type='memory'),
        navbar,
        body_paragraph,
    ],
    fluid = True
)

middle = dbc.Container(
    [
        upload_button,
        style_dropdown,
        images
    ],
    fluid = False
)

bottom = dbc.Container(
    [
        footer
    ],
    fluid = True
)

layout = dbc.Container(
    [
    top, 
    middle,
    bottom
    ],
    fluid = True
)