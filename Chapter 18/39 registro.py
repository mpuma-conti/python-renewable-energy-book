import logging

# Configuración del logging
logging.basicConfig(filename='sistema_automatizado.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def ajustar_valvula(control_signal):
    try:
        # Implementar la lógica para ajustar la válvula
        print(f"Ajustando válvula con señal de control: {control_signal:.2f}")
        logging.info(f"Ajuste de válvula: {control_signal:.2f}")
    except Exception as e:
        logging.error(f"Error al ajustar la válvula: {e}")

# Ejemplo de uso
ajustar_valvula(25.5)