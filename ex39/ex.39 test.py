# -*- coding: utf-8 -*- #한글패치
# -*- coding: cp949 -*-
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California': 'CA',
    'NeW York' : 'NY',
    'Hawaii' : 'HI',
}

cities = {
    'CA' : 'Los Angeles',
    'Hi' : 'Honolulu',
    'FL' : 'Jacksonville'
}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

print('-' * 10)
print("Hawaii`s abbervialation is : %s" % states['Hawaii'])
print("Florida`s abbervialation is : %s" %states['Florida'])

print('-' * 10)
print("states = %s" % states)
print("state.item() = %s")


print ('-' * 10)
for state, abbrev in states.items():
    print ("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print ('-' * 10)
for abbrev, city in cities.items():
    print ("%s has the city %s" % (abbrev, city))

# now do both at the same time
print ('-' * 10)
for state, abbrev in states.items():
    print ("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]))

print ('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print ("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print ("The city for the state 'TX' is: %s" % city)