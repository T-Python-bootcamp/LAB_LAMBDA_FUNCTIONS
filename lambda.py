myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filtered = list(filter(lambda item: item.startswith("Kh") or item.startswith("Mo"), myList))
