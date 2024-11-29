import random

def game():
    reward=0
    while(True):
        num =random.random()
        if(num> 1/3):
            reward=reward+4
        else:
            reward= reward+4
            break

    return reward

reward=0
for i in range(1000):
    reward=reward+game()

print(reward/1000)
