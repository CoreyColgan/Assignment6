#!/usr/bin/env python
# coding: utf-8

# In[16]:


#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# Create class for exception handling invalid conversions

class CatchFaultyConversion(Exception):
    pass

# Create a new method inside of a new file (called conversions_refactored.py) named convert that takes in 3 values:
   # 1.fromUnit ­ the unit we are converting from, as a string
   # 2.toUnit ­ the unit we are converting to, as a string
   # 3.value ­ the value of fromUnit we are converting from
    
def conversions(fromUnit, toUnit, val):

    if fromUnit.lower() == "Celsius" and toUnit.lower() == "Kelvin":
        return float(val) + 273.15

    elif fromUnit.lower() == "Celsius" and toUnit.lower() == "Fahrenheit":
        return float(val) * 9 / 5 + 32

    elif fromUnit.lower() == "Fahrenheit" and toUnit.lower() == "Celsius":
        return (float(val) - 32) * 5 / 9

    elif fromUnit.lower() == "Fahrenheit" and toUnit.lower() == "Kelvin":
        return (float(val) + 459.67) * 5 / 9

    elif fromUnit.lower() == "Kelvin" and toUnit.lower() == "Fahrenheit":
        return float(val) * 9 / 5 - 459.67

    elif fromUnit.lower() == "Kelvin" and toUnit.lower() == "Celsius":
        return float(val) - 273.15

    elif fromUnit.lower() == "Yards" and toUnit.lower() == "Miles":
        return float(val) / 1760

    elif fromUnit.lower() == "Yards" and toUnit.lower() == "Meters":
        return float(val) / 1.094

    elif fromUnit.lower() == "Meters" and toUnit.lower() == "Yards":
        return float(val) * 1.094

    elif fromUnit.lower() == "Meters" and toUnit.lower() == "Miles":
        return float(val) / 1609.344

    elif fromUnit.lower() == "Miles" and toUnit.lower() == "Yards":
        return float(val) * 1760

    elif fromUnit.lower() == "Miles" and toUnit.lower() == "Meters":
        return float(val) * 1609.344

    elif fromUnit.lower() == toUnit.lower():
        return val

    else:
        raise CatchFaultyConversion("Input is invalid.")


# In[ ]:





# In[ ]:




