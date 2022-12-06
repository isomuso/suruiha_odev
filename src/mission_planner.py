#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray



class Drone:
    def __init__(self):
        self.pos_x = float()
        self.pos_y = float()
        self.pos_z = float()

        self.first_run_take_off = True
        self.take_off_x = float()
        self.take_off_y = float()

       
        self.pub = rospy.Publisher('move_drone', Float32MultiArray, queue_size=10)
        #buraya subscriber ekle
    
    #callback fonksiyonunu buraya yazın
    
    
    def set_speed_setpoint(self, control_setpoint):
        """
        control_setpoint :: liste :: [float x, float y, float z]
        """
        msg = Float32MultiArray()
        msg.data = control_setpoint
        print(control_setpoint)
        self.pub.publish(msg)
        

    # takeoff fonksiyonunu buraya yazın

    
 
rospy.init_node('gcs', anonymous=True)
crazyflie = Drone()


rate = rospy.Rate(10) # 10hz dödürmek için
#yazacağınız while döngüsünün frekansını belirlemek 
#için rate.sleep() fonksiyonunu döngüye ekleyin.

if __name__ == '__main__':
    #takeoff fonksiyonunu buradan çağırın.
    pass
