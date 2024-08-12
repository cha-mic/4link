import numpy as np
import matplotlib.pyplot as plt
import math 

from FourSectionLink import Point
from FourSectionLink import FourSectionLink

# length of link1-4
link1_1 = 80
link2_1 = 40
link3_1 = 80
link4_1 = 70

# points
p1 = Point(0, 0)

# ---------- main ----------- #

fig = plt.figure(figsize=(7, 7))
angle_array = np.arange(30, 135, 5)

mech1 = FourSectionLink(p1, link1_1, link2_1, link3_1, link4_1, 0.0, math.radians(angle_array[0]))

for angle in angle_array:
    mech1.angles["angle1"] = math.radians(angle) 

    mech1.calculate_angle()
    if (None in  mech1.angles.values()) == False:
        mech1.calculate_points()
        x_array_1, y_array_1 = mech1.points_to_array()
        plt.plot(x_array_1, y_array_1)

plt.xlim((-50, 150))
plt.ylim((-50, 150))
plt.show()







