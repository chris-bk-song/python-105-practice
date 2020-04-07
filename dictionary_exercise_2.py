# The hotel has 5 rooms
# The names of the rooms are 101, 102, 103, 104, 105
# Store the occupant name for each of the rooms

# please use one dictionary to hold this information

# Make sure you can
# - put someone in a n unoccupied room
# - make a room available by setting the occupant name to ''
# - check if a room number is valid
# - check if a room is occupied or not

# For any one room, you should store:
# - occupant name
# - phone number
# - has prepaid

James = {
    'occupant_name': 'James',
    "phone_number": 1231231231,
    'has_prepaid': True
}

Jane = {
    'occupant_name': 'Jane',
    "phone_number": 1111111111,
    'has_prepaid': False
}

hotel = {
    '101': '',
    '102': '',
    '103': '',
    '104': '',
    '105': '',
}

hotel['101'] = James
hotel['104'] = Jane


for room_number in hotel.keys():
    if hotel[room_number] == '':
        print(f'{room_number} is vacant')
    else:
        print(f'{room_number} is occupied by {hotel[room_number]["occupant_name"]}')

print(hotel['101'])
print(hotel['102'])