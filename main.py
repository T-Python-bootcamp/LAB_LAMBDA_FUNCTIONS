

myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

filtered_list = filter( lambda x:(x[0:2]=='Kh' or x[0:2]=='Mo') , myList )
filtered_list = list(filtered_list)
print(filtered_list)