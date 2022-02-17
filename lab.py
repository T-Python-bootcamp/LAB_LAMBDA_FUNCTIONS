myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]
specialList = list(filter(lambda lst: lst[0:2] =="Kh" or lst[0:2] =="Mo",myList))
print(specialList)