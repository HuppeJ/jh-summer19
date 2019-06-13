class Starship(object):
    # Class variable (Like static variables)
    sound = "Vrrrrrrrrrrrrrrrrrrrrr"
    
    # Every Python class needs to have one, and only one, __init__(self) function. This is called the initializer.
    # If no need of __init__ add the function and write pass under it
    def __init__(self):
        # Instance variable declare all of them in the __init__ function
        self.engines = False
        self.engine_speed = 0
        self.shields = True

    def engage(self):
        self.engines = True

    def warp(self, factor):
        self.engine_speed = 2
        self.engine_speed *= factor

    # A class method never touches member variables or regular methods. 
    # (Like Static methods but a static method also doesn't access any of the class members; 
    # sit doesn't even care that it's part of the class!)
    # So, to make it extra-super-clear we can't do that in a class method, we call the first argument cls
    @classmethod
    def make_sound(cls):
        print(cls.sound)