import random

subjects = [
    'virat kholhi',
    'nilmla sita raman',
    'salman khan',
    'shahrukh khan',
    'a mumbai cat',
    'rudra',
    'a group of monkey',

]

actions = [
'launch',
'cancels',
'dances with',
'eats',
'orders',
'celebrates',
]

places = [
'at red fort',
'mumbai local train',
'plate of samosa',
'inside parliament',
'at ganga ghat',
'bhopal juction',
'suring IPL match',
'at india gate',
]


while True:
    subject  = random.choice(subjects)
    action   = random.choice(actions)
    place    = random.choice(places)

    headline = f" BREKING NEWS: {subject}{action}{place}"
    
    print("\n" + headline)

    user_input = input("n\ do oyu want  another headline (yes/no)").strip()
    if user_input == "no":
        break

    print("\n thanks for using the fake news headline generate have a fun day ")
