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

compare_set_to_list()