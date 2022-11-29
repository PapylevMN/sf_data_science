''' Игра угадай число'''
import numpy as np

num = np.random.randint(1,101)

count = 0

while True:
    count += 1
    pred_num = int(input('Угадай число от 1 до 100'))    
    
    if pred_num > num:
        print('Number must be lower')
    
    elif pred_num < num:
        print('Number must be higher')
    else:
        print(f'You have found a number {num} for {count} attempts')
        break
    
    

