# day = int(input('Day (0-6)? '))
# if day == 0:
#     print('Sunday')
# elif day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# elif day == 6:
#     print('Saturday')
# else:
#     print('Please type numbers between 0 - 6')

# Below is another way to find out if you need to sleep or go to work by using functions
def sleep_or_work(day): # Make sure it's a number between 0 and 6
    if day < 7 and day >= 0:
        if day == 0 or day == 6:
            return 'Sleep in'
        else:
            return 'Go to work!'

while True:
    day = int(input('Day (0-6)? '))
    message = sleep_or_work(day)
    print(message)

