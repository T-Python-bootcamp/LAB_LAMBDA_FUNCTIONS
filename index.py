## Given the following list, using a lambda function , filter the list to include only names starting in "Kh" and "Mo".
myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]
new_list=list(filter(lambda x:(x.find("Kh")==0 or x.find("Mo")==0),myList))
print(new_list)