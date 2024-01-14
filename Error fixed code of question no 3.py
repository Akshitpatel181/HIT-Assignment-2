
#Error fixed code of question no 3

global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers():
    global global_variable   #Declare global_variable as global
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:   #Fix the indentation
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

m1_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers()   #Remove the argument, numbers, as it is not used

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable   #Correct the dictionary name

modify_dict()   #Remove the argument, as it is not used

def update_global():
    global global_variable  # Declare global_variable as global
    global_variable += 10

for i in range(5):
    print(i)
    i += 1   #This change has no effect since 'i' is reassigned in the next iteration

if my_dict['key4'] == 10:   #Correct the dictionary name
    print("Condition met!")

if 5 not in my_dict:  # Correct the dictionary name
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
my_set = {1, 2, 3, 4, 5}   #Reset my_set to the correct value
print(my_set)
