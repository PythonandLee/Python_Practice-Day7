# Move elements from one to another.
# Here create 2 'def' to make program easy to read.

def show_magicians(magicians, great_magicians):

    while magicians:
        current_magician = magicians.pop()
        print("Hello, magician " + current_magician.title() + ".")
        great_magicians.append(current_magician)

def make_great(great_magicians):

    for magician in great_magicians:
        print("\nHello, the Great " + magician.title() + "!")

magicians = ['david', 'jason', 'elvis', 'harry']
great_magicians = []

show_magicians(magicians, great_magicians)
make_great(great_magicians)