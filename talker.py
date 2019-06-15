import rospy
from brics_actuator.msg import JointPositions, JointValue, Poison
import string
import math


def talker(Q):
    pub = rospy.Publisher('/arm_1/arm_controller/position_command', JointPositions, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    count = 0


    while not rospy.is_shutdown():


        joint_pos = JointPositions()
        joint_number = 1


        joint_val_1 = JointValue()
        joint_val_2 = JointValue()
        joint_val_3 = JointValue()
        joint_val_4 = JointValue()
        joint_val_5 = JointValue()


        joint_val_1.joint_uri = "arm_joint_1"
        joint_val_1.unit = "rad"
        joint_val_2.joint_uri = "arm_joint_2"
        joint_val_2.unit = "rad"
        joint_val_3.joint_uri = "arm_joint_3"
        joint_val_3.unit = "rad"
        joint_val_4.joint_uri = "arm_joint_4"
        joint_val_4.unit = "rad"
        joint_val_5.joint_uri = "arm_joint_5"
        joint_val_5.unit = "rad"

        joint_val_1 = JointValue()
        joint_val_1.joint_uri = "arm_joint_1"
        joint_val_1.unit = "rad"
        joint_val_1.value = Q[0] + 2.95         #adding offsets to all angles, we assume 0's
                                                 #in candle possition, youbot diver has 0's
                                                 #close to folded possition

        joint_val_2 = JointValue()
        joint_val_2.joint_uri = "arm_joint_2"
        joint_val_2.unit = "rad"
        joint_val_2.value = Q[1] + 1.05

        joint_val_3 = JointValue()
        joint_val_3.joint_uri = "arm_joint_3"
        joint_val_3.unit = "rad"
        joint_val_3.value = Q[2] - 2.44

        joint_val_4 = JointValue()
        joint_val_4.joint_uri = "arm_joint_4"
        joint_val_4.unit = "rad"
        joint_val_4.value = Q[3] + 1.73

        joint_val_5 = JointValue()
        joint_val_5.joint_uri = "arm_joint_5"
        joint_val_5.unit = "rad"
        joint_val_5.value = Q[4] + 2.95



	poison = Poison()

        joint_pos.poisonStamp = poison

        joint_pos.positions = [joint_val_1, joint_val_2, joint_val_3, joint_val_4, joint_val_5]

        #pub_youbotleaparm.publish(joint_pos)

         # rospy.loginfo(joint_pos)
        pub.publish(joint_pos)

        count+=1
	rate.sleep()



	if count == 2:
                print("Published: ", Q[0]*180 / math.pi, Q[1]*180 / math.pi, Q[2]*180 / math.pi, Q[3]*180 / math.pi, Q[4]*180 / math.pi)
		return
