import os
os.system('cls')

#Write a function to calculate and return the wind chill based on a given temperature and wind speed.
def windchill(temp,wind_speed):
  windchill_in_farenheit = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed**0.16)) + (0.4275 * temp * (wind_speed**0.16))
#   return windchill_in_farenheit
  print (f'At temperature {temp}F, and wind speed {wind_speed} mph, the windchill is: {windchill_in_farenheit:.2f}')

  
#Write a function to convert from Celsius to Fahrenheit.
def celcius_to_fahrenheit(celcius):
  converted_fahrenheit = celcius * 1.8 + 32
 
#Allow the user to enter the temperature in Celsius of Fahrenheit.
temp = float(input('What is the temperature? '))
ask_temp_type = input('What tempterature are you inputing?\nFahrenheit or Celcius\nPlease use (F or C) ')    

wind_speed = 0
while wind_speed <= 55:
  wind_speed = wind_speed + 5
#If they provide it in Celsius, first convert it to Fahrenheit before using the formula above. 
  if ask_temp_type.upper() == 'C': 
    celcius = temp  
    celcius_to_fahrenheit(celcius)
    windchill(temp,wind_speed)
  else:
    windchill(temp,wind_speed)
    
    
    