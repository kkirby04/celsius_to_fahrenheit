celsius = int(input())

def conv(c):
    #returning the conversion of the user inputted celsius value 
    return  ((9/5)*c)+32

#setting the fahrenheit value to the function conv() 
fahrenheit = conv(celsius)
#printing out the fahrenheit value
print(fahrenheit)

