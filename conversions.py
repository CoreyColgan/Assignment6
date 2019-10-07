#!/usr/bin/env python
# coding: utf-8

# In[10]:


#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Part 1 - create functions to test celsius conversions

# Function to test celcius to kelvin
def convertCelciusToKelvin(celciusMeasurement):
    celsiusToKelvin = celciusMeasurement + 273.15
    celsiusToKelvin = (round(celsiusToKelvin,4))
    return celsiusToKelvin

# Function to test kelvin to celsius
def convertKelvinToCelcius(kelvinMeasurement):
    kelvinToCelsius = kelvinMeasurement - 273.15
    kelvinToCelsius = (round(kelvinToCelsius,4))
    return kelvinToCelsius

# Function to test celsius to fahrenheit
def convertCelciusToFahrenheit(celciusMeasurement):
    celsiusToFahrenheit = ((celciusMeasurement * 9.0) / 5.0) + 32.0
    celsiusToFahrenheit = (round(celsiusToFahrenheit,4))
    return celsiusToFahrenheit

# Function to test fahrenheit to celsius
def convertFahrenheitToCelsius(fahrenheitMeasurement):
    fahrenheitToCelsius = ((fahrenheitMeasurement - 32.0) * 5.0) / 9.0
    fahrenheitToCelsius = (round(fahrenheitToCelsius,4))
    return fahrenheitToCelsius

# Function to test fahrenheit to kelvin
def convertFahrenheitToKelvin(fahrenheitMeasurement):
    fahrenheitToKelvin = ((fahrenheitMeasurement + 459.67) * 5.0) / 9.0
    fahrenheitToKelvin = (round(fahrenheitToKelvin,4))
    return fahrenheitToKelvin

# Function to test kelvin to fahrenheit
def convertKelvinToFahrenheit(kelvinMeasurement):
    kelvinToFahrenheit = ((kelvinMeasurement * 9.0) / 5.0) - 459.67
    kelvinToFahrenheit = (round(kelvinToFahrenheit,4))
    return kelvinToFahrenheit


# In[ ]:





# In[ ]:




