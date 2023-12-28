import requests
   
    
api_url = 'https://jsonplaceholder.typicode.com/posts/1'
response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    for key, value in data.items():
        print(f"{key}: {value}")
else:
    print(f"Error en la solicitud. Código de estado: {response.status_code}")
