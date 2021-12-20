
#import motor_time
import cv2
'''
import pyfirmata 
import time

comport ='COM3'

board=pyfirmata.Arduino(comport)

#pin setup belt
belt_f = board.get_pin('d:2:o')
belt_r = board.get_pin('d:3:o') 
beltSpeed_6 = board.get_pin('d:6:p') # belt speed control

# box position
Push_f = board.get_pin('d:4:o')
Push_r = board.get_pin('d:7:o')
PushSpeed = board.get_pin('d:5:p') #position speed


# box push
boxPush_f = board.get_pin('d:8:o')
boxPush_r = board.get_pin('d:9:o') 


objectPush_f = board.get_pin('d:10:o')
objectPush_r = board.get_pin('d:12:o')
objectPushSpeed = board.get_pin('d:11:p') # object push speed control


def belt_run():
    belt_f.write(1)
    belt_r.write(0)
    beltSpeed_6.write(0.4)
    time.sleep(0.2)


def belt_stop():
    belt_f.write(0)
    belt_r.write(0)
    time.sleep(1)

def box_position_1_2():
    Push_f.write(1)
    Push_r.write(0)
    PushSpeed.write(0.4)
    time.sleep(2.4)

    Push_f.write(0)
    Push_r.write(0)
    time.sleep(1)

def box_position_2_3():
    Push_f.write(1)
    Push_r.write(0)
    PushSpeed.write(0.4)
    time.sleep(2.7)

    Push_f.write(0)
    Push_r.write(0)
    time.sleep(1)

def box_position_3_2():
    Push_f.write(0)
    Push_r.write(1)
    PushSpeed.write(0.4)
    time.sleep(2.7)

    Push_f.write(0)
    Push_r.write(0)
    time.sleep(1)

def box_position_2_1():
    Push_f.write(0)
    Push_r.write(1)
    PushSpeed.write(0.4)
    time.sleep(2.7)

    Push_f.write(0)
    Push_r.write(0)
    time.sleep(1)

def box_position_1_3():
    Push_f.write(1)
    Push_r.write(0)
    PushSpeed.write(0.4)
    time.sleep(5.5)

    Push_f.write(0)
    Push_r.write(0)
    time.sleep(1)

def box_position_3_1():
    Push_f.write(0)
    Push_r.write(1)
    PushSpeed.write(0.4)
    time.sleep(5.5)

    Push_f.write(0)
    Push_r.write(0)
    time.sleep(1)

def box_push():
    boxPush_f.write(1)
    boxPush_r.write(0)
    time.sleep(4.3)

    boxPush_f.write(0)
    boxPush_r.write(0)
    time.sleep(1)

    boxPush_f.write(0)
    boxPush_r.write(1)
    time.sleep(4.3)

    boxPush_f.write(0)
    boxPush_r.write(0)
    time.sleep(1)

def object_push():

    objectPush_f.write(0)
    objectPush_r.write(1)
    objectPushSpeed.write(0.3)
    time.sleep(0.2)

    objectPush_f.write(0)
    objectPush_r.write(0)
    time.sleep(1)

    objectPush_f.write(1)
    objectPush_r.write(0)
    objectPushSpeed.write(0.3)
    time.sleep(0.2)

    objectPush_f.write(0)
    objectPush_r.write(0)
    time.sleep(1)


#while True:
    #box_position_1_2()
    #belt_run()
    #box_position_2_3()
    #box_position_3_2()
    #box_position_2_1()
    #box_position_1_3()
    #box_position_3_1()
    #box_push()
    #object_push()
'''

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width /2)
    cy = int(height /2)
    #print(cx,cy)
    ###########################
    nx = int(350)
    ny = int(240)

    pixel_center1 = hsv_frame[ny, nx]
    hue_value1 = pixel_center1[0]

    nx1 = int(290)
    ny1 = int(240)

    pixel_center2 = hsv_frame[ny1, nx1]
    hue_value2 = pixel_center2[0]

    nx2 = int(320)
    ny2 = int(270)

    pixel_center3 = hsv_frame[ny2, nx2]
    hue_value3 = pixel_center3[0]

    nx3 = int(320)
    ny3 = int(210)

    pixel_center4 = hsv_frame[ny3, nx3]
    hue_value4 = pixel_center4[0]

    ######################################
    # Pick pixel value
    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    

    color = "Belt"
    
    #print(hue_value)
    #time.sleep(1)
    #belt_run() #call belt run

    if (hue_value < 15) and (hue_value1 <15) and (hue_value2 <15) and (hue_value3 <15) and (hue_value4 <15):
        color = "RED"
        print(hue_value, hue_value1, hue_value2, hue_value3)
        

    #elif hue_value < 22:
        #color = "ORANGE"
        

    elif hue_value < 33:
        if hue_value1 <33:
            if hue_value2 <33:
                if hue_value3 <33:
                    if hue_value4 <33:
                        color = "BLUE" 
                        print(hue_value, hue_value1, hue_value2, hue_value3)

    elif hue_value < 78:
        if hue_value1 <78:
            if hue_value2 <78:
                if hue_value3 <78:
                    if hue_value4 <78:
                        color = "GREEN"
                        print(hue_value, hue_value1, hue_value2, hue_value3)


    #elif hue_value < 131:
        #color = "BLUE"
        

    #elif hue_value < 170:
        #color = "VIOLET

        

    
    #belt_stop()

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
##################################################################################################
   
   
   
    pixel_center_bgr1 = frame[ny, nx]
    b1, g1, r1 = int(pixel_center_bgr1[0]), int(pixel_center_bgr1[1]), int(pixel_center_bgr1[2])

    cv2.rectangle(frame, (nx - 120, 10), (nx + 100, 70), (255, 255, 255), -1)
    cv2.putText(frame, color, (nx - 55, 50), 0, 0.8, (b1, g1, r1), 2)
    cv2.circle(frame, (nx, ny), 5, (25, 25, 25), 3)
   

    pixel_center_bgr2 = frame[ny1, nx1]
    b2, g2, r2 = int(pixel_center_bgr2[0]), int(pixel_center_bgr2[1]), int(pixel_center_bgr2[2])

    cv2.rectangle(frame, (nx1 - 120, 10), (nx1 + 100, 70), (255, 255, 255), -1)
    cv2.putText(frame, color, (nx1 - 55, 50), 0, 0.8, (b2, g2, r2), 2)
    cv2.circle(frame, (nx1, ny1), 5, (25, 25, 25), 3)


    pixel_center_bgr3 = frame[ny2, nx2]
    b3, g3, r3 = int(pixel_center_bgr3[0]), int(pixel_center_bgr3[1]), int(pixel_center_bgr3[2])

    cv2.rectangle(frame, (nx2 - 120, 10), (nx2 + 100, 70), (255, 255, 255), -1)
    cv2.putText(frame, color, (nx2 - 55, 50), 0, 0.8, (b3, g3, r3), 2)
    cv2.circle(frame, (nx2, ny2), 5, (25, 25, 25), 3)
   
    pixel_center_bgr4 = frame[ny3, nx3]
    b4, g4, r4 = int(pixel_center_bgr4[0]), int(pixel_center_bgr4[1]), int(pixel_center_bgr4[2])

    cv2.rectangle(frame, (nx3 - 120, 10), (nx3 + 100, 70), (255, 255, 255), -1)
    cv2.putText(frame, color, (nx3 - 55, 50), 0, 0.8, (b4, g4, r4), 2)
    cv2.circle(frame, (nx3, ny3), 5, (25, 25, 25), 3)
   
   
   
    #print(color) # print color name
###################################################################################################
    cv2.rectangle(frame, (cx - 120, 10), (cx + 100, 70), (255, 255, 255), -1)
    cv2.putText(frame, color, (cx - 55, 50), 0, 0.8, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

    cv2.imshow("Frame", frame)
    print(hue_value, hue_value1, hue_value2, hue_value3)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
