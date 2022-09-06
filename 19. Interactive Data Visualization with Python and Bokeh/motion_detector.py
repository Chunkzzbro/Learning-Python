#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.listdir()


# In[15]:


#DATA FROM THE 156-157


import cv2
import time
import pandas

df = pandas.DataFrame(columns = ["Start","End"])    #Creates a Dataframe with columns Start and End to store the timestamps of the object entering and exiting the frame
from datetime import datetime

status_list = [None,None]                           #For storing when an object enters and exit the frames
times = []                                          #Timestamp of the entry and exit of item
video = cv2.VideoCapture(0)                         #Switches on the web camera. 0 for builtin camera and 1 for external camera

##initializing first frame.
first_frame = None

while True:                                                   #Iterating per milli second to display a video
   
    check,frame = video.read()                                #Captures Each frame and also checks whether video is read or not 
    status = 0                                                #Shows whether there is an contour object with difference less than 1000 present at a current time
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)             #Converts the BGR frame into a grayscale
    gray = cv2.GaussianBlur(gray,(21,21),0)                   #Blurring the grayscale version
    
#if condition to get the first frame for comparison
    if first_frame is None :
        first_frame = gray
        continue
        
    
    delta_frame = cv2.absdiff(first_frame,gray)               #shows difference in intensities of corresponding pixels of first frame and gray
    thresh_delta = cv2.threshold(delta_frame,30,255,          #Makes all the pixel with differences more than 30 to 225 
                                 cv2.THRESH_BINARY)[1]
    
    thresh_delta = cv2.dilate(thresh_delta,None ,             #Smoothening the thresh delta
                              iterations = 2)
    
#Forming Contours:
    (cnts,_) = cv2.findContours(thresh_delta.copy(),         #Finding the countours in thresh delta.
                                 cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in cnts:                                    #A for loop to check if the countour value is less than 1000 and to make a rectangle over the countour
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x,y,w,h) = cv2.boundingRect(contour)  
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),3)
        

    status_list.append(status)                                #List displaying status of item entering and exiting frame
    
    status_list = status_list[-2:]
    
    if status_list[-1] == 1 and status_list[-2] ==0:          #When status changes from 0 to 1 (entry) and from 1 to 0 Exit the timestamp of when the object enters and exit the fram
        times.append(datetime.now())                        
    if status_list[-1] == 0 and status_list[-2] ==1:
        times.append(datetime.now())   

        
#Displaying the captured frame in an external window:    
    
    cv2.imshow("Gray",gray)                                   #Shows the converted gray scale image in another window
    cv2.imshow("Delta",delta_frame)                           #Shows the delta frame 
    cv2.imshow("threshold frame",thresh_delta)                #Shows the threshold Frame
    cv2.imshow("ColorFrame",frame)                            #shows the color frame with rectangles.
    
    key = cv2.waitKey(1)                                      #Transfers control to next loop unless q is pressed where it breaks from loop
    
    if key==ord('q'):                                         #When q is pressed it exits the video
        if status ==1:                                        #To store the final timestamp into times list where the video is stopped incase the status of object is still 1
            times.append(datetime.now())
        break
    
    
    
    print(status)                                             #Shows whether there is something entering or moving out from frame

    
    
print(status_list)
print(times)

          
for i in range(0,len(times),2):                               #With a step of 2, of the values in times the entry of object is stored under start and the exit of object is stored under end               
    df = df.append({"Start":times[i],"End":times[i+1]},
                    ignore_index = True)
    
df.to_csv("Times.csv")                                        #Saves File to CSV

video.release()                                               #The webcame turns off and video is released
cv2.destroyAllWindows()  


# In[16]:





# In[ ]:





# In[ ]:




