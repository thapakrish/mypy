# @ Krishna
# Modified example used at Coursera course 'Crafting Quality Code' from UofToronto
# A simple example of a python class

class FruitsCalorie:
    """A calorie counter in fruits"""

    def __init__(self, apple, banana, orange, pomegranate, peach):
        """ (FruitsCalorie, int, int, int, int, int) -> NoneType

        A FruitsCalorie with apple, banana, orange, pomegranate, and peach.
        """
        
        self.apple = apple
        self.banana = banana
        self.orange = orange
        self.pomegranate = pomegranate
        self.peach = peach
        
    def __str__(self):
        """ (FruitsCalorie) -> str
        
        Return a string representation of this FruitsCalorie.
        
        >>> eg1 = FruitsCalorie(1, 2, 3, 4, 5)
        >>> eg1.__str__()
        'FruitsCalorie: $1807 ($72x1, $118x2, $131x3, $154x4, $98x5)'
        """

        return 'FruitsCalorie: ' + \
               '${0} ($72x{1}, $118x{2}, $131x{3}, $154x{4}, $98x{5})'.format(
                   self.get_total(), self.apple, self.banana,
                   self.orange, self.pomegranate, self.peach)
                   
                   
    def __eq__(self, other):
        """ (FruitsCalorie, FruitsCalorie) -> bool

        Return True iff this FruitsCalorie has the same amount of calorie as other.
        
        >>> ex1 = FruitsCalorie(2, 0, 0, 0, 0)
        >>> ex2 = FruitsCalorie(0, 1, 0, 0, 0)
        >>> ex1 == ex2
        False
        """

        return self.get_total() == other.get_total()
            

    def get_total(self):
        """ (FruitsCalorie) -> int

        Return the total amount of calories in fruits.
        """

        return self.apple*72 + self.banana * 118 + self.orange * 131 + \
               self.pomegranate * 154 + self.peach * 98
    
    def add(self, count, fruit):
        """ (FruitsCalorie, int, str) -> NoneType

        Add count items of fruit to the list.
        Fruit is one of 'apple', 'banana',
        'orange', 'pomegranate', and 'peach'.
        """
        self.fruit += count

    def remove(self, count, fruit):
        """ (FruitsCalorie, int, str) -> NoneType

        Remove count items of fruit from the list.
        Fruit is one of 'apple', 'banana',
        'orange', 'pomegranate', and 'peach'.
        """
        self.fruit -= count

if __name__ == '__main__':

    ex1 = FruitsCalorie(2, 0, 0, 0, 0)
    ex2 = FruitsCalorie(0, 1, 0, 0, 0)
    ex3 = FruitsCalorie(2, 0, 0, 0, 0)
    
# Prints from the __str__ portion of code
    print(ex1)
    print(ex2)
    print(ex3)
    
# Checks if they are equal    
    print(ex1 == ex2)
    print(ex1 == ex3)
    
# If I didn't have the __eq__ method in FruitsCalorie class, == would've compared 
# memory address instead of total calories.
    
