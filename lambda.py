myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]



listes=list(filter(lambda xx:  xx [0:2]=="Kh" or xx [0:2]=="Mo",myList))
print(listes)