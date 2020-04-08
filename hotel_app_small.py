# Dictionary that can be used to manage the occupants of a hotel
# Small: Single Hotel
# Goal here is to get practice with the syntax for 
# querying and manipulating the data in a single, nested dictionary.

hotel = {
    '101': {
        'guest': {
            'name': 'Elliot Anderson',
            'phone': '222-222-2222'
        }
    },
    '102': {},
    '103': {},
    '104':{
        'guest': {
            'name': 'Darlene Alderson',
            'phone': '111-111-1111'
        }
    },
    '105': {},
}

main_menu = '''

1. Print hotel room status
2. Check in customer
3. Check out customer
4. Quit

'''

while True:
    menu_choice = int(input(main_menu))

    room_number = hotel.keys()
    
    if menu_choice == 1:
        def is_vacant(room_number):
            for room_number in hotel.keys():
                if hotel[room_number] == {}:
                    print(f'Room {room_number} is vacant.')
                else:
                    print(f'Room {room_number} is occupied by {hotel[room_number]}.')

        print(f'{is_vacant(room_number)}\n')
        
    elif menu_choice == 2:

        def check_in(room_number):
            for room_number in hotel.keys():
                if hotel[room_number] == {}:
                    print(f'Room {room_number} is available.')
                    yes_or_no = input('Do you want to take this room? [Y/N]\n')
                    yes_or_no = yes_or_no.upper()
                    if yes_or_no == 'Y':
                        new_name = input('What is the name?\n')
                        new_phone = input('What the phone number?\n')
                        hotel[room_number]['guest'] = {'name': new_name, 'phone': new_phone}
                    elif yes_or_no == 'N':
                        print('[This room is unoccupied.]\n')
                    else:
                        print('[Please type either Y or N.]')
                else:
                    print(f'Room {room_number} is already occupied.')

        print(f'{check_in(room_number)}\n')

    elif menu_choice == 3:

        def check_out(room_number):
            for room_number in hotel.keys():
                if hotel[room_number] != {}:
                    remove = input(f'Do you want check out of room {room_number}? [Y/N]\n')
                    remove = remove.upper()
                    if remove == 'Y':
                        hotel[room_number] = {}
                        print(f'[Room {room_number} has been checked out.]\n')
                    elif remove == 'N':
                        print('[Enjoy your stay.]\n')

        print(f'{check_out(room_number)}\n')

    elif menu_choice == 4:
        break
        
print('Thank you for using the hotel app!')