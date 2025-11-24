import os
print('cwd:', os.getcwd())
print('X.txt exists:', os.path.exists('X.txt'))
print('y.txt exists:', os.path.exists('y.txt'))
if os.path.exists('X.txt'):
    with open('X.txt') as f:
        print('X.txt sample:', f.read().strip().split('\n')[:5])
if os.path.exists('y.txt'):
    with open('y.txt') as f:
        print('y.txt sample:', f.read().strip().split('\n')[:5])
