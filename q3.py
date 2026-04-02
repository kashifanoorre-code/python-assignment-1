def circle_area(radius):
    print("area of circle is: ",round(3.14*radius*radius,2))
def rectangle_area(length,breadth):
    print("area of rectangle is:",round(length*breadth,2))
def triangle_area(base,height):
    print("area of triangle is: ",round(0.5*base*height,2))
def square_area(side):
    print("area of square is: ",round(side*side,2))
def paralellogram_area(base,height):
    print("area of triangle is: ",round(base*height,2))
def volume_cube(side):
    print("volume of cube is: ",round(side*side*side,2))
def volume_cuboid(length,breadth,height):
    print("volume of cuboid is: ",round(length*breadth*height,2))
def volume_sphere(radius):
    print("volume of sphere is: ",round((4/3)*3.14*radius*radius*radius,2))
def volume_cylinder(radius,height):
    print("volume of cylinder is: ",round(3.14*radius*height,2))
def volume_cone(radius,height):
    print("volume of cone is: ",round((1/3)*3.14*radius*radius*height,2))


x=int(input("enter 1 for area of circle, 2 for rectangle,3 for triangle,4 for square, 5 for parallelogram, 6 for volume of cube, 7 for cuboid,8 for sphere,9 for cylinder, 10 for cone: "))
match x:
    case 1:
        radius=int(input("enter radius: "))
        circle_area(radius)
    case 2:
        length=int(input("enter length: "))
        breadth=int(input("enter breadth: "))
        rectangle_area(length,breadth)
    case 3:
        base=int(input("enter base: "))
        height=int(input("enter height: "))
        triangle_area(base,height)
    case 4:
        side=int(input("enter side: "))
        square_area(side)
    case 5:
        height=int(input("enter height: "))
        base=int(input("enter base: "))
        paralellogram_area(base,height)
    case 6:
        side=int(input("enter side: "))
        volume_cube(side)
    case 7:
        length=int(input("enter length: "))
        breadth=int(input("enter breadth: "))
        height=int(input("enter height: "))
        volume_cuboid(length,breadth,height)
    case 8:
        radius=int(input("enter radius: "))
        volume_sphere(radius)
    case 9:
        radius=int(input("enter radius: "))
        height=int(input("enter height: "))
        volume_cylinder(radius,height)
    case 10:
        radius=int(input("enter radius: "))
        height=int(input("enter height: "))
        volume_cone(radius,height)