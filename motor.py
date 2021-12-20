import cv2
from pyfirmata import Arduino, util
import pyfirmata 
import time


comport ='COM3'

board=pyfirmata.Arduino(comport)

it = util.Iterator(board)
it.start()

################################################
##            Arduino Pins Motor              ##
################################################

#Object Push Start
Object_push_f = board.get_pin('d:2:o')
Object_push_b = board.get_pin('d:3:o')
OP_Speed_contrl = board.get_pin('d:6:p') #Object Push Motor Speed Control


#Piston Forward & Backward
Piston_push_f = board.get_pin('d:4:o')
Piston_push_b = board.get_pin('d:5:o')


#Piston Move Left & Right
Piston_move_f = board.get_pin('d:7:o')
Piston_move_b = board.get_pin('d:8:o')
PM_Speed_control = board.get_pin('d:10:p')


#Belt Run Forward & Backward
Belt_run_f = board.get_pin('d:9:o')
Belt_run_b = board.get_pin('d:12:o')
BR_Speed_control = board.get_pin('d:11:p')


################################################
##           Arduino Pins Sensors             ##
################################################

Object_push_sensor = board.get_pin('a:0:i')
Piston_move_sensor_L = board.get_pin('a:1:i')
Piston_move_sensor_M = board.get_pin('a:2:i')
Piston_push_sensor = board.get_pin('a:3:i')
Piston_move_sensor_R = board.get_pin('a:4:i')

op_sensor = Object_push_sensor.read()
pm_sensor_L = Piston_move_sensor_L.read()
pm_sensor_M = Piston_move_sensor_M.read()
pp_sensor =Piston_push_sensor.read()
pm_sensor_R = Piston_move_sensor_R.read()
time.sleep(0.2)


################################################
##               Object Push                 ##
################################################

def op_f(): #Object Push Foward
    OP_Speed_contrl.write(0.4)
    Object_push_f.write(1)
    Object_push_b.write(0)

def op_b(): #Object Push backward
    OP_Speed_contrl.write(0.4)
    Object_push_f.write(0)
    Object_push_b.write(1)


def op_s(): #Object Push Stop
    Object_push_f.write(0)
    Object_push_b.write(0)


def object_push_run():  #Object Push Motor Run
    op_f()
    time.sleep(0.2)
    op_s()
    time.sleep(0.3)
    op_b()
    time.sleep(0.2)
    op_s()
    time.sleep(1)


################################################
##         Piston Forward & Backward          ##
################################################

def pp_f(): #Piston Push Foward
    Piston_push_f.write(1)
    Piston_push_b.write(0)

def pp_b(): #Piston Push backward
    Piston_push_f.write(0)
    Piston_push_b.write(1)


def pp_s(): #Piston Push Stop
    Piston_push_f.write(0)
    Piston_push_b.write(0)


def piston_push_run():  #Piston Forward & Backward Motor Run
    pp_f()
    time.sleep(0.01)
    pp_s()
    time.sleep(1)
    pp_b()
    time.sleep(0.01)
    pp_s()
    time.sleep(1)


################################################
##         #Piston Move Left & Right          ##
################################################

def pm_R():
    Piston_move_f.write(1)
    Piston_move_b.write(0)
    PM_Speed_control.write(0.5)

def pm_L():
    Piston_move_f.write(0)
    Piston_move_b.write(1)
    PM_Speed_control.write(0.5)

def pm_s():
    Piston_move_f.write(0)
    Piston_move_b.write(0)
    #PM_Speed_control.write(0.5)


################################################
##       Belt Run Forward & Backward          ##
################################################

def br_f(): #Belt Foward
    BR_Speed_control.write(0.25)
    Belt_run_f.write(1)
    Belt_run_b.write(0)

def br_b(): #Belt backward
    BR_Speed_control.write(0.25)
    Belt_run_f.write(0)
    Belt_run_b.write(1)


def br_s(): #Belt Stop
    BR_Speed_control.write(0.3)
    Belt_run_f.write(0)
    Belt_run_b.write(0)


def red():
    while True:
        
        op_sensor = Object_push_sensor.read()
        pm_sensor_L = Piston_move_sensor_L.read()
        pm_sensor_M = Piston_move_sensor_M.read()
        pp_sensor =Piston_push_sensor.read()
        pm_sensor_R = Piston_move_sensor_R.read()
        time.sleep(0.1)

        if pm_sensor_M >= 0.600 and pm_sensor_R >= 0.600 and pm_sensor_L <= 0.599:
            br_f()
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

        elif pm_sensor_M <= 0.599 and pm_sensor_R >= 0.600 and pm_sensor_L >= 0.600:
            while pm_sensor_L >= 0.600:
                pm_L()
                
                pm_sensor_L = Piston_move_sensor_L.read()
                time.sleep(0.1)
                if pm_sensor_L <=0.599:
                    pm_R()
                    pm_s()
                    br_f()
                    break
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

        elif pm_sensor_M >= 0.600 and pm_sensor_R <= 0.599 and pm_sensor_L >= 0.600:
            while pm_sensor_L >= 0.600:
                pm_L()
                
                pm_sensor_L = Piston_move_sensor_L.read()
                time.sleep(0.1)
                if pm_sensor_L <=0.599:
                    pm_R()
                    pm_s()
                    br_f()
                    break
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

def green():
    while True:
        time.sleep(0.1)
        op_sensor = Object_push_sensor.read()
        pm_sensor_L = Piston_move_sensor_L.read()
        pm_sensor_M = Piston_move_sensor_M.read()
        pp_sensor =Piston_push_sensor.read()
        pm_sensor_R = Piston_move_sensor_R.read()

        if pm_sensor_M <= 0.599 and pm_sensor_R >= 0.600 and pm_sensor_L >= 0.600:
            br_f()
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

        elif pm_sensor_M >= 0.600 and pm_sensor_R <= 0.599 and pm_sensor_L >= 0.600:
            while pm_sensor_M >= 0.600:
                pm_L()
                
                pm_sensor_M = Piston_move_sensor_M.read()
                time.sleep(0.1)
                if pm_sensor_M <=0.599:
                    pm_R()
                    pm_s()
                    br_f()
                    break
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

        elif pm_sensor_M >= 0.600 and pm_sensor_R >= 0.600 and pm_sensor_L <= 0.599:
            while pm_sensor_M >= 0.600:
                pm_R()
                
                pm_sensor_M = Piston_move_sensor_M.read()
                time.sleep(0.1)
                if pm_sensor_M <=0.599:
                    pm_L()
                    pm_s()
                    br_f()
                    break
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

def BLUE():
    while True:
        time.sleep(0.1)
        op_sensor = Object_push_sensor.read()
        pm_sensor_L = Piston_move_sensor_L.read()
        pm_sensor_M = Piston_move_sensor_M.read()
        pp_sensor =Piston_push_sensor.read()
        pm_sensor_R = Piston_move_sensor_R.read()

        if pm_sensor_M >= 0.600 and pm_sensor_R <= 0.599 and pm_sensor_L >= 0.600:
            br_f()
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

        elif pm_sensor_M >= 0.600 and pm_sensor_R >= 0.600 and pm_sensor_L <= 0.599:
            while pm_sensor_R >= 0.600:
                pm_R()
                
                pm_sensor_R = Piston_move_sensor_R.read()
                time.sleep(0.1)
                if pm_sensor_R <=0.599:
                    pm_L()
                    pm_s()
                    br_f()
                    break
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break

        elif pm_sensor_M <= 0.599 and pm_sensor_R >= 0.600 and pm_sensor_L >= 0.600:
            while pm_sensor_R >= 0.600:
                pm_R()
                
                
                pm_sensor_R = Piston_move_sensor_R.read()
                time.sleep(0.1)
                if pm_sensor_R <=0.599:
                    pm_L()
                    pm_s()
                    br_f()
                    break
            if pp_sensor <= 0.599:
                br_b()
                br_s()
                time.sleep(0.2)
                piston_push_run()
                break  
    
 

###############################################################

####################################################
pm_sensor_L = Piston_move_sensor_L.read()
pm_sensor_M = Piston_move_sensor_M.read()
pm_sensor_R = Piston_move_sensor_R.read()
time.sleep(0.1)

if pm_sensor_L >= 0.600 and pm_sensor_R >=0.600 and pm_sensor_M >= 0.600:
    
    while pm_sensor_L >= 0.600:
        pm_L()
        pm_sensor_L = Piston_move_sensor_L.read()
        time.sleep(0.1)
        if pm_sensor_L <=0.599:
                pm_R()
                pm_s()
                break
############################################################      
'''cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)
'''
print("")
while True:
    op_sensor = Object_push_sensor.read()
    time.sleep(0.6)
    print(" ---Object Not Detected--- ", end="\r")


    #_, frame = cap.read()
    #height, width, _ = frame.shape
    #cx = int(width / 2)
    #cy = int(height / 2)
    #cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    #cv2.imshow("Frame", frame)
    #key = cv2.waitKey(1)

    if op_sensor <= 0.599:
        print("")
        print('  Object Detected')
        object_push_run()
        


        red_color_count = 0
        green_color_count = 0
        BLUE_color_count = 0

        cap = cv2.VideoCapture(0)
        
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 700)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

        while True:
            _, frame = cap.read()
            hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            height, width, _ = frame.shape

            print("")
            print(" --Camera Turned On-- ", end="\r")

            cx = int(width / 2)
            cy = int(height / 2)

            # Pick pixel value
            pixel_center = hsv_frame[cy, cx]
            hue_value = pixel_center[0]

                # New Add Line Cam
   ############################################
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

####################################################

            color = " "
            

            if (hue_value < 1) and (hue_value1 < 1) and (hue_value2 < 1) and (hue_value3 < 1) and (hue_value4 < 1):
                color = "No Color"
                print("")
                print("---Can't Detect Color---", end="/r")

                    


            elif (hue_value < 175) and (hue_value1 <175) and (hue_value2 <175) and (hue_value3 <175) and (hue_value4 <175):
                    color = "RED"
                    red_color_count = red_color_count +1

            #elif hue_value < 22:
                #color = "ORANGE"
                
            elif (hue_value < 120) and (hue_value1 <120) and (hue_value2 <120) and (hue_value3 <120) and (hue_value4 <120):
                    color = "BLUE"                        
                    BLUE_color_count = BLUE_color_count +1

            elif (hue_value < 78) and (hue_value1 <78) and (hue_value2 <78) and (hue_value3 <78) and (hue_value4 <78):
                    color = "GREEN"                
                    green_color_count = green_color_count +1

            #elif hue_value < 131:
                #color = "BLUE"
            #elif hue_value < 170:
                #color = "VIOLET"
                
            else:
                color = "Belt"


            pixel_center_bgr = frame[cy, cx]
            b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

            #print(color) # print color name

            cv2.rectangle(frame, (cx - 120, 10), (cx + 100, 70), (255, 255, 255), -1)
            cv2.putText(frame, color, (cx - 55, 50), 0, 0.8, (b, g, r), 2)
            cv2.circle(frame, (cx, cy), 5, (25, 25, 25), 3)

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

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1)

 ############################################################           
          
            if red_color_count == 30:
                print("")
                print("RED Color Count: ", red_color_count)
                print("BLUE Color Count: ", BLUE_color_count)
                print("GREEN Color Count: ", green_color_count)
                print("")
                print("Confirm RED Color")
                red()
                break
            
            elif BLUE_color_count == 30:
                print("")
                print("RED Color Count: ", red_color_count)
                print("BLUE Color Count: ", BLUE_color_count)
                print("GREEN Color Count: ", green_color_count)
                print("")
                print("Confirm BLUE Color")
                BLUE()
                break
            
            elif green_color_count == 30:
                print("")
                print("RED Color Count: ", red_color_count)
                print("BLUE Color Count: ", BLUE_color_count)
                print("GREEN Color Count: ", green_color_count)
                print("")
                print("Confirm GREEN Color")
                green()
                break
                        
#########################################################

            if key == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

'''
while True:
    #green()
    red()
    BLUE()

'''


