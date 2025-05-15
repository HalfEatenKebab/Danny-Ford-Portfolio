from sys import argv
from car_list import cars


#-------------------------------------------------------------------------------
# This chunk of code chekcs if we want add a car, calls the create_car function, then calls add_car to add it to our list

def check_add_car(car_list):  
    answer = str(input("Do you want to add a car? Y/N \n > "))
    if answer in ["y", "Y", "Yes", "yes", "YES"]: 
        new_car = create_car() 
        add_car(car_list, new_car)
        check_add_car(car_list) 
    else:
        change_car(car_list)

def add_car(car_list, new_car):
    car_list.append(new_car)
    

#-------------------------------------------------------------------------------
# These blocks of functions are the princple for creating any new cars, having sepearte functions for each list/dict parameters

def create_car():   
    new_model = model()
    new_color = color(new_model)
    new_speed = speed(new_model)
    print(f"So you have a {new_color} {new_model} that reaches {new_speed} mph! Nice!")
    
    car = {'model': new_model,
           'color': new_color, 
           'speed': new_speed
          }
    return car


def model():
    print("What is the model of your car?")
    model_name = input('> ')
    return model_name
    
def color(model_name):
    print(f"What is the color of your {model_name}?")
    color = input('> ')
    return color

def speed(model_name):
    print(f"What is the top speed of the {model_name}")
    speed = int(input('> '))
    return speed



#-------------------------------------------------------------------------------
# This block starts the option to change details in the list

def change_car(car_list):
    answer = str(input("Would you like to change a car's details?\n > "))
    if answer in ["y", "Y", "Yes", "yes", "YES"]:  
        car_to_change = input("What car do you want to change \n > ") 
        for car in car_list:
            if car['model'] == car_to_change:
                
                type = str(input("What would you like to change?\n 'Model'-'Color'-'Speed'\n> "))
            
                if type in ["Model", "model"]:
                    change_model(car_list, car_to_change)
                    break
                    
                if type in ["Color","color"]:
                    change_color(car_list, car_to_change)
                    break
                    
                if type in ["Speed", "speed"]:
                    change_speed(car_list, car_to_change)
                    break
                    
        if car['model'] != car_to_change:
            print(f"Error: {car_to_change} cannot be found, please try again")
            del car_to_change
            change_car(car_list)
# BUG: The for loop only goes through twice, if you enter a car that is in the list second time around it moves past the if car == car_to_change. Will also skip through even if it gets two negative results
                
#-------------------------------------------------------------------------------    

def change_model(car_list, car_to_change):
    print(f"Changing the {car_to_change} model name")

def change_color(car_list, car_to_change):
    print(f"Changing the {car_to_change} color")

def change_speed(car_list, car_to_change):
    print(f"Changing the {car_to_change} top speed")


    
#-------------------------------------------------------------------------------
# Anytime we want to read the entire car list from the console

def read_list(car_list):
    print("\nPrinting the data:")
    for car in car_list:
        print(car)
    

#-------------------------------------------------------------------------------

check_add_car(cars)
read_list(cars)



# To improve this further I could:
# - Edit the list/dict from the console, rather than entering the file manually 
# - Beable to add new dict items, which will then add onto current saved dicts
#     ~ Given option to edit all straight away or to fill with 'none'

 




