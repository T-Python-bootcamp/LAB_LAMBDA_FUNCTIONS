
myList = ["Ahmed", "Mohammed", "Mona",
          "Khareem", "Moayed", "Khadeeja", "Salim"]
List = list(filter(lambda item: item[0:2]
            == 'Kh' or item[0:2] == "Mo", myList))
print(List)
