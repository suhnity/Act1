#inputting of numbers
first_term = int(input("First term number:"))
last_term= int(input("Last term number:"))

#initialize total sum
total_sum=0

#calculate
for num in range(first_term, last_term +1):
    total_sum += num

#display the result    
print(f"The sum of the numbers from {first_term} to {last_term} is {total_sum}")    