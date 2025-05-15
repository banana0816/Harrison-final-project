from finalprojectharrison import books
b = books()

"""def Load(self, filename = "books.txt"):
        try:
            with open(filename, 'r') as file:

                for line in file:
                    title, author, price = line.strip().split(', ')
                    self.Books[title] = {'author': author,'price': float(price)}
            print("Books loaded from file.")
        except FileNotFoundError:
            print("File not found.")"""

b.Load()

print(b.name)
v = input("would u like to add a book?('yes','no')")
if v == "yes":
    c = b.add()
v = input("would u like to remove a book?('yes','no')")
if v == "yes":
    c = b.sell()
v = input("would u like to see the books?('yes','no')")
if v == "yes":
    c = b.show()
v = input("would u like to save the books?('yes','no')")
if v == "yes":
    c = b.Save()