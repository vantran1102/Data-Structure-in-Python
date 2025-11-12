from hash import HashTable

myHash = HashTable()
myHash.print_hash()

myHash.set("A", 1000)
myHash.set("B", 2000)
myHash.set('C', 3000)
print("after set key-value: ")
myHash.print_hash()
print("get item")
print("Value of B is: ", myHash.get("B"))
print("Value of C is: ",myHash.get("C"))
print("Print all Key")
print(myHash.key())

