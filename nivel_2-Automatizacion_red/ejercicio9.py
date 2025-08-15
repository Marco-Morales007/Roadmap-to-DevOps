#instalar crontab si no lo tienes
# sudo apt-get install cron

from crontab import CronTab
import os

# Usuario actual
cron = CronTab(user=True)

# Carpeta origen y destino
source_folder = "/home/antonius/Desktop/my_projects/Roadmap-to-DevOps"
backup_folder = "/home/antonius/backups"

# Crear carpeta de backups si no existe
os.makedirs(backup_folder, exist_ok=True)

# Comando para crear el backup con fecha
backup_command = f"tar -czf {backup_folder}/backup_$(date +\\%Y\\%m\\%d_\\%H\\%M\\%S).tar.gz -C {os.path.dirname(source_folder)} {os.path.basename(source_folder)}"

# Verificar si ya existe un cron job igual
exists = False
for job in cron:
    if backup_command in job.command:
        exists = True
        print("El cron job ya existe.")
        break

if not exists:
    # Crear nuevo cron job
    job = cron.new(command=backup_command)
    job.setall("0 0 * * *")  # Ejecutar todos los días a medianoche
    cron.write()
    print("Cron job creado: se ejecutará cada 24 horas a medianoche.")