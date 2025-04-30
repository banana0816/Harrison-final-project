class books():
    def __init__(self):
        self.author = "harrison"
        self.name = ""
        self.title = ""
        self.price = 0
        self._Books = {"sb"}

    def add(self):
        self.title = input("What book would u like to add")
        print("You have added",self.title)

        self._name = input("enter the name of the book you would like to add: \n").upper
        self._author = input("enter the author of the book you have just added: \n").upper
        self.price = float(input("enter the listing price  of the book: \n"))


        
        self.Books[self._name] = {'author':self._author,'price':self._price}



    def sell(self):
        self.name = input("enter the name of the book you want to sell")
        try:
            str(self.name)
            if self.name in self.Books:
                self.Books.pop(self.name)
                print("the remaining books are:",self.Books)
        except:
            print("please enter a book title")

    def show(self):
        for x in self.Books:

            print(self.title, self.author)
            print(self.price)