# Dictionary that can be used to manage the occupants of a hotel
# Small: Single Hotel
# Goal here is to get practice with the syntax for 
# querying and manipulating the data in a single, nested dictionary.

hotel = {
    '101': {
        'guest': {
            'name': 'Elliot Anderson',
            'phone': 8675309
        }
    },
    '102': {},
    '103': {},
    '104':{
        'guest': {
            'name': 'Darlene Alderson',
            'phone': 4567890
        }
    },
    '105': {},
}

# Write functions to:
# is_vacant(which_hotel, '101')
# -check if a room is occupied

room_number = hotel.keys()

def is_vacant(room_number):
    for room_number in hotel.keys():
        if hotel[room_number] == {}:
            print(f'Room {room_number} is vacant.\n')
        else:
            print(f'Room {room_number} is occupied by {hotel[room_number]}.\n')

print('\n[The current list of the occupied and vacant rooms is shown below]\n')
print(f'{is_vacant(room_number)}\n')

# check_in('101', guest_dictionary)
# -assign a person to a room

assign_room = hotel.keys()

def check_in(assign_room):
    for assign_room in hotel.keys():
        if hotel[assign_room] == {}:
            print(f'Room {assign_room} is available.\n')
            yes_or_no = input('Do you want to take this room? [Y/N]\n')
            if yes_or_no == 'Y':
                new_name = input('What is the name?\n')
                new_phone = input('What the phone number?\n')
                hotel[assign_room]['guest'] = {'name': new_name, 'phone': new_phone}
            elif yes_or_no == 'N':
                print('[This room is unoccupied.]\n')
            else:
                print('[Please type either Y or N.]\n')
        else:
            print(f'Room {assign_room} is already occupied.\n')

print(f'{check_in(assign_room)}\n')
print('[The updated list of occupied and vacant rooms is shown below after check-in]\n')
print(f'{is_vacant(room_number)}\n')




# check_out('101')
# -return the person dictionary in that room 

empty_room = hotel.keys()

def check_out(empty_room):
    for empty_room in hotel.keys():
        if hotel[empty_room] != {}:
            remove = input(f'Do you want check out of room {empty_room}? [Y/N]\n')
            if remove == 'Y':
                hotel[empty_room] = {}
                print(f'[Room {empty_room} has been checked out.]\n')
            elif remove == 'N':
                print('[Enjoy your stay.]\n')

print(f'{check_out(empty_room)}\n')
print('[The updated list of occupied and vacant rooms is shown below after check-out]\n')
print(f'{is_vacant(room_number)}\n')
