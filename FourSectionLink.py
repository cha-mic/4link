import math 

class Point:
    def __init__(self, x=None, y=None) -> None:
        self.x = x
        self.y = y
    
class FourSectionLink:
    def __init__(self, p1=Point(0, 0), link1=None, link2=None, link3=None, \
                link4=None, angle0=None, angle1=None) -> None:
        
        self.link1 = link1
        self.link2 = link2
        self.link3 = link3
        self.link4 = link4
        self.angle0 = angle0
        self.angle1 = angle1
        self.angle2 = None
        self.angle3 = None
        self.angle4 = None
        self.angle5 = None
        self.p1 = Point(p1.x, p1.y)
        self.p2 = Point()
        self.p3 = Point()
        self.p4 = Point()

        print("link1-4 and angle0-5 and p1-4 initialized")
        
    def coordinate_of_points(self):
        
        print("--- calcurate angle and point ---")

        check_angle2 = 1
        check_angle3 = 1

        self.p2.x = self.p1.x + self.link1 * math.cos(self.angle0)
        self.p2.y = self.p1.y + self.link1 * math.sin(self.angle0)

        link5_2 = self.link1 ** 2 + self.link4 ** 2 - 2 * self.link1 * self.link4 * math.cos(self.angle1)

        angle2_cos = (self.link1**2 + link5_2 - self.link4**2) / (2 * self.link1 * math.sqrt(link5_2))
        angle3_cos = (self.link2**2 + link5_2 - self.link3**2) / (2 * self.link2 * math.sqrt(link5_2))

        if angle2_cos > 1.0:
            check_angle2 = 0
        if angle3_cos > 1.0:
            check_angle3 = 0

        if check_angle2 and check_angle3:
            self.angle2 = math.acos(angle2_cos)
            self.angle3 = math.acos(angle3_cos)
            print("Success!  angle2:{0:.3f}, angle3:{1:.3f}".format(math.degrees(self.angle2), math.degrees(self.angle3)))
        else:
            print("Error     angle2:{0},     angle3:{1}".format(check_angle2, check_angle3))

        
        self.p4.x = self.p1.x + self.link4 * math.cos(self.angle0 + self.angle1)
        self.p4.y = self.p1.y + self.link4 * math.sin(self.angle0 + self.angle1)

        try:
            self.p3.x = self.p2.x + self.link2 * math.cos(self.angle0 + (math.pi - self.angle2 - self.angle3))
            self.p3.y = self.p2.y + self.link2 * math.sin(self.angle0 + (math.pi - self.angle2 - self.angle3))
        except:
            print("error:p3")

        return self.p1, self.p2, self.p3, self.p4
    
    def calculate_angle(self, angle1=None):
    
        if angle1 == None:
            angle1 = self.angle1

        print("--- calcurate angles ---")

        check_angle2 = 1
        check_angle3 = 1
        check_angle4 = 1        

        link5_2 = self.link1 ** 2 + self.link4 ** 2 - 2 * self.link1 * self.link4 * math.cos(angle1)

        angle2_cos = (self.link1**2 + link5_2 - self.link4**2) / (2 * self.link1 * math.sqrt(link5_2))
        angle3_cos = (self.link2**2 + link5_2 - self.link3**2) / (2 * self.link2 * math.sqrt(link5_2))
        angle4_cos = (self.link2**2 + self.link3**2 - link5_2) / (2 * self.link2 * self.link3)

        if angle2_cos > 1.0:
            check_angle2 = 0
        if angle3_cos > 1.0:
            check_angle3 = 0
        if angle4_cos > 1.0:
            check_angle3 = 0

        if (check_angle2 and check_angle3) and check_angle4:

            self.angle2 = math.acos(angle2_cos)
            self.angle3 = math.acos(angle3_cos)
            self.angle4 = math.acos(angle4_cos)
            self.angle5 = (math.pi - angle1 - self.angle2) + (math.pi - self.angle3 - self.angle4)
            print("Success!  angle2:{0:.3f}, angle3:{1:.3f}, angle4:{2:.3f}, angle5:{3:3f}"\
                  .format(math.degrees(self.angle2), math.degrees(self.angle3), math.degrees(self.angle4), math.degrees(self.angle5)))
            
            return self.angle1, self.angle2, self.angle3, self.angle4
        
        else:
            print("Error     angle2:{0},     angle3:{1},     angle4:{2}".format(check_angle2, check_angle3, check_angle4))

            return None, None, None, None

    def calculate_points(self, p1=None, angle0=None, angle1=None, angle2=None):

        if p1 == None:
            p1 = self.p1
        if angle0 == None:
            angle0 = self.angle0
        if angle1 == None:
            angle1 = self.angle1
        if angle2 == None:
            angle2 = self.angle2

        print("--- calcurate points ---")

        self.p2.x = p1.x + self.link1 * math.cos(angle0)
        self.p2.y = p1.y + self.link1 * math.sin(angle0)

        self.p4.x = p1.x + self.link4 * math.cos(angle0 + angle1)
        self.p4.y = p1.y + self.link4 * math.sin(angle0 + angle1)

        self.p3.x = self.p2.x + self.link2 * math.cos(angle0 + (math.pi - self.angle2 - self.angle3))
        self.p3.y = self.p2.y + self.link2 * math.sin(angle0 + (math.pi - self.angle2 - self.angle3))

        print("p1[{0:.3f}, {1:.3f}], p2[{2:.3f}, {3:.3f}], p3[{4:.3f}, {5:.3f}], p4[{6:.3f}, {7:.3f}]".format(p1.x, p1.y, self.p2.x, self.p2.y, self.p3.x, self.p3.y, self.p4.x, self.p4.y))

        return p1, self.p2, self.p3, self.p4

    def check_angles(self):

        print("--- check angle ---")

        link5_2 = self.link1 ** 2 + self.link4 ** 2 - 2 * self.link1 * self.link4 * math.cos(self.angle1)
        try:
            self.angle2 = math.acos((self.link1**2 + link5_2 - self.link4**2) / (2 * self.link1 * math.sqrt(link5_2)))
            self.angle3 = math.acos((self.link2**2 + link5_2 - self.link3**2) / (2 * self.link2 * math.sqrt(link5_2)))
            print("angle1,2,3:",math.degrees(self.angle1), math.degrees(self.angle2), math.degrees(self.angle3))
        except:
            print("error: angle2 or 3")
            return 0

        try:
            self.angle4 = math.acos((self.link2**2 + self.link3**2 - link5_2) / (2 * self.link2 * self.link3))
            self.angle5 = (math.pi - self.angle1 - self.angle2) + (math.pi - self.angle3 - self.angle4)
            print("angle4,5:",math.degrees(self.angle4), math.degrees(self.angle5))
        except:
            print("error: angle4")
            return 0

        if self.angle2 + self.angle3 >= math.pi:
            print("angle2 + angle3 >= pi")
            return 0
        
        if self.angle5 >= math.pi:
            print("angle5 >= pi")
            return 0
        
        return 1

    def points_to_array(self, p1=None, p2=None, p3=None, p4=None):

        if p1 == None:
            p1 = self.p1
        if p2 == None:
            p2 = self.p2        
        if p3 == None:
            p3 = self.p3
        if p4 == None:
            p4 = self.p4

        x_array = [p1.x, p2.x, p3.x, p4.x, p1.x]
        y_array = [p1.y, p2.y, p3.y, p4.y, p1.y]

        return x_array, y_array