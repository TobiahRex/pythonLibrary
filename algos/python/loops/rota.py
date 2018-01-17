def rota(inputRooms):
    while (len(inputRooms) < 7):
        inputRooms += inputRooms

    rooms = inputRooms[:7]
    

print(rota(['one', 'two', 'three']))
