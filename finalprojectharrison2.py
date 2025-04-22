from finalprojectharrison import books

b = books()

print(b.name)
v = input("would u like to add a book?('yes','no')")
if v == "yes":
    c = b.add()