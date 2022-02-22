myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

names = list(filter(lambda i : i.startswith("Kh") or i.startswith("Mo") , myList))

print(names)