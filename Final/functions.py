
import requests

import ipywidgets as widgets



def temperature_finder(date, time, lat, long, fahrenheit=True):
   
    #Checking for the correct temp unit
    if fahrenheit:
        temp_unit = 'F'
    else:
        temp_unit = 'C'
    
    #Uses arguments to finish the url and allows access to website with the data
    url = f'https://api.meteomatics.com/{date}T{time}Z/t_2m:{temp_unit}/{lat},{long}/json'
    weather_data = requests.get(url, auth=('ucsd_ghimire_anadi', '99tNrBzNb7')).json()
    
    #Code for checking the full output; meant for debugging
    #print("API Response:", weather_data)  
    
    #returns the temp vaule by going through the data in the .json file
    temperature_value = weather_data['data'][0]['coordinates'][0]['dates'][-0]['value']
    return temperature_value 


@widgets.interact(
    
    #spinoff from the Lecture Interact Decor
    
    
    date='2024-03-21',
    time='12:00',
    lat=(-90, 90),
    long=(-180, 180),
    fahrenheit=True
)
def temperature_finder(date, time, lat, long, fahrenheit=True):
   
    #Checking for the correct temp unit
    if fahrenheit:
        temp_unit = 'F'
    else:
        temp_unit = 'C'
    
    #Uses arguments to finish the url and allows access to website with the data
    url = f'https://api.meteomatics.com/{date}T{time}Z/t_2m:{temp_unit}/{lat},{long}/json'
    weather_data = requests.get(url, auth=('ucsd_ghimire_anadi', '99tNrBzNb7')).json()
    
    #Code for checking the full output; meant for debugging
    print("API Response:", weather_data)  
    
    #returns the temp vaule by going through the data in the .json file
    temperature_value = weather_data['data'][0]['coordinates'][0]['dates'][-0]['value']
    return temperature_value 