# mul = lambda x,y: x*y
# print(mul(4,5))

# listtt=[1,2,4,5,6,7,8,9,10]
# even = list(filter(lambda x : x%2 == 0 , listtt))
# print(even)

myList = ["Ahmed", "Mohammed", "Mona", "Khareem", "Moayed", "Khadeeja", "Salim"]

names = list(filter(lambda i : i.startswith("Kh") or i.startswith("Mo") , myList))

print(names)