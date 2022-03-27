# These codes prints list
#countries=['NG', 'US', 'UK', 'GH', 'SZ', 'EGY', 'MCA']
#print(countries[-5])


#countries=['NG', 0, 'UK', [1, 2, 'EGY'], 3.244]
#print(countries[3][2])
   
# These codes is used for user define function
'''
def addition_function(num1, num2):
   return num1 + num2  # what you want the function to do for you

addition_function(4, 5) 
print(addition_function(num1, num2))

'''
# These codes reads files 

#CountryName = open("C:/Users/Alima/Desktop/pythonPortfolioRef/NamesOfCountries.txt", "r")
#print(CountryName.readlines()[2])
#CountryName.close()

# These codes write files 
'''
CountryName = open("C:/Users/Alima/Desktop/pythonPortfolioRef/NamesOfCountries.txt", "w")
print(CountryName.write('My name is Alimat'))
CountryName.close()
'''
# This code is use to specify class of object in other to use many data
'''
class Person:
   def __init__(self, name, age):
          self.name = name
          self.age = age
name = input('Enter your name: ')
age = input('Enter your age: ')
p1 = Person(name, age)
print(p1.name)  
print(p1.age)

'''


        
