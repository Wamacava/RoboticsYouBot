import rospy
from brics_actuator.msg import JointPositions

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.positions)


    print("Joint 1: %s" % (data.positions[0].value))
    print("Joint 2: %s" % (data.positions[1].value))
    print("Joint 3: %s" % (data.positions[2].value))
    print("Joint 4: %s" % (data.positions[3].value))
    print("Joint 5: %s" % (data.positions[4].value))
    print("------------------------------------" )







def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/arm_1/arm_controller/position_command', JointPositions, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
