# printing the sum of current and previous number
print ("Printing current and previous number sum in range (10)")

# first is to initialize a variable to store previous number which is the 0
previous_number = 0

# repeat the first 10 numbers
for i in range (0,10):

# then calculate for the sum of the current and previous number
    sum = previous_number + i

# print 
    print("The current number is", i, "and the previous number is", previous_number, "sum:", sum)

# update the previous number for the next repeatition 
    previous_number = i
