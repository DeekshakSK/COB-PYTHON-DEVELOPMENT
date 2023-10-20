import requests, json

apikey = '7040ea904442a45d6950ba584410ce59'
baseurl = 'https://api.openweathermap.org/data/2.5/weather?q='
cityname =input('Enter the City Name: ')

url=baseurl+cityname+'&appid='+apikey
print('URL : ',url,'\n')

response = requests.get(url)
data=response.json()

#print(data)


print('Current Temparature = ',data['main']['temp'])
print('Maximum Temparature = ',data['main']['temp_max'])
print('Minimum Temparature = ',data['main']['temp_min'])
print('Humidity = ',data['main']['humidity'])
print('Pressure = ',data['main']['pressure'])
