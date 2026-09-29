import dash
from dash import dcc, html
import plotly.graph_objs as go
import numpy as np
import random

# Inicialización de la aplicación Dash
app = dash.Dash(__name__)

# Layout de la aplicación
app.layout = html.Div([
    html.H1("Dashboard de Supervisión de Planta Hidroeléctrica"),
    dcc.Graph(id='nivel-embalse'),
    dcc.Graph(id='flujo-agua'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # 1 segundo
        n_intervals=0
    )
])

# Datos iniciales
tiempo = []
nivel_embalse = []
flujo_agua = []

# Callback para actualizar los gráficos
@app.callback(
    [dash.dependencies.Output('nivel-embalse', 'figure'),
     dash.dependencies.Output('flujo-agua', 'figure')],
    [dash.dependencies.Input('interval-component', 'n_intervals')]
)
def update_graph_live(n):
    # Simulación de datos en tiempo real
    nuevo_tiempo = n
    nuevo_nivel = 500 + random.uniform(-5, 5)  # Nivel del embalse fluctuante
    nuevo_flujo = 300 + random.uniform(-10, 10)  # Flujo de agua fluctuante

    tiempo.append(nuevo_tiempo)
    nivel_embalse.append(nuevo_nivel)
    flujo_agua.append(nuevo_flujo)

    # Limitar la cantidad de puntos en los gráficos
    if len(tiempo) > 100:
        tiempo.pop(0)
        nivel_embalse.pop(0)
        flujo_agua.pop(0)

    # Gráfico del Nivel del Embalse
    nivel_fig = {
        'data': [go.Scatter(
            x=tiempo,
            y=nivel_embalse,
            mode='lines+markers',
            name='Nivel del Embalse (m³)',
            line=dict(color='blue')
        )],
        'layout': go.Layout(
            title='Nivel del Embalse en Tiempo Real',
            xaxis=dict(title='Tiempo (s)'),
            yaxis=dict(title='Nivel del Embalse (m³)'),
            margin=dict(l=40, r=20, t=40, b=30)
        )
    }

    # Gráfico del Flujo de Agua
    flujo_fig = {
        'data': [go.Scatter(
            x=tiempo,
            y=flujo_agua,
            mode='lines+markers',
            name='Flujo de Agua (m³/s)',
            line=dict(color='green')
        )],
        'layout': go.Layout(
            title='Flujo de Agua en Tiempo Real',
            xaxis=dict(title='Tiempo (s)'),
            yaxis=dict(title='Flujo de Agua (m³/s)'),
            margin=dict(l=40, r=20, t=40, b=30)
        )
    }

    return nivel_fig, flujo_fig

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True)