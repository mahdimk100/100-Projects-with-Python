import requests

print("\t\tWelcome to the Weather Forecaster!\n\n")
print('Just Enter the City you want the weather report for and click on the button! It is that simple!\n\n')

city_name = input('Enter the name of City : ')
print('\n\n')

def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = 'Erorr Occurred'
    print(T)

Gen_report(city_name)