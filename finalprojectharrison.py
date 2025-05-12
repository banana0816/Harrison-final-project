class books(): 
    def __init__(self):
                self.author = "harrison"
                self.name = ""
                self.title = ""
                self.price = 0
                self.Books = {}

    def add(self):
        self.title = input("What book would u like to add")
        print("You have added", self.title)

        self.name = input("enter the name of the book you would like to add: \n").upper()
        self.author = input("enter the author of the book you have just added: \n").upper()
        self.price = float(input("enter the listing price  of the book: \n"))
        
        self.Books[self.name] = {"author" : self.author,"price" : self.price}



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
        for i in self.Books:
            print(i)#0
            print(self.Books[i])#harry potter
            print(self.Books[i]["author"])#J.K.Rowling         
            print(self.Books[i]["price"])#1

    def Save(self, filename = "books.txt"):
        with open(filename, 'w') as file:
            for i in self.Books:
                file.write(f"{self.Books[i]}, ")
                file.write(f"{self.Books[i]["author"]}, ")
                file.write(f"{self.Books[i]["price"]}\n")
        print("Books saved to file.")

    def Load(self, filename = "books.txt"):
        try:
            with open(filename, 'r') as file:

                for line in file:
                    title, author, price = line.strip().split(', ')
                    self.Books[title] = {'author': author,'price': float(price)}
            print("Books loaded from file.")
        except FileNotFoundError:
            print("File not found.")

      

                    