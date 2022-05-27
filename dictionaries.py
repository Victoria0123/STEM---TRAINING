#Dictionaries in python
mydict={
    "Book":"Dynamics",
    "Publisher":"Longhorn",
    "Year":2001
}

#Accessing item
x=mydict["Year"]
print(x)

#Accessing using get()
y=mydict.get("Year")
print(y)

#All keys
x=mydict.keys()
print(x)

#All values
x=mydict.values()
print(x)

#Printing all items in a dictionary
x=mydict.items()
print(x)

#Checking if key exists
if "publisher" in mydict:
    print("publisher is one of the keys")
print(len(mydict))    

#Dictionaries can hold different data types
mydict={
    "Book":"Dynamics",
    "Publisher":"Longhorn",
    "Year":2001,
    "Authors":["John", "Mike", "Ike"]
}

