import numpy as np
import matplotlib.pyplot as plt
import math 

from FourSectionLink import Point
from FourSectionLink import FourSectionLink

# length of link1-4
link1_1 = 80
link2_1 = 30
link3_1 = 80
link4_1 = 40

link1_2 = 40
link2_2 = 80
link3_2 = 20
link4_2 = 80

# points
p1 = Point(0, 0)

# ---------- main ----------- #

angle_array = np.arange(45, 135, 5)

mech1 = FourSectionLink(p1, link1_1, link2_1, link3_1, link4_1, 0.0, math.radians(angle_array[0]))
# mech1.calculate_angle()
# mech1.calculate_points()

i = 1
while (None in mech1.angles.values()) == True:
    mech1.angles["angle1"] = math.radians(angle_array[i]) 
    mech1.calculate_angle()
    i += 1

mech1.calculate_points()
mech2 = FourSectionLink(mech1.p3, link1_2, link2_2, link3_2, link4_2, math.atan2(mech1.p4.y - mech1.p3.y, mech1.p4.x - mech1.p3.x), mech1.angles["angle4"])

for angle in angle_array:
    mech1.angles["angle1"] = math.radians(angle) 

    mech1.calculate_angle()
    if (None in mech1.angles.values()) == False:
        mech1.calculate_points()
        x_array_1, y_array_1 = mech1.points_to_array()
        # plt.plot(x_array_1, y_array_1)

        mech2.p1 = mech1.p3
        mech2.angles["angle1"] = mech1.angles["angle4"]
        mech2.angles["angle0"] = math.atan2(mech1.p4.y-mech1.p3.y, mech1.p4.x-mech1.p3.x)

        mech2.calculate_angle()
        if (None in mech2.angles.values()) == False:
            mech2.calculate_points()
            x_array_2, y_array_2 = mech2.points_to_array()
            plt.plot(x_array_1, y_array_1)
            plt.plot(x_array_2, y_array_2)

plt.show()







