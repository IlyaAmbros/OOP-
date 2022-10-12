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
        x = ['A' , 'B' , 'C' , 'D' , 'E' , 'F']
        y = [10 , 11 , 12 , 13 , 14 , 15]

        parts = id.split( "-" , 6 )
        z = int(parts[6][2]) + int(parts[6][4]) + int(parts[6][5])
        for i in range(len(x)):
            if y[i] == z :
                parts[6] = parts[6][0] + x[i] + parts[6][1] + parts[6][3] + "0"

        result = " "
        for i in range(5) :
            result += (parts[i] + "-")
        final_result = result + parts[6]
        self.__id = final_result


product = Products( "2022-01-10-11-01-01-123456" , "Pasta" , 110 )
print(product)
        