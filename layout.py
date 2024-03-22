from dash import dcc, html

initial_projects = ['Project A']

def app_layout():
    layout = html.Div([
        html.Div([
            html.Img(src="https://querri.com/hubfs/Querri%20Logo.svg", 
            style={
                'width': '80%', 
                'display': 'block', 
                'margin': '20px auto'
                }),
            dcc.Dropdown(
                options=[{'label': project, 'value': project} for project in initial_projects],
                value=initial_projects[0],
                id='project-dropdown',
                searchable=False,
                clearable=False
            ),
            
        ], style={
            'position': 'fixed', 
            'top': '0', 
            'left': '0', 
            'bottom': '0', 
            'backgroundColor': '#2D3339', 
            'color': 'black', 
            'padding': '20px',
            'textAlign': 'center',
            'width': '250px'  # Adjust the width to match the darker grey container
            }),

        html.Div([
            dcc.Upload(
                id='upload-data',
                children=html.Div([
                    'Drag and Drop or ',
                    html.Button('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=True
            ),
            html.Div(id='output-data-upload'),
        ]),

        html.Div([
            dcc.Input(
                id='user-input',
                type='text',
                placeholder='How can Querri help you today?',                    
                style={
                    'fontSize': '18px',
                    'width': 'calc(100% - 290px)',
                    'height': '60px',
                    'borderRadius': '25px', 
                    'paddingLeft': '20px', 
                    'border': '1px solid #ccc', 
                    'outline': 'none', 
                    'margin': '20px auto 0 auto', 
                    'display': 'block', 
                    'boxSizing': 'border-box', 
                    'position': 'absolute', 
                    'bottom': '20px', 
                    'left': '50%', 
                    'transform': 'translateX(-50%)',
                    'zIndex': 1
                }
            ),
            html.Img(
                src='https://cdn-icons-png.flaticon.com/128/10610/10610564.png',
                id='submit-button',
                n_clicks=0,
                style={
                    'height': '60px', 
                    'width': '60px', 
                    'borderRadius': '25px', 
                    'cursor': 'pointer', 
                    'position': 'absolute', 
                    'right': '144px', 
                    'bottom': '20px',
                    'zIndex': 1
                }
            )
        ], style={'display': 'flex', 'justifyContent': 'center', 'alignItems': 'center'}),

        html.Div(id='output-plots', style={'marginTop': '100px', 'zIndex': 0})  # Chat response
    ], style={
        'display': 'flex', 
        'flexDirection': 'column',
        'alignItems': 'center', 
        'position': 'fixed', 
        'bottom': '0', 
        'left': '292px', 
        'right': '0', 
        'backgroundColor': '#394349',
        'height': '1080px'
    })

    return layout