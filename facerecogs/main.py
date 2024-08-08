import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key('1NPMeeLIyMsingu6NX6fJgwOtiEbzOmgWkNYA5Aosquo').sheet1

path = "image"
image = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    image.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

encodeListKnown = findEncodings(image)
print("Encoding complete")

def markAttendance(name):
    now = datetime.now()
    dtString = now.strftime('%Y-%m-%d %H:%M:%S')
   
    # Check if name already exists in sheet
    cell = sheet.find(name)
    if cell is None:
        # If name doesn't exist, add a new row
        sheet.append_row([name, dtString])
    else:
        # If name exists, update the timestamp
        sheet.update_cell(cell.row, 2, dtString)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceloc in zip(encodesCurFrame,facesCurFrame):
       matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
       facedis = face_recognition.face_distance(encodeListKnown,encodeFace)
       matchIndex = np.argmin(facedis)

       if matches[matchIndex]:
           name = classNames[matchIndex].upper()
           y1,x2,y2,x1 = faceloc
           y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
           cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
           cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
           cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
           
           # Mark attendance in Google Sheet
           markAttendance(name)

    cv2.imshow('Webcam',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()