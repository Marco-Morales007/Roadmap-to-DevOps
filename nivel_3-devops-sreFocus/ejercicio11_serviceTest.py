"""
11. Script de prueba de servicios 
    - Verifica si nginx, mysql o ssh están activos, y si no, los reinicia. 
    - Aprende: subprocess, systemctl, status.
"""

import subprocess

# Lista de servicios a monitorear
servicios = ["nginx", "mysql", "ssh"]

def verificar_servicio(servicio):
    try:
        resultado = subprocess.run( # Ejecuta "systemctl is-active servicio"
            ["systemctl", "is-active", servicio],
            capture_output=True,
            text=True
        )
        estado = resultado.stdout.strip()

        if estado == "active":
            print(f"OK: {servicio} se encuentra activo")
        else:
            print(f"FAIL: {servicio} se encuentra inactivo. Intentando reiniciar...")
            reiniciar_servicio(servicio)

    except Exception as e:
        print(f"Error verificando {servicio}: {e}")

def reiniciar_servicio(servicio):
    try:
        subprocess.run(["sudo", "systemctl", "restart", servicio], check=True)
        print(f" {servicio} reiniciado correctamente")
    except subprocess.CalledProcessError:
        print(f" No se pudo reiniciar {servicio} (revisa permisos o logs)")

def main():
    for servicio in servicios:
        verificar_servicio(servicio)

if __name__ == "__main__":
    main()
