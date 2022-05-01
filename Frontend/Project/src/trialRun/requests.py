import requests

url= 'http://localhost:5000/predict_api'

req = requests.get(url ,json = {'ambient_temp':30 , 'module_temp':25 , 'irradiance':0 })

print(req.json())

