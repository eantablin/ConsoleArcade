
""" Fundamental problems
If function gets called again it'll keep stacking numbers onto array
i.e: 0) 0) tomato, 1) 1) sausage; etc..

"""

inventory = ["tomato", "sausage", "apple"]

invHolder = []
x = 0
strHolder = ""

for i in inventory: # Make it easier for player to pick
    strHolder = f"{x}) {i}\n" # 0) Apples \n1) Tomatoes; etc..
    invHolder.append(strHolder)
    x += 1

inventory = invHolder

for i in inventory:
    print(i)