import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64

from callbacks import map_style_model_path

theme_color_code = "#ffffff" #Indigo

image_filename = 'assets/icon.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read()).decode("utf-8")

# 1. Navbar placeholder (currently black row)
navbar = dbc.Row()


# 2. Mosaic icon image
icon_image = dbc.Row(
                    html.Img(src='data:image/png;base64,{}'.format(encoded_image),
                    style={'width':'178px', 'margin-top': "5%"}),
                    justify='center'
        )


### 3. Body title
body_paragraph = dbc.Row(
    [
        dbc.Col(
                [
                    html.H1(
                        "Neural Style Transfer",
                        style={'text-align':'center', "color":"black", "font-family": "Verdana; Gill Sans"}
                            ),
                    html.Br(),
                    html.H5(
                        "Apply styles from well-known pieces of art to your own photos",
                        style={'text-align':'center', "color":"darkgray", "font-family": "Verdana; Gill Sans"}
                            )
                ],
                style ={"padding":"1% 1% 3% 0%", "background-color":theme_color_code}
               )
    ],
    style = {'text-align':'center', "padding":"1% 1% 1% 1%", "background-color":theme_color_code}
)

### 4. Upload button
upload_button = dbc.Col(
    [
        dcc.Upload(id='upload-image',
                   children = dbc.Col(
                       [
                           'Click to upload an image'
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
        
### 5. Dropdown for selecting style
style_dropdown = dbc.Row(
    [
        dbc.Col(
            [
                html.P(html.B("Select a style")),
                dcc.Dropdown(
                    id='passage_dropdown',
                    options=[{'label':key, 'value' : key} for key in map_style_model_path],
                    placeholder = 'Styles',
                    value='Mosaic'
            )
            ]
        )
    ]
)


### 6. Display original and processed images
images = dbc.Row(
    [
        dbc.Col(dbc.CardImg(id='original-image'), style = {"padding" : "2% 1% 1% 2%", 
                                                            'lineHeight': '60px',
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'margin': '10px'}),
        dbc.Col(dbc.CardImg(id='processed-image'), style = {"padding" : "2% 1% 1% 2%", 
                                                            'lineHeight': '60px',
                                                            'borderWidth': '1px',
                                                            'borderStyle': 'dashed',
                                                            'borderRadius': '5px',
                                                            'margin': '10px'})
    ]
)

### 6. Github logo


### 7. Footer
footer = dbc.Row(
    dbc.Col(
        html.Div(
        [
            'Transferring styles from one image to another is just one application of a class neural networks called Generalized Adversarial Networks'
        ' or GANs, for short. This application uses open-source work from ',
        html.A("PyTorch tutorials.", 
                href = "https://github.com/pytorch/examples/tree/master/fast_neural_style/",
                target = "_blank")
        ]
    ),
    width={"size": 10}
), 
    justify='center'
)

### Bring it together
top = dbc.Container(
    [
        dcc.Store(id='memory-output', storage_type='memory'),
        navbar,
        icon_image,
        body_paragraph,
    ],
    fluid = False
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
    fluid = False
)

layout = dbc.Container(
    [
        top, 
        middle,
        bottom
    ]
)