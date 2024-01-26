# printing the sum of current and previous number
print ("Printing current and previous number sum in range (10)")

# first is to initialize a variable to store previous number which is the 0
previous_number = 0

# repeat the first 10 numbers
for i in range (1,5):

# then calculate for the sum of the current and previous number
    current_number = i
    sum = previous_number + current_number

# print 
    print("Sum of", current_number, "and", previous_number, "is", sum)

# update the previous number for the next repeatition 
previous_number = current_number
