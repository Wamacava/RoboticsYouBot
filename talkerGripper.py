
import rospy
import brics_actuator.msg
from brics_actuator.msg import JointPositions, JointValue, Poison

def talker():
    pub = rospy.Publisher('/arm_1/gripper_controller/position_command', JointPositions, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
	data1 = JointPositions()
	data2 = JointPositions()

        #data1.poisonStamp.originator =''
        #data1.poisonStamp.description =''
        #data1.poisonStamp.qos = 0.0
    
        #data1.positions.timeStamp =0
        data1.positions.joint_uri ='gripper_finger_joint_l'
        data1.positions.unit ='m'
        data1.positions.value = 0

        #data2.positions.timeStamp =0
        data2.positions.joint_uri ='gripper_finger_joint_r'
        data2.positions.unit ='m'
        data2.positions.value = 0

       


        
	#data.positions[0].value = 2.95 
        #data.positions[1].value = 1.05
        #data.positions[2].value = -2.44
        #data.positions[3].value = 1.73
        #data.positions[4].value = 2.95

	#data.positions.value = 2
        #hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(data1)
        pub.publish(data1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
