import time

range_items:int = 10**7

def compare_set_to_list():
    data_list = [i for i in range(range_items)]
    data_set = set()
    for numb in range(range_items):
        data_set.add(numb)
    value_to_check: int = 10**6

    start_time = time.time()
    for _ in range(10**5):
            print(f"the {_+1}'s test to check if {value_to_check} is in dataset => {value_to_check in data_set}")
    print(f"for 100000 iteration in a set it took {time.time() - start_time}'s") #output: for 100000 iteration in a set it took 0.812553882598877's

    start_time = time.time()
    for _ in range(10**5):
            print(f"the {_+1}'s test to check if {value_to_check} is in dataset => {value_to_check in data_list}")
    print(f"for 100000 iteration in a list it took {time.time() - start_time}'s") #output for 100000  iteration in a list it took 585.9723460674286's

#compare_set_to_list()

"""
Problems solved with using list and set. Pinpoint the elements that appear in both of the given lists.
"""
#Problem 1: Array Intersection
#Naive approache
list1 = [3,5,10,54,3,45,33,21,33,24]
list2 = [4,8,3,76,987,65,3,5]
intersection_list = []
start_time = time.time()
for num1 in list1:
    if num1 not in intersection_list:
        for num2 in list2:
            if num1==num2:
                    intersection_list.append(num1)
                    list2.remove(num1)
                    break
    else:
        continue
print(f"it took {time.time() - start_time}'s") #output: it took 5.9604644775390625e-06's
print(intersection_list)

list1 = [3,5,10,54,3,45,33,21,33,24]
list2 = [4,8,3,76,987,65,3,5]
#now using set
start_time = time.time()
set1 = set(list1) 
set2 = set(list2)
intersection = set1 & set2

print(intersection)
print(f"it took {time.time() - start_time}'s") #output: it took 4.0531158447265625e-06's