class Products :

    def __init__(self , id , name , price):
        self.setId(id)
        # self.id = getId()
        self.name = name
        self.setPrice(price)
    
    def __str__(self):
        return f"Product ( id : {self.__id} ; name : {self.name} ; price : {self.__price})"

    def __repr__(self):
        return self.__str__()

    def getPrice(self):
        return self.__price

    def setPrice(self , price ):
        if price >= 0:
            self.__price = price
        else:
            print("ERROR: product price cannotbe negative !!!")

    def getId(self):
        return self.__id

    def setId(self , id ):
        parts = id.split( "-" , 6 )
        x = hex(int(parts[6]))
        parts_2 = x.split("x")
        self.__id =  f'{parts[0]}-{parts[1]}-{parts[2]}-{parts[3]}-{parts[4]}-{parts[5]}-{parts_2[1]}'
        return self.__id


product = Products( "2022-01-10-11-01-01-123456" , "Pasta" , 110 )
print(product)

        