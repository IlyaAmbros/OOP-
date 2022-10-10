import time
from random import randint
from datetime import datetime
from os import system

##########################################################################################################################################################################

def formating(x):
    format_x = str(x).zfill(2) + "/"
    return format_x

def formating_2(x):
    format_x = (6 - len(str(x)))*"0" + str(x)
    return format_x

def createId():
    result = time.localtime(int(randint(100000000, 1664817163)))
    id = formating(result.tm_year) + formating(result.tm_mon) + formating(result.tm_mday) + formating(result.tm_hour) + formating(result.tm_min) + formating(result.tm_sec) + formating_2(randint( 0 , 999999)) #str(randint( 0 , 999999)).zfill(6)
    return id

def getId():
    today = datetime.today()
    d = today.strftime("%Y-%m-%d-%H-%M-%S")
    r = randint( 0 , 999999)
    return f'{d}-{r:06b}'

def addressCorrection(x):
    parts = x.strip().split()
    if len(parts) == 3:
        if parts[0].isalpha() == True and len(parts[0]) > 3 :
                if parts[1].isalpha() == True and len(parts[1]) > 3 :
                    if parts[2].isnumeric() == True and len(parts[2]) <= 4 :
                        correct_data = [ parts[0].title() , parts[1].title() , parts[2]]
                        return correct_data

def nameCorrection(x):
    parts = x.strip().split()
    if len(parts) == 2:
        if parts[0].isalpha() == True and len(parts[0]) >= 3 :
                if parts[1].isalpha() == True and len(parts[1]) >= 3 :
                    correct_data = [ parts[0].title() , parts[1].title() ]
                    return correct_data

def format(x):
    return f"# {x}"

def createMenu():
    menu = []
    food = [ "pizza" , "fish" , "burgers" , "gamburgers" , "salads" , "sausages" , "poke" , "steaks" , "pasta" , "meat" , "pork" , "spaghetti" , "pasta" , "carbonara" , "sushi" , "soup" ]
    for i in range (len(food)) :
        menu.append(Products( food[i] , randint( 30 , 150 ) ))
    return menu

def printMenu(x):
    print ( "\n" , format("Welcome to Delivery club ") , "\n" )
    print ( format("Let me suggest our menu :") , "\n" )
    for i in range (len(x)) :
        print( format(x[i]) , "\n")

def clear():
    return system("cls")

##########################################################################################################################################################################

class Products :

    def __init__(self , name , price):
        self.id = createId()
        # self.id = getId()
        self.name = name
        self.setPrice(price)
    
    def __str__(self):
        return f"Product ( id : {self.id} ; name : {self.name} ; price : {self.__price})"

    def __repr__(self):
        return self.__str__()

    def getPrice(self):
        return self.__price

    def setPrice(self , price ):
        if price >= 0:
            self.__price = price
        else:
            print("ERROR: product price cannotbe negative !!!")

##########################################################################################################################################################################

class Client:

    def __init__( self , fullname , physicalAddress ):
        self.id = createId()
        self.setFullname( fullname )
        self.setPhysicalAddress( physicalAddress )

    def __str__(self):
        if type(self) == "<class 'NoneType'>" :
            return "Error !!! The data was entered incorrectly ."
        else :
            return f"\nClient :\n\n1) fullname : {self.__fullname[0]}  {self.__fullname[1]} ;\n\n2) physicalAddress {self.__physicalAddress[0]} , {self.__physicalAddress[1]} {self.__physicalAddress[2]} ;\n\n3) id : {self.id} ."

    def __repr__(self):
        return self.__str__()

    def getFullname(self):
            return self.__fullname

    def setFullname(self , fullname ):
        self.__fullname = nameCorrection(fullname)

    def getPhysicalAddress(self):
        return self.__physicalAddress

    def setPhysicalAddress(self , physicalAddress ):
        self.__physicalAddress = addressCorrection(physicalAddress)

##########################################################################################################################################################################

class Bag :
    def __init__(self , prodacts ):
        self.client = p1.getFullname()
        self.setData(prodacts)
        self.setData(prodacts)
        self.setData(prodacts)

    def __str__(self):
        if len(self.__products) == 0 :
            print ("There are no products in the basket !!!")
        else :
            print( f"\nA receipt in the name of {self.client[0]}  {self.client[1]} :\n" )
            for i in range(len(self.__products)):
                print(f"# {i+1}) {self.__products[i]} : {self.__id[i]} ;")
            print(f"# Total cost of the order = {self.__cost}")


    def __repr__(self):
        return self.__str__()

    def getId(self):
        return self.__id
    
    def getProducts(self):
        return self.__products

    def getCost(self):
        return self.__cost 

    def setData(self , prodacts ):
        self.__products = []
        self.__id = []
        self.__cost = 0 
        list_prodacts = prodacts.strip().split()
        for i in range(len(list_prodacts)):
            for j in range (len(menu)) :
                if list_prodacts[i] == menu[j].name :
                    self.__products.append( menu[j].name )
                    self.__id.append( menu[j].id )
                    self.__cost += menu[j].setPrice()

##########################################################################################################################################################################

clear()

menu = createMenu()

name = input ("Enter your fullname : ")
print()
adress = input ("Enter your address : ")

clear() 

p1 = Client( name , adress )
print(p1)

printMenu(menu)

prodacts = str(input("Keep the products you want to fill the basket with :"))

Bag(prodacts)
