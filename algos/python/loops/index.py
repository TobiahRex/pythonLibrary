from urllib.request import urlopen;
with urlopen('http://sixty-north.com/c/t.txt') as story:
    story_words = [];
    for line in story:
        line_words = line.decode().split();
        for word in line_words:
            story_words.append(word);

    print(story_words);

obj = {
     'toby': 1,
     'tobiah': 2,
     'rex': 3,
     'trex': 4,
    }
# NOTE One cannot declare keys as implicit strings.  One must provide quotes around keys.

# for name in obj:
    # print(name, obj[name]);

# print(obj);
