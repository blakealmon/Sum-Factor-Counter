#  ----- || Built by Blake Almon || -----

#gets all factors for 3 and 5, then gets the sum of them.

factorOne = 3
factorTwo = 5

# || Input, use  -- 1000 --
x = int(input())

# || Creating list
list = []

# || For Loop
for x in range(x):

    # || If statement for -- 3 --
    if(x % factorOne == 0):

         # || Adding x to the list if it is divisible by -- 3 --
        list.append(x)
    
    # || Elif statment for -- 5 --
    elif(x % factorTwo == 0):

        # || Adding x to the list if it is divisible by -- 5 --
        list.append(x)

# || Printing out sum of the list
print(sum(list))


# || In the If staments you can change -- 3 -- and -- 5 -- to other numbers as you please