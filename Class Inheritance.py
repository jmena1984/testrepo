class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [] # intialized to zero
        for i in range(no_of_sides):
            self.sides.append(0)
            
    def input_sides(self):
        for i in range(self.n):
                self.sides[i] = float(input('Enter side'+str(i+1)+' : ')) # updates the list one index at a time.
            
    def display_sides(self):
        for i in range(self.n):
            print('Sides', i+1, 'is', self.sides[i]) # prints value by index.
            
p1 = Polygon(3)
p1.input_sides()
print(p1.n)
print(p1.sides)
p1.display_sides()         


# Example: Inheritance

# We are INHERITING the triangle class from the polygon class, in order to find the area of a triangle.

class Triangle(Polygon):
    def __intit__(self):
        Polygon.__init__(self,3) # call the polygon class. This will create the sides list and initialize all its items(side) of the list to 0.
    
    def find_area(self):
        a, b, c = self.sides # names are assigned to corresponding items in list. ex. a, b, c = [1, 2, 3]...a = 1, b = 2, c = 3.  
        #calculate the semi perimeter
        s = (a+b+c)/2
        area = (s*(s-a) * (s-b) * (s-c)) **0.5
        print('The area of the triangle is', area)
        
t = Triangle(3)
t.input_sides()
t.find_area()





