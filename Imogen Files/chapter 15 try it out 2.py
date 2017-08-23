import my_module

from my_module import c_to_f

celcius = float(raw_input ("Enter a temperature in celcius: "))
fahrenheit = c_to_f(celcius)
print "That's ", fahrenheit, "degrees fahrenheit"
