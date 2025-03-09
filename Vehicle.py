def test_drive(vehicle):
    vehicle.Move()

def repair(vehicle):
    print(f'The {vehicle} is being repaired.\n'
          'Or is it? *VSauce music plays*')

def fuel_up(vehicle):
    print(f'The {vehicle} is being fueled up.\n'
          f'Or is it? *Vsauce music plays*')

def park(vehicle):
    print(f"Somebody's {vehicle} is being parked up in joshuas big brain")


class Vehicle:
    def Move(self):
        print('Moves forawrd with 4 wheels.')

    def __str__(self):
        return f'{self.__class__.__name__}'




class Bicycle(Vehicle):
    def Move(self):
        print('Moves forward using two wheels. *ring ring*')

    def __str__(self):
        return f'{self.__class__.__name__}'



class AirPlane(Vehicle):
    def Move(self):
        print('*wheeeeeeehhhhaoooooowww*')

    def __str__(self):
        return f'{self.__class__.__name__}'



class AndreCar(Vehicle):
    def Move(self):
        print('The wheels on the car go round and round!')

    def __str__(self):
        return f'{self.__class__.__name__}'



class DanielCar(Vehicle):
    def Move(self):
        from tkinter import messagebox
        print('Car starts moving...')
        messagebox.showerror(title='', message='Daniel Car felt lazy and combusted.\n"Goodye cruel world"')

    def __str__(self):
        return f'{self.__class__.__name__}'



class SnailSled:
    def Move(self):
        print("I make it smooth and slimy for all the lovely snail ladies.")

    def __str__(self):
        return f'{self.__class__.__name__}'



class JoshuaCar:
    def Move(self):
        import webbrowser
        print('Starts moving like a smart smart car!1!!111')
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')

    def __str__(self):
        return f'{self.__class__.__name__}'



class Boat:
    def Move(self):
        print( "The boat sails across the water.")

    def __str__(self):
        return f'{self.__class__.__name__}'



class Helicopter:
    def Move(self):
        print('The helicopter hovers above the ground')

    def __str__(self):
        return f'{self.__class__.__name__}'



class Train:
    def Move(self):
        print('The train runs on tracks. Until it doesnt.')

    def __str__(self):
        return f'{self.__class__.__name__}'



class Tractor:
    def Move(self):
        print('Big wheels. The tractor plows through the field.')

    def __str__(self):
        return f'{self.__class__.__name__}'



class MotorCycle:
    def Move(self):
        print('The motorcycle zooms down the highway.')

    def __str__(self):
        return f'{self.__class__.__name__}'



class Rocket:
    def Move(self):
        print('The rocket blasts off into space.')

    def __str__(self):
        return f'{self.__class__.__name__}'



class UFO:
    def Move(self):
        print('The UFO glides silently through the air.')

    def __str__(self):
        return f'{self.__class__.__name__}'


class SurfBoard:
    def Move(self):
        print('The surfboard rides the ocean waves. Until a shark finds the rider and turns him into a nugget.')

    def __str__(self):
        return f'{self.__class__.__name__}'


class Duck:
    def Move(self):
        print('Quack Quack Quack')

    def __str__(self):
        return f'{self.__class__.__name__}'


class AlbertCar:
    def Move(self):
        print('Quack Quack Quack')

    def __str__(self):
        return f'{self.__class__.__name__}'

name, cls = None, None
for name, cls in globals().items(): # similar to __dict__ but no
    if isinstance(cls, type) and hasattr(cls, 'Move'):
        # cheks if class
        # cheks for move method
        print(f'Yay im so happy. This is a seperator. {"-" * 50}')
        test_drive(cls())
        repair(cls())
        fuel_up(cls())
        park(cls())
