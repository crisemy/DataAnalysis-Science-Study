import requests

# URL de la API de DolarApi para el Dólar Oficial
url = 'https://dolarapi.com/v1/dolares/oficial'

try:
    # Realizar la solicitud GET a la API
    response = requests.get(url)
    response.raise_for_status()  # Lanza un error si la respuesta no es 200 OK
    data = response.json()

    # Extraer la cotización de venta del Dólar Oficial
    valor_venta = data['venta']
    print(valor_venta)

    # Valor en dólares que deseas convertir
    dolares = 100

    # Realizar la conversión
    conversion = dolares * valor_venta
    print(f'{dolares} dólares equivalen a {conversion} pesos argentinos.')

except requests.exceptions.RequestException as e:
    print(f'Error al obtener los datos: {e}')
