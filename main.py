import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
import os
from PIL import Image
import streamlit as st
genai.configure(api_key="AIzaSyDdKhAAamBuGsNbFKJS15xILruvpKB_WQE")
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(layout='wide')


col1,col2=st.columns([2,1])
with col1:
    run=st.checkbox('Run',value=True)
    FRAME_WINDOW=st.image([])
with col2:
    st.title("Answer")
    output_text_area=st.subheader("")
txt=""
prev_pos=None
canvas=None
image_combined=None
erase_color=(0,0,0)   #Color of the eraser
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
# Initialize the HandDetector class with the given parameters
detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.8, minTrackCon=0.5)

#Detecting the Hand
def getHandInfo(img):
    # Find hands in the current frame
    # The 'draw' parameter draws landmarks and hand outlines on the image if set to True
    # The 'flipType' parameter flips the image, making it easier for some detections
    hands, img = detector.findHands(img, draw=False, flipType=True)
    # Check if any hands are detected
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)
        return fingers1,lmList1
    else:
        return None

#Drawing

def draw(info,prev_pos,canvas):
    fingers,lmlist=info
    current_pos=None
    if fingers==[0,1,0,0,0]:
        current_pos=lmlist[8][0:2]
        if prev_pos is None:prev_pos=current_pos
        cv2.line(canvas,current_pos,prev_pos,(255,0,255),10)
    elif fingers==[1,0,0,0,0]:
        canvas=np.zeros_like(img)
    elif fingers == [0, 1, 1, 0, 0]:
        current_pos = lmlist[8][0:2]
        if prev_pos is None: prev_pos = current_pos
        cv2.circle(img, current_pos, 80, (0, 0, 0), -1)
        cv2.circle(canvas, prev_pos, 80, erase_color, -1)

    return current_pos,canvas




# SEND TO GEMINI

def sendtoai(model,canvas,fingers):
    if fingers==[1,1,0,0,1]:
        pil_image=Image.fromarray(canvas)
        response = model.generate_content(["Solve this math problem and give a proper explaination:",pil_image])
        return response.text




# Continuously get frames from the webcam
while True:
    # Capture each frame from the webcam
    # 'success' will be True if the frame is successfully captured, 'img' will contain the frame
    success, img = cap.read()
    img=cv2.flip(img,1)
    if canvas is None:
        canvas=np.zeros_like(img)

    info=getHandInfo(img)
    if info:
        fingers , lmlist=info
        prev_pos,canvas=draw(info,prev_pos,canvas)
        txt=sendtoai(model,canvas,fingers)
    image_combined=cv2.addWeighted(img,0.7,canvas, 0.3,0)
    FRAME_WINDOW.image(image_combined,channels="BGR")
    if txt:
        output_text_area.text(txt)
    # cv2.imshow("Image", img)
    # cv2.imshow("Canvas",canvas)
    #cv2.imshow("Combined",image_combined)
    cv2.waitKey(1)



