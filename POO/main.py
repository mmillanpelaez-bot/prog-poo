from POO.social.person import Person
from POO.time.hours import Hours
from POO.geometry.point import Point
from POO.geometry.sphere import Sphere
from POO.geometry.cylinder import Cylinder


def main_point():
    p1 = Point(2,3,0)
    p2 = Point(9,1,0)
    p2.x = 2
    p2.x = 3

    print (p1 == p2)

    p1 = p2
    p3 = p2

    p1.x = 999999999
    p3.x = 100
    print (p1.toString())
    print (p2)

    print (p1.x)

def main_person():
    manolo = Person ('Manolo', 69, '123456789Y', 'Calle Sinsalida', 'Musulman')
    manuela = Person ("Manuela", 96, "123456789Y", "Calle Consalida", "Manmusul")
    #manolo = Person (nome ='Manolo', age = 69, dni ='123456789Y', adress ='Calle Sinsalida', nacionality ='Musulman')

def main_geometry(): #Point, Shape3D, Cylinder, Sphere
    center = Point(1, 2, 3)

    sphere = Sphere(center, 4)
    cylinder = Cylinder(center, 3, 7)

    print(sphere)
    print()
    print(cylinder)

    # Export results to file
    with open("shapes_results.txt", "w") as f:
        f.write(str(sphere) + "\n\n" + str(cylinder))

def main_hours():
    ayer = Hours(12,4,-1)
    print (ayer)

if __name__ == "__main__":
    # main_hours()
    main_point()