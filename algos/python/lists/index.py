aList = [];
aList.append('toby');
aList.append('tobiah');
aList.append('bickley');
# NOTE Cannot chain method calls in Python.
# Must call a new method on the returning result.

#print(aList.append['rex']);  # BUG TypeError: 'builtin_function_or_method' object is not subscriptable | IOW, cannot subscribe to the output of a method call.

bList = [
         'luke',
         'leia',
         'han',
         'chewie'
        ]
print(bList); # ['luke', 'leia', 'han', 'chewie']
