import cv2
import face_recognition as FR

windowW = 640
windowH = 360
fps = 30
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, windowW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, windowH)
cam.set(cv2.CAP_PROP_FPS,fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

AsqaureImg = FR.load_image_file('demoImages-master/known/Donald Trump.jpg')
AsquareLoc = FR.face_locations(AsqaureImg)[0]
AsquareEnc = FR.face_encodings(AsqaureImg)[0]

knownEnc = [AsquareEnc]
names = ['Asquare']
while True:
    ignore, frame = cam.read()
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    unKnownImg = frameRGB
    unknownLocs = FR.face_locations(unKnownImg)
    unknownEncs = FR.face_encodings(unKnownImg)
    print(unknownLocs)

    for unknownLoc,unknownEnc in zip(unknownLocs,unknownEncs):
        top,left,buttom,right = unknownLoc
        cv2.rectangle(frame,(left,top),(right,buttom),(0,255,0),2)
        compare = FR.compare_faces(knownEnc,unknownEnc)
        print(compare)
        name = 'unknown'
        if True in compare:
            compareIdx = compare.index(True)
            name = names[compareIdx]
        cv2.putText(frame,name,(left,top),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv2.imshow('Asquare face_recognition', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()
    
    