#input number
num = int(input("Enter number: "))

#check if number is greater than 1
if num < 2:
    is_prime = False
    
else:
    for i in range(2, int(num ** 0.5) +1):
        if num % i == 0: #not prime if divisible by any number
            is_prime = False
            break #exit loop
    
#display result
if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")