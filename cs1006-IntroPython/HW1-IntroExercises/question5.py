#Question 5 

def sayHello(name):
    print("Hello {}!".format(name))
    
def countChar(name):
    print("You have", len(name), "letters in your name.")

def even(name):
    if (len(name) % 2) == 0:
        print("You have an even number of letters in your name.")
    else: 
        print("You have an odd number of letters in your name.")
  
def listChar(name):
    x = list(name) 
    n= 0
    while n < len(x):
        print("Letter", n, "is:", x[n])
        n = n + 1


def main():
    name = input("Enter your first name: ")
    sayHello(name)  
    countChar(name)
    even(name)
    listChar(name)
    
main()