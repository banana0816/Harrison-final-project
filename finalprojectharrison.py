class books():  
    def __init__(self):
                self.author = "harrison"
                self.name = ""
                self.title = ""
                self.price = 0
                self.Books = {}

    def Load(self, filename = "books.txt"):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    parts = line.strip().split(', ')
                    if len(parts) !=3:
                        print(f"error {parts}")
                        continue
                    title,author,price = parts
                    self.Books[title] = {'author': author,'price': float(price)}
            print("Books loaded from file.")
        except FileNotFoundError:
            print("File not found.")

    def add(self):
        self.name = input("enter the name of the book you would like to add: \n").upper()
        self.author = input("enter the author of the book you have just added: \n").upper()
        self.price = float(input("enter the listing price of the book: \n"))
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
        self.Load()
        for i in self.Books:
            print(i)
            print(self.Books[i]["author"])
            print(self.Books[i]["price"])

    def Save(self, filename = "books.txt"):
        with open(filename, 'w') as file:
            for i in self.Books:
                author = self.Books[i]['author']
                price = self.Books[i]['price']
                file.write(f"{i}, {author}, {price}\n")
        print("Books saved to file.")

    

    