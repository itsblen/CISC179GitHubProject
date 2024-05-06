from random import randint
import collections

# equip/weapon NPC price in mesos
weapon_npc = 450000

# equip/weapon cost in mesos
weapon_cost = 3500000

# cost of scrolls in mesos
scroll_cost = 5500000

# cost of prestigeous coin in mesos
coin_cost = 3050000

# number of trials/slots on weapons
trials = 7

# number of successes on weapon before stopping
target = 4

# when to stop on weapon (successes: slots) format
stop_at = {0: 6, 1: 3, 2: 1, 5: 2}

# number of runs
run_count = 1000000

# 4 pass cost in coins
four_cost = 60

# 5 pass cost in coins
five_cost = 300

# 6 pass cost in coins
six_cost = 1000

booms = 0 # the number of destroyed items that cannot be resold to recoup cost
total_cost = 0 # the total cost of production, in mesos
revenue = 0 # the recouped cost from selling byproduct
expected_cost = 0 # the total expected cost after revenue
successes = 0 # the total number of successful finished desired products
produced = {} # dictionary of everything that has been made

for x in range(run_count):
    scrolls_passed = 0 # tracker for current number of passed scrolls
    slots = trials # starting number of available slots
    total_cost += weapon_cost # add the cost of one additional weapon
    boomed = False # by default items exist and are not destroyed
    while slots > 0 and slots != stop_at.get(scrolls_passed, 0): # while there are available slots and a stop_at condition has not been reached, continue scrolling
        total_cost += scroll_cost # add the cost of one additional scroll
        number = randint(1, 100) # roll to see the scroll result
        if number <= 30: # pass condition
            scrolls_passed += 1 # increase the number of passed slots by 1
        elif number <= 65: # boom condition 
            boomed = True
            booms += 1 # increased the number of boomed byproducts by 1
            break # end loop since item is destroyed and cannot be scrolled anymore
        slots -= 1 # remove one slot (fail condition not needed since the only thing that happens on fail is -1 slot)
        
    if not boomed: # if the item survived
        with_slots = produced.get(scrolls_passed, {}) # set with_slots equal to the value of key scrolls_passed, otherwise empty dict
        with_slots[slots] = with_slots.get(slots, 0) + 1 # increase the number of the currently produced item by 1
        produced[scrolls_passed] = with_slots # update the dictionary produced with key scrolls_passed (current product) with with_slots 

ordered = collections.OrderedDict(sorted(produced.items(), reverse=True)) # sort produced in descending order by number of passed slots

print(f'items produced:')
for slots, passed_dict in ordered.items(): # nested for loop to iterate between products by passed scrolls and remaining slots
    for passed, count in collections.OrderedDict(sorted(passed_dict.items(), reverse=True)).items(): # second part of nested for loop
        print(f'number of scrolls passed: {slots}, slots remaining: {passed}, count: {count}') # print the total number of current iteration of product
        if slots < 4: # if the product is "garbage" (cannot be sold to other players for a reasonable price)
            revenue = revenue + ((count * weapon_npc) / coin_cost) # recoup value by selling the item to an NPC
        elif slots == 4: # if the product has 4 passed slots
            revenue = revenue + (count * four_cost) # recoup value by selling item to other players
        elif slots == 5: 
            if passed < 2: # if the product has 5 passed slots, but isn't the desired product
            	revenue = revenue + (count * five_cost) # recoup value by selling item to other players
            else: # if the product has 5 passed slots, and is the desired product
                successes = count # track the number of "finished" product
        elif slots == 6: # if the product has 6 passed slots
            revenue = revenue + (count * six_cost) # recoup value by selling item to other players
        
expected_cost = (total_cost / coin_cost) - revenue # calculate total expected cost
print(f'total_cost: {total_cost:.2f}, total_cost in coins: {total_cost / coin_cost:.2f}') # output total cost in coins and mesos
print(f'expected cost: {expected_cost/successes}') # output expected cost per item for finished completed product