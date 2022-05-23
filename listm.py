#for loops in python
mangoes = "Book"
for i in mangoes:
   print(i)
print("done") 

#for loops with lists
words=["I", "DID", "A"]
for word in words:
    print(word + "i")

#counting letters in strings
str="Hello guys welcome back to my class"
count=0
for x in str:
  if(x=='o'):
    count+=1
print("the number of o's is:",count)    