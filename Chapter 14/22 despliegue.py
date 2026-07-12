from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
import joblib
model = joblib.load('modelo_prediccion.pkl')

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener los datos enviados por el usuario
    data = request.get_json()
    
    # Extraer las características
    temperatura = data['temperatura']
    humedad = data['humedad']
    viento = data['viento']
    dia_semana = data['dia_semana']
    
    # Preprocesar los datos
    features = np.array([[temperatura, humedad, viento, dia_semana]])
    prediction = model.predict(features)
    
    # Devolver la predicción
    return jsonify({'prediccion_demanda': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)