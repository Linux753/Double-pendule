import cv2

continuer=True

cap=cv2.VideoCapture(0)

print("Dimentions capture :", cap.get(3),"*",cap.get(4))
cap.set(3, 640)
cap.set(4,480)

fourcc=cv2.VideoWriter_fourcc(*'XVID')
fileOut=cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))
absPoint=[0]*640*480
nbAbsPoint=0

while(cap.isOpened() and continuer):
    ret,frame=cap.read()
    if ret:
        fileOut.write(frame)
        for i in range(0, frame.shape[0], 1):
            for j in range(0, frame.shape[1],1):
                if frame.item(i,j,1)>80 and frame.item(i,j,2)>80 and frame.item(i,j,0)<100:
                    frame.itemset((i, j, 0), 0)
                    frame.itemset((i,j,1),0)
                    frame.itemset((i, j, 2), 255)
                    absPoint[nbAbsPoint]=i
                    nbAbsPoint=nbAbsPoint+1
        cv2.imshow("Video", frame)
        print(absPoint[round(nbAbsPoint/2)])
        nbAbsPoint=0
    if cv2.waitKey(1)== ord('q'):
        continuer=False

cap.release()
fileOut.release()
cv2.destroyAllWindows()

