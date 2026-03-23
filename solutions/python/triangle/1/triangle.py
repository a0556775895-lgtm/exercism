def equilateral(sides):
    if(sides[0]<=0 or sides[1]<=0 or sides[2]<=0):
        return False;
    
    return sides[0]==sides[1]==sides[2] and is_triangle(sides)
    


def isosceles(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    return (sides[0] == sides[1] or 
            sides[0] == sides[2] or 
            sides[1] == sides[2]) and is_triangle(sides)


def scalene(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    return (sides[0] != sides[1] and 
            sides[0] != sides[2] and 
            sides[1] != sides[2]) and is_triangle(sides)



def is_triangle(sides):
    return (sides[0] + sides[1] > sides[2] and
            sides[0] + sides[2] > sides[1] and
            sides[1] + sides[2] > sides[0])