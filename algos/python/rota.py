def rota(rooms):
    while (len(rooms) < 7):
        rooms += rooms
    return rooms

print(rota(['one', 'two', 'three']))
