my_list = [5,2,3,1,4] # my number list

my_list2 = ["a","b","c"] # my string list

greatest = max(my_list) # greatest number value in the list
smallest = min(my_list) # smallest number value in the list

print(f"The greatest number in the list {greatest}") # prints the greatest
print(f"The smallest number in the list {smallest}") # prints the smallest

list_sum = sum(my_list) # Creates a new variable with the sum of all digits in the list
print(f"The sum of all numbers in the list {list_sum}") # prints the sum of the list

my_list_lenght = len(my_list) # gets a new varaible with the value of the lenght of my list
print(f"The lenght of my list is {my_list_lenght}") # prints my list lenght

in_order = sorted(my_list) # sorting the list in alphabetical order
print(f"My sorted list {in_order}") # printing the list in alphabetical order

def filter_prize(prize):
    if (prize >= 400):
        return True
    else: 
        return False

item_prize = [230,400,450,350,370]
filtered_prize = filter(filter_prize,item_prize)
print(list(filtered_prize))
