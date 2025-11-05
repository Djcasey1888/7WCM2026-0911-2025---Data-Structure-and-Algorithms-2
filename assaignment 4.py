def collatz(n):

    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=n*3 + 1
        print("Your number is now ", n)

        
    print("Your end result is ",n)
        
n=int(input("Choose a positive integer: "))
 
if n>0 and n%2==0:
    collatz(n)
else:
    print("Please choose a positive integer")
    

    
