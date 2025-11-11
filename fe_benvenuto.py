import dash
from dash import dcc
from dash import html

# codici colori

ACUS_NAVY = 'rgb(31. 44. 82)'
ACUS_GRAY = 'rgb(63, 68, 68)'

# immagini

LOGO_PATH = '/assets/Acus-logo-con-payoff-bianco.png'
BANNER_PATH = '/assets/banner.jpg'

app = dash.Dash(__name__)

# seconda barra blue

header_fixed = html.Div(
    style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'width': '100%',
        'backgroundColor': ACUS_NAVY,  # Sfondo RGB 31, 44, 82
        'color': 'white',              # Lettere Bianche
        'height': '60px',
        'zIndex': 1000,
        'display': 'flex',
        'alignItems': 'center',
        'padding': '0 20px',
        'boxShadow': '0 2px 5px rgba(0, 0, 0, 0.2)',
    },
    children=[
        html.Img(src=LOGO_PATH, style={'height': '40px', 'marginRight': '15px'}),
        html.H2('ACUS Quiz', style={'color': 'white', 'fontSize': '1.5em'}),
        # Link di navigazione
        html.Div(style={'marginLeft': 'auto'}, children=[
            html.A('Info Quiz', href='#', style={'color': 'white', 'marginRight': '15px'}),
            html.A('Contatti', href='#', style={'color': 'white'}),
        ])
    ]
)

# prima barra bianca

hero_bar = html.Div(
    style={
        'backgroundColor': 'white', # Sfondo Bianco
        'color': ACUS_GRAY,         # Testo RGB 63, 68, 68
        'paddingTop': '60px',       # Spazio per l'header fisso
        'paddingBottom': '20px',
        'textAlign': 'center',
    },
    children=[
        html.H1('Metti alla Prova la Tua Conoscenza di ACUS!', style={'color': ACUS_GRAY}),
        html.Img(src=BANNER_PATH, style={'width': '80%', 'maxWidth': '800px', 'marginTop': '10px'}),
    ]
)

if __name__ == '__main__':
    app.run(debug=True)