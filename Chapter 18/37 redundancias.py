import threading

def funcion_principal():
    try:
        # Código principal del sistema
        while True:
            # Operaciones críticas
            pass
    except Exception as e:
        print(f"Error en la función principal: {e}")

def funcion_backup():
    try:
        # Código de respaldo
        while True:
            # Operaciones críticas de respaldo
            pass
    except Exception as e:
        print(f"Error en la función de respaldo: {e}")

# Iniciar ambas funciones en hilos separados
thread_main = threading.Thread(target=funcion_principal)
thread_backup = threading.Thread(target=funcion_backup)

thread_main.start()
thread_backup.start()