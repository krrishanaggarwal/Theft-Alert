
import cv2,time,pandas
from datetime import datetime as dt
from playsound import playsound
first_frame=None
status_list=[None,None]
# times=[]
# df=pandas.DataFrame(columns=["Start","End"])
video=cv2.VideoCapture(0)
while True:
    check,frame=video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if first_frame is None:
        first_frame=gray
        continue
    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,35,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)
    # cv2.imshow("thresh",thresh_frame)
    
    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contours in cnts:
        if cv2.contourArea(contours)<10000:
            continue
        status=1
    
        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    
    if status_list[-1]==1 and status_list[-2]==0:
    # if status==1:
        playsound("D:/programming/projects/intrusion/Burglar-alarm-sound (mp3cut.net).mp3")
        # times.append(dt.now())
    # if status_list[-1]==0 and status_list[-2]==1:
    #     times.append(dt.now())
        
    print(status) 
    
    cv2.imshow("GrayFrame",gray)
    cv2.imshow("Delta",delta_frame)
    cv2.imshow("frame",thresh_frame)
    cv2.imshow("Color",frame)
    key=cv2.waitKey(1)
    if key==ord('q'):
        # if status==1:
        #     times.append(dt.now())
        break
# for i in range(0,len(times),2):
#     df=df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)
    
    
# df.to_csv("Times.csv")
    
    
# print(times)
video.release()
cv2.destroyAllWindows()
