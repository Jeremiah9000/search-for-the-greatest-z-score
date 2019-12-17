import numpy as np
import time

start = time.time()
seconds = 10
update = False

print('running...')
try:
    with open('greatest_z.txt') as f:
        y = float(f.read())
except FileNotFoundError:
    y = 0.0

coutner = 0
while True:
    coutner += 1
    x = np.random.randn()
    if abs(x) > abs(y):
        update = True
        print(f'greater z-score found! {x}')
        y = x
    if time.time() >= (start + seconds):
        end = time.time()
        print(f'{coutner} cycles')
        if update:
            print(f'greatest z-score found in {int(end - start)} seconds is z of {y}')
            with open('greatest_z.txt', 'w+') as f:
                f.write(str(y))
        else:
            print(f'no z-score found in {int(end - start)} seconds that is greater than the previous z of {y}')
        break
