import time
from random import randint
from faker import Faker
from os import system
fake = Faker()

# Creating an Id

def formating(x):
    format_x = str(x).zfill(2) + "/"
    return format_x

def createId():
    result = time.localtime(int(randint(100000000, 1664817163)))
    id = formating(result.tm_year) + formating(result.tm_mon) + formating(result.tm_mday) + formating(result.tm_hour) + formating(result.tm_min) + formating(result.tm_sec) + str(randint( 100000 , 999999))
    return id

# Declaring classes

class Products :
    def __init__(self , id , name , price):
        self.id = id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"Product ( id : {self.id} ; name : {self.name} ; price : {self.price})"

class Client:
    def __init__( self , id , fullname , physicalAddress ):
        self.id = id
        self.fullname = fullname
        self.physicalAddress = physicalAddress
    def __str__(self):
        return f" Client ( id : {self.id} ; fullname : {self.fullname} ; physicalAddress : {self.physicalAddress})"

#############################################################

all_products = []

for i in range (100):
    p =  Products( createId() , "product X" , randint( 100, 300 ) )
    all_products.append(p)

system("cls")

task_completed = False

for i in range (len(all_products)):
    print()
    print(all_products[i])
    for j in range (len(all_products)):
        if i != j :
            if all_products[i].id == all_products[j].id :
                task_completed = False
                break
            else :
                task_completed = True
    if task_completed == False :
        print (100*"#" + "\n" + "Result = The task failed !!!\n" + 100*"#")
        break

print()

if task_completed == True :
    print (100*"#" + "\n" + "Result = Task completed !!!\n" + 100*"#")

