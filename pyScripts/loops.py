# # ----------- for loop -----------
primes = [ 2, 3, 5, 7, 9 ]
for prime in primes:
    print prime

# ----------- for loop -----------
xnumbers = ['\n', 'yo', 'yo', 'this', 'is', 'a', 'python3', 'loop']
for x in xnumbers:
     print x
# this is going to throw an error for pyton 3 because xnumbers is not defined.

# ----------- while loop -----------
count = 0
print '\n'
while True:
    print count
    count += 1
    if count >= 5:
        break
