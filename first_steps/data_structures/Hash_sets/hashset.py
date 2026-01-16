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
Problems solved with using list and set.. 
"""
#Problem 1: Array Intersection =>  Pinpoint the elements that appear in both of the given lists
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

#Problem 2: Non-Repeating Elements => determine all elements in a given list that appear only once, meaning they don't have any duplicates in the same list
#Naive approache

list1 = [3,5,10,54,3,45,32,5,21,33,33]
start_time = time.time()
unique = []
duplicate = []
for num in range(len(list1)):
    for j in range(num+1,len(list1)):
        if list1[num] == list1[j]:
            duplicate.append(list1[num])
        elif j == len(list1) - 1 and list1[num]  not in duplicate:
                unique.append(list1[num])
                
print(sorted(unique))
print(f"it took {time.time() - start_time}'s") #output it took 1.621246337890625e-05's

#now using set

start_time = time.time()
seen, repeated = set(), set()
for num in list1:
    if num in seen:
        repeated.add(num)
    else:
        seen.add(num)
print(sorted(list(seen-repeated)))
print(f"it took {time.time() - start_time}'s") #it took 5.0067901611328125e-06's

#Problem 3: Unique Elements consist on finding elements that exist only in list1 and elements that exist only in list2, respectively.

list1 = [3,5,10,54,3,45,33,21,33,24]
list2 = [4,8,3,76,987,65,3,5]
duplicate = []
unique = []
#Naive approache
for num in range(len(list1)):
    if list1[num] not in list2:
        for j in range(num + 1,len(list1)):
            if list1[j] == list1[num]:
                duplicate.append(list1[num])
            elif j == len(list1) - 1 and list1[num] not in duplicate:
                unique.append(list1[num])
for num in range(len(list2)):
    if list2[num] not in list1:
        for j in range(num + 1,len(list2)):
            if list2[j] == list2[num]:
                duplicate.append(list2[num])
            elif j == len(list2) - 1 and list2[num] not in duplicate:
                unique.append(list2[num])
print(unique)

#using the set 

set1 = set(list1)
set2 = set(list2)
unique_to_1 = set1 - set2

unique_to_2 = set2 - set1
print(f"{sorted(list(unique_to_1)), sorted(list(unique_to_2))}")

#Problem 4: Unique String in the List consist on  identifying the first unique string from a list. 
#naive_approach
string_sentence = "i really hope that we will learn together,  sharing is caring that's our emblem, our motto. Hope this example is just right to show case the difrence"

biglist = string_sentence.split(". ")
sublist = [subl for sub in biglist for subl in sub.split(", ")]
words = [s.lower() for sen in sublist for s in sen.split(" ")]

duplicated = []

for index in range(len(words)):
    if words[index] in duplicated:
        continue
    else:
        for index_j in range(index + 1,len(words)):
            if words[index] == words[index_j]:
                duplicated.append(words[index])
            
for word in words:
    if word not in duplicated:
        print(word)
    break
#susing_set
seen, duplica = set(),set()

for word in words:
    if word in seen:
        duplica.add(word)
    seen.add(word)

for w in words:
    if w not in duplica:
        print(f"TADAAAA=>{w}")
        break