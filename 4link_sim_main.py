import numpy as np
import matplotlib.pyplot as plt
import math 

from four_link_sim import Point
from four_link_sim import Four_link

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

mech1 = Four_link(p1, link1_1, link2_1, link3_1, link4_1, 0.0, math.radians(angle_array[0]))
mech1.coordinate_of_points()
mech1.check_angles()

mech2 = Four_link(mech1.p3, link1_2, link2_2, link3_2, link4_2, math.atan2(mech1.p4.y-mech1.p3.y, mech1.p4.x-mech1.p3.x), mech1.angle4)
mech2.coordinate_of_points()
mech2.check_angles()

for i in angle_array:
    mech1.angle1 = math.radians(i)   
    mech1.coordinate_of_points()
    mech1.check_angles()
    x_array_1, y_array_1 = mech1.points_to_array()
    plt.plot(x_array_1, y_array_1)

    mech2.p1 = mech1.p3
    mech2.angle1 = mech1.angle4
    mech2.angle0 = math.atan2(mech1.p4.y-mech1.p3.y, mech1.p4.x-mech1.p3.x)

    mech2.coordinate_of_points()
    x_array_2, y_array_2 = mech2.points_to_array()
    plt.plot(x_array_2, y_array_2)

# plt.xlim((-200, 200))
# plt.ylim((-200, 200))
# plt.plot((mech1.p1.x, p2.x),(mech1.p1.y, p2.y), label = "link1")
# plt.plot((p2.x, p3.x),(p2.y, p3.y), label = "link2")
# plt.plot((p3.x, p4.x),(p3.y, p4.y), label = "link3")
# plt.plot((p4.x, p1.x),(p4.y, p1.y), label = "link4")
# plt.plot(x_array, y_array)
# plt.legend()
plt.show()







