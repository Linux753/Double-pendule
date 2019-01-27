import cv2
import math

continuer=True


def dpRandomInit():
    cap = cv2.VideoCapture(0)
    ret,frame=cap.read()
    if ret :
        cv2.imshow("Double pendule" , frame)
    cap.set(3, 640)
    cap.set(4, 480)
    return cap

def dpRandom(cap, absPoint0 , ordPoint0 , absPoint1 , ordPoint1 , absPoint2 , ordPoint2):
    nbAbsPoint0 = 0
    nbOrdPoint0 = 0
    nbAbsPoint1 = 0
    nbOrdPoint1 = 0
    nbAbsPoint2 = 0
    nbOrdPoint2 = 0
    ret, frame = cap.read()
    cv2.imwrite("image.jpg", frame)
    if ret:
        for i in range(0, frame.shape[0], 1):
            for j in range(0, frame.shape[1],1):
                b=frame.item(i,j,0)
                g=frame.item(i,j,1)
                r=frame.item(i, j, 2)
                if g<140 and r<180 and b>200:
                    frame.itemset((i , j, 0), 255)
                    frame.itemset((i , j, 1), 0)
                    frame.itemset((i, j , 2), 0)
                    absPoint0[nbAbsPoint0] = j
                    nbAbsPoint0 = nbAbsPoint0 + 1
                    ordPoint0[nbOrdPoint0] = i
                    nbOrdPoint0 = nbOrdPoint0 + 1
                elif g > 200 and r < 180 and b > 150:
                    frame.itemset((i, j, 0), 0)
                    frame.itemset((i, j, 1) ,0)
                    frame.itemset((i, j, 2), 0)
                    absPoint1[nbAbsPoint1] = j
                    nbAbsPoint1 = nbAbsPoint1 + 1
                    ordPoint1[nbOrdPoint1] = i
                    nbOrdPoint1 = nbOrdPoint1 + 1
                elif g > 220 and r > 220 and b > 220:
                    frame.itemset((i, j, 0), 0)
                    frame.itemset((i, j, 1), 0)
                    frame.itemset((i, j, 2), 255)
                    absPoint2[nbAbsPoint2] = j
                    nbAbsPoint2 = nbAbsPoint2 + 1
                    ordPoint2[nbOrdPoint2] = i
                    nbOrdPoint2 = nbOrdPoint2 + 1
        cv2.imshow("Double pendule", frame)
        return (absPoint0[round(nbAbsPoint0/2)], ordPoint0[round(nbOrdPoint0/2)]),(absPoint1[round(nbAbsPoint1/2)], ordPoint1[round(nbOrdPoint1/2)]),(absPoint2[round(nbAbsPoint2/2)], ordPoint2[round(nbOrdPoint2/2)])

def dpRandomQuit(cap):
    cap.release()
    cv2.destroyAllWindows()

print(math.asin((357-293)/94))
absPoint0=[0]*(640*480)
ordPoint0=[0]*(640*480)
absPoint1=[0]*(640*480)
ordPoint1=[0]*(640*480)
absPoint2=[0]*(640*480)
ordPoint2=[0]*(640*480)
cap=dpRandomInit()
continuer=True
P0=(0,0)
P1=(0,0)
P2=(0,0)
teta1=0
teta2=0
while continuer :
    k=cv2.waitKey(1)
    if k == ord('q'):
        continuer=False
    P0,P1,P2  = dpRandom(cap , absPoint0 , ordPoint0 ,absPoint1 , ordPoint1 , absPoint2 , ordPoint2)
    print(P0)
    print(P1)
    print(P2)
    teta1=math.asin(abs(P0[0]-P1[0])/math.sqrt(pow(abs(P0[0]-P1[0]), 2)+pow(abs(P0[1]-P1[1]), 2)))*(180/math.pi)
    print(teta1 , round(math.sqrt(pow(abs(P0[0]-P1[0]), 2)+pow(abs(P0[1]-P1[1]), 2))))
    teta2=math.asin(abs(P1[0]-P2[0])/math.sqrt(pow(abs(P1[0]-P2[0]), 2)+pow(abs(P1[1]-P2[1]),2 )))*(180/math.pi)
    print(teta2 , round(math.sqrt(pow(abs(P1[0]-P2[0]), 2)+pow(abs(P1[1]-P2[1]),2 ))))



dpRandomQuit(cap)


