def rota(inputRooms):
    while (len(inputRooms) < 7):
        inputRooms += inputRooms

    rooms = inputRooms[:7]
    return rooms


print(rota(['one', 'two', 'three'])) #['one', 'two', 'three', 'one', 'two', 'three', 'one']
