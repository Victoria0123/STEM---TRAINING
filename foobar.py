def print_nums (n):
    for num in range (n):
        if num % 3==0 and num % 5!=0:
           print("foo")
        if num % 5==0 and num % 3!=0:
            print("bar")
        if num % 3==0 and num % 5==0:
            print("foobar")
        if num % 3 !=0 and num % 5 !=0:
            print(num)
       
print_nums(10)
 
def print_nums (n):
    for num in range (n):
        if num >5:
            print("greater than")
        else:
            print(num)

print_nums(10)

