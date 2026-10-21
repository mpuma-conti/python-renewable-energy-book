import subprocess

# Ejemplo de configuración de firewall para permitir solo tráfico desde una IP específica
def configurar_firewall(ip_permitida):
    # Comando para permitir tráfico desde la IP permitida
    comando = f"sudo ufw allow from {ip_permitida}"
    subprocess.run(comando, shell=True)

# Configurar firewall para permitir tráfico desde 192.168.1.100
configurar_firewall("192.168.1.100")