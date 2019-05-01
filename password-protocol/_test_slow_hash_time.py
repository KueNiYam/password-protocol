import time
import hashlib

value = b'abcde12345'
count = 1000000

start = time.time()

while count > 0 :
    value = hashlib.sha256(value).digest()
    count -= 1

end = time.time()
print('걸린시간', end-start)
