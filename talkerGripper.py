
import rospy
from brics_actuator.msg import JointPositions, JointValue, Poison
import string
import math


def talkerGripper(G):

    pub = rospy.Publisher('/arm_1/gripper_controller/position_command', JointPositions, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(5) # 10hz
    count = 0




    while not rospy.is_shutdown():


        joint_pos = JointPositions()
        joint_number = 1


        joint_val_1 = JointValue()
        joint_val_2 = JointValue()



        joint_val_1.joint_uri = "gripper_finger_joint_l"
        joint_val_1.unit = "rad"
        joint_val_2.joint_uri = "agripper_finger_joint_r"
        joint_val_2.unit = "rad"

        joint_val_1 = JointValue()
        joint_val_1.joint_uri = "gripper_finger_joint_l"
        joint_val_1.unit = "m"
        joint_val_1.value = G[0]


        joint_val_2 = JointValue()
        joint_val_2.joint_uri = "gripper_finger_joint_r"
        joint_val_2.unit = "m"
        joint_val_2.value = G[1]



	    poison = Poison()

        joint_pos.poisonStamp = poison

        joint_pos.positions = [joint_val_1, joint_val_2]

        #pub_youbotleaparm.publish(joint_pos)

         # rospy.loginfo(joint_pos)
        pub.publish(joint_pos)

        count+=1
	    rate.sleep()

        if count == 2:
            print("Published: ", G[0], "m", G[1], "m")
            return
