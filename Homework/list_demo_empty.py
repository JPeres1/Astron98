
# Let's start with an empty list:
fruits = []


#Next, let's add the following fruits to the list: 'apple', 'banana', and 'kiwi'.
fruits.append('apple')
fruits.append('banana')
fruits.append('kiwi')



#Print the second element in the list (which index would that be?)

print(fruits[1])

#Now add another 'banana' to the end of the list, and replace the first one with 'cherry'.
#See if you can do this without actually typing out 'banana' in your code.

fruits.append(fruits[1])
fruits[1]="cherry"
print(fruits)

#Sort the list in alphabetical order (see built in methods)
fruits.sort()


#Print the length of fruits
print(len(fruits))





#SECOND DEMO

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Slice the list to include only the integers from 2 to 9 (inclusive) and print its length.
nums= nums[1:9]
print(len(nums))
print(nums)
#Now create a new list with all of the odd numbers in nums in decreasing order
nums_reverse=nums[9::-2]
print(nums_reverse)
# Creating two sample lists with different types of elements


# Concatenating lists using the '+' operator



# Printing the concatenated list


# Creating another sample list



# Concatenating lists using the 'extend()' method



# Printing the updated list1 after concatenation using 'extend()'




