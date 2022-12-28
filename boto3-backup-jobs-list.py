import boto3
from datetime import datetime, timedelta

# Crea un cliente de AWS Backup
client = boto3.client('backup')

# Calcula la fecha de hace 3 meses
three_months_ago = datetime.now() - timedelta(days=90)

# Inicializa la variable NextToken con None
next_token = None

# Inicializa una lista vacía para almacenar los trabajos de copia de seguridad
backup_jobs = []

# Utiliza un bucle while para llamar repetidamente al método list_backup_jobs
# hasta que no se devuelva un NextToken
while True:
    # Crea un diccionario de parámetros para la llamada al método list_backup_jobs
    params = {
        'ByCreatedAfter': three_months_ago,
        'ByCreatedBefore': datetime.now(),
        'MaxResults': 100
    }

    # Si next_token no es None, agrega el parámetro NextToken al diccionario de parámetros
    if next_token is not None:
        params['NextToken'] = next_token

    # Llama al método list_backup_jobs y proporciona los parámetros necesarios
    response = client.list_backup_jobs(**params)

    # Agrega los trabajos de copia de seguridad devueltos a la lista
    backup_jobs.extend(response['BackupJobs'])

    # Asigna el NextToken devuelto a la variable next_token
    # para utilizarlo en la siguiente iteración del bucle
    next_token = response.get('NextToken')

    # Si no se devuelve un NextToken, sale del bucle
    if next_token is None:
        break

# Muestra la lista de trabajos de copia de seguridad
print(backup_jobs)
