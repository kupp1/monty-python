"""
Monty Hall simulation with diagrams
Author: kupp1
"""


from matplotlib import pyplot as plt
from randompy.randompy.randompy import RandomPy
import sys

try:
    doors_number = int(input('Enter number of doors (>= 3): '))
    attempts_number = int(input('Enter the number of attempts: '))

    if doors_number < 3:
        sys.exit('Number of doors must be 3 or more!')
    if attempts_number < 1:
        sys.exit('Number of attempts must be 1 or more!')
except ValueError:
    sys.exit('ValueError! Input must be integers!')

randSigned = RandomPy()

first_choce_win_count = 0
second_choice_win_count = 0
first_choce_win = []
second_choice_win = []
first_choce_win_odds = []
second_choice_win_odds = []

car_doors = randSigned.integers(min=1, max=doors_number, n=attempts_number)['random']['data']
guest_doors = randSigned.integers(min=1, max=doors_number, n=attempts_number)['random']['data']

for i in range(1, attempts_number+1):
    car_door = car_doors[i-1]
    guest_door = guest_doors[i-1]
    if car_door == guest_door:
        first_choce_win_count += 1
    else:
        second_choice_win_count += 1

    first_choce_win_odds.append(first_choce_win_count / i)
    second_choice_win_odds.append(second_choice_win_count / i)

    first_choce_win.append(first_choce_win_count)
    second_choice_win.append(second_choice_win_count)
first_choce_win_percent = (first_choce_win_count * 100)/attempts_number
second_choice_win_percent = (second_choice_win_count * 100)/attempts_number
print('first_choce_win_percent: %s%s' % (str(first_choce_win_percent), '%'))
print('second_choice_win_percent: %s%s' % (str(second_choice_win_percent), '%'))

plt.plot(first_choce_win, 'r')
plt.plot(second_choice_win, 'b', alpha=0.7)
plt.title('Monti Hall Simulation, %s doors' % doors_number)
plt.xlabel('attempts')
plt.ylabel('wins')
plt.legend(['first choice', 'second choice'])
plt.show()

plt.plot(first_choce_win_odds, 'r')
plt.plot(second_choice_win_odds, 'b')
plt.title('Monti Hall Simulation, %s doors' % doors_number)
plt.xlabel('attempts')
plt.ylabel('win odds')
plt.legend(['first choice', 'second choice'])
plt.show()
