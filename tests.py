#!/usr/bin/env python
# coding: utf-8

# File for running tests for conversions

import conversions
import unittest


class TestConversions(unittest.TestCase):
    
    # Function to test celsius to kelvin conversion
    def testConvertCelsiusToKelvin(self):
        result = conversions.convertCelsiusToKelvin(20.0)
        self.assertEqual(result, 293.15)

    # Function to test celisus to fahrenheit conversion
    def testConvertCelsiusToFahrenheit(self):   
        result = conversions.convertCelsiusToFahrenheit(12.4)
        self.assertEqual(result, 54.32)

    # Function to test fahrenheit to celsius conversion
    def testConvertFahrenheitToCelsius(self):
        result = conversions.convertFahrenheitToCelsius(70.0)
        self.assertEqual(result, 21.11)
   
    # Function to test fahrenheit to kelvin conversion
    def testConvertFahrenheitToKelvin(self):
        result = conversions.convertFahrenheitToKelvin(70.0)
        self.assertEqual(result, 294.26)
    
    # Function to test kelvin to celsius conversion
    def testConvertKelvinToCelsius(self):
        result = conversions.convertKelvinToCelsius(200.0)
        self.assertEqual(result, -73.15)
    
    # Function to test kelvin to fahrenheit conversion
    def testConvertKelvinToFahrenheit(self):
        result = conversions.convertKelvinToFahrenheit(190.09)
        self.assertEqual(result, -117.51)

# Main function to run tests

if __name__ == '__main__':
    unittest.main()
