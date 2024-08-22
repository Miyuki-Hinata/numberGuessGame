import sys
sys.stdout.buffer.write(b'Hello Jupiter!\n')
sys.stdout.flush()
food = sys.stdin.buffer.readline()
print('Thank you' + food.decode())