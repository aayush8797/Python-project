word_list = ["keyboard", "monitor", "mouse"]

import random
a=random.choice(word_list)

b=input("Guess a letter:").lower()

for num in a:
    if num == b:
        print('right')
    else:
        print("wrong") 