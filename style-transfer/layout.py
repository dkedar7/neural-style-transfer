import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

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
                                href = "https://github.com/dkedar7/MachineComprehension", target="_blank",
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
                        "Apply a style to your photos",
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
        

### 4. Dropdown for selecting style
passage_dropdown = dbc.Row(
    [
        dbc.Col(
            [
                html.P(html.B("Select a style")),
                dcc.Dropdown(
                    id='passage_dropdown',
                    options=[{'label':"key", 'value' : "key"}],
                    placeholder = 'Passage suggestions'
            )
            ]
        )
    ]
)

### 3 + 4. Passage suggestion to passage input area


### Input_question
input_question = dbc.Row(
    [
        dbc.Col(
            [
                html.P(html.B("Step 2. Ask a question:")),
                dbc.Input(
                    id='input_question',
                    value = 'What is this passage about?',
                    style = {'padding':'2% 1% 2% 1%'}
                )
            ]
        )
    ],
    style = {'padding':'2% 0% 2% 0%'}
)

### Dropdown for selecting model
model_dropdown = dbc.Row(
    [
        dbc.Col(
            [
                html.P(html.B("Step 3. Choose a model:")),
                dcc.Dropdown(
                    id='model_dropdown',
                    options = [{'label':"BiDAF", 'value' : "bidaf_dd"},
                            {'label':"DistilBERT", 'value' : "distilbert_dd"},
                            {'label':"RoBERTA", 'value' : "roberta_dd"},
                            {'label':"ALBERT", 'value' : "albert_dd"}
                    ],
                    value = "bidaf_dd",
                    searchable=False,
                    clearable=False
                )
            ]
        )
    ]
)

### Submit button
submit_button = dbc.Row(
    [
        dbc.Button("Find answer", id = 'submit_button', size="md",
        color="primary", disabled = False,
        className = "mt-3 mx-auto")
    ],
    justify = 'center'
)

### Output text
output_text = dbc.Spinner(
    dbc.Row(
    [
        dbc.Col(
            [
                dbc.Jumbotron(html.P(id='output_text',children=['']))
            ]
        )
    ] ,
    style = {'text-align':'center', 'padding': '5% 0% 5% 0%'}
    )
)

# Interpretability and About models section
tabs = dbc.Row(
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(
                            dbc.Tabs(
                                [
                                    dbc.Tab(label="Interpret", tab_id="interpret-tab"),
                                    dbc.Tab(label="About BiDAF", tab_id="about-bidaf"),
                                    dbc.Tab(label="About DistilBERT", tab_id="about-distilbert"),
                                    dbc.Tab(label="About RoBERTa", tab_id="about-roberta"),
                                    dbc.Tab(label="About ALBERT", tab_id="about-albert"),
                                ],
                                id="tabs",
                                card=True,
                                active_tab="interpret-tab",
                            )
                        ),
                        dbc.CardBody(id="card-content"),
                    ]
                )
            ),
    style = {'height':'50vh'}
)

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
                    html.U("Hugging Face"), 
                href = "https://huggingface.co/",
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
                        href="https://github.com/dkedar7/MachineComprehension",
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
        submit_button,
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