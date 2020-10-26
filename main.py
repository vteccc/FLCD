from ST import HashTable

ht = HashTable()
ht.insert("boi")
ht.insert("boi")
ht.insert("bio")
ht.insert("iob")
print(ht.find("boi"))
print(ht.find("bio"))
print(ht.find("iob"))
print(ht.find("b"))

print(ht)
