# # ----------- for loop -----------
primes = [ 2, 3, 5, 7, 9 ]
for prime in primes:
    print prime

# ----------- for loop -----------
xnumbers = ['\n', 'yo', 'yo', 'this', 'is', 'a', 'python3', 'loop']
for x in xnumbers:
     print x
# this is going to throw an error for pyton 3 because xnumbers is not defined.

# ----------- while loop with "break" statement -----------
count = 0
print '\n'
while True:
    print count
    count += 1
    if count >= 5:
        break

# ----------- for loop with "continue" statement -----------
print '\n'
xrange = [1,2,3,4,5]
for x in xrange:
    # Check if x is even
    if x % 2 == 0:
        continue
        # "continue" is used to skip over the current iteration.
    print x
