myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]


filtred_list = list(filter(lambda x: (x.startswith("Kh") or x.startswith("Mo")), myList))
print(filtred_list)