#!/usr/bin/python
import rospy
from std_msgs.msg import Float64
import numpy as np
import math

class Controller:
    def __init__(self):
        ## Robot has 5 joints
        self.link_length = 0.2
        self.rate = rospy.Rate(10) # 10hz
        self.publisher = [None] * 5
        _0T1 = np.zeros((4, 4))
        _1T2 = np.zeros((4, 4))
        _2T3 = np.zeros((4, 4))
        _3T4 = np.zeros((4, 4))
        _4T5 = np.zeros((4, 4))
        q_desired = np.full((5, 1), math.pi/6)

        for i in range(1, 6):
            print(i)
            self.publisher[i-1] = rospy.Publisher('/custom_pos/joint' + str(i-1)  + '_position_controller/command', Float64, queue_size=1)


    def forwardKinematics(self):
        while not rospy.is_shutdown():
            self.rate.sleep()
            self.publisher[4].publish(0.5)



    def main(self):
        self.forwardKinematics()
        rospy.spin()



if __name__ == '__main__':
    try:
        rospy.init_node('controller')
        positioner = Controller()
        positioner.main()
    except rospy.ROSInterruptException:
        pass
        