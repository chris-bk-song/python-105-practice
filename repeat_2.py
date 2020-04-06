# Repeat exercise #2
# Change my function so that it returns instead of print()-ing
# a_dog_says = repeat(3, repeat(5, 'woof'))
# woofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoofwoof

def repeat_2 (how_many_times, the_string):
    return how_many_times * the_string

a_dog_says = repeat_2(3, repeat_2(5, 'woof'))
print(a_dog_says)

