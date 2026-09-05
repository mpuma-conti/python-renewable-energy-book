import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np
import random

# Inicialización de la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Supervisión de Planta Solar"),
    dcc.Graph(id='voltaje-senal'),
    dcc.Graph(id='potencia-generada'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # 1 segundo
        n_intervals=0
    )
])

# Datos iniciales
time = []
voltaje = []
potencia = []

# Callback para actualizar los gráficos
@app.callback(
    [dash.dependencies.Output('voltaje-senal', 'figure'),
     dash.dependencies.Output('potencia-generada', 'figure')],
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    # Simulación de datos en tiempo real
    new_time = n
    new_voltaje = 230 + random.uniform(-5, 5)  # Voltaje fluctuante alrededor de 230 V
    new_potencia = 500 + random.uniform(-20, 20)  # Potencia fluctuante alrededor de 500 W
    
    time.append(new_time)
    voltaje.append(new_voltaje)
    potencia.append(new_potencia)
    
    # Limitar la cantidad de puntos en los gráficos
    if len(time) > 100:
        time.pop(0)
        voltaje.pop(0)
        potencia.pop(0)
    
    # Gráfico de Voltaje
    volt_fig = {
        'data': [go.Scatter(
            x=time,
            y=voltaje,
            mode='lines+markers',
            name='Voltaje (V)',
            line=dict(color='blue')
        )],
        'layout': go.Layout(
            title='Voltaje en Tiempo Real',
            xaxis=dict(title='Tiempo (s)'),
            yaxis=dict(title='Voltaje (V)'),
            margin=dict(l=40, r=20, t=40, b=30)
        )
    }
    
    # Gráfico de Potencia
    pot_fig = {
        'data': [go.Scatter(
            x=time,
            y=potencia,
            mode='lines+markers',
            name='Potencia Generada (W)',
            line=dict(color='green')
        )],
        'layout': go.Layout(
            title='Potencia Generada en Tiempo Real',
            xaxis=dict(title='Tiempo (s)'),
            yaxis=dict(title='Potencia (W)'),
            margin=dict(l=40, r=20, t=40, b=30)
        )
    }
    
    return volt_fig, pot_fig

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)