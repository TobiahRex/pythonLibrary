obj = {
     'toby': 1,
     'tobiah': 2,
     'rex': 3,
     'trex': 4,
    }
# NOTE One cannot declare keys as implicit strings.  One must provide quotes around keys.

for name in obj:
    print(name, obj[name]);
    # toby 1
    # tobiah 2
    # rex 3
    # trex 4

# print(obj);
