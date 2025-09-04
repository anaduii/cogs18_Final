import requests

def test_temperature_finder():
    
    #Adding arguments for the test
    
    date = '2024-03-21'
    time = '00:00:00'
    lat = '52.520551'
    long = '13.461804'
    temp_test = 9.1

    actual_temp = temperature_finder(date, time, lat, long, fahrenheit=False)
    assert actual_temp == temp_test

def test_requests():
    
    #Checking if the website is responsive
    
    response = requests.get('https://api.meteomatics.com/2024-03-21T00:00:00Z/t_2m:F/52.520551,13.461804/json') 
    assert response.status_code == 200