def exp1():
    obj = {
            'name': 'Toby',
            'age': 28
        }

    def x():
      return (obj, { 'name': 'Tobiah', 'age': 29 })

    obj2, obj3 = x()
    print('obj2: %s \nobj3: %s' % (obj2, obj3))

def exp2():
    list1 = []

    def addTo(x):
        print('adding...')
        list1.append(x)

    def remove(y):
        print('removing...')
        list1.pop()

    def run(a, z):
        switcher = {
            'f1': addTo,
            'f2': remove,
            'f3': lambda: 'default',
        }

        func = switcher.get(a, lambda: 'nothing'); # NOTE what does Lambda mean?
        func(z);

    run('f1', { 'name': 'Toby' });
    print(list1)

exp2()
