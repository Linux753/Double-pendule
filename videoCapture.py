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

def dpRandom(cap, absPoint0 , ordPoint0):
    nbAbsPoint0 = 0
    nbOrdPoint0 = 0
    ret, frame = cap.read()
    cv2.imwrite("image.jpg", frame)
    if ret:
        for i in range(0, frame.shape[0], 1):
            for j in range(0, frame.shape[1],1):
                b=frame.item(i,j,0)
                g=frame.item(i,j,1)
                r=frame.item(i, j, 2)
                if r>50 :
                    frame.itemset((i , j, 0), 255)
                    frame.itemset((i , j, 1), 0)
                    frame.itemset((i, j , 2), 0)
                    absPoint0[nbAbsPoint0] = i
                    nbAbsPoint0 = nbAbsPoint0 + 1
                    ordPoint0[nbOrdPoint0] = j
                    nbOrdPoint0 = nbOrdPoint0 + 1
        cv2.imshow("Double pendule", frame)
        if nbAbsPoint0==0:
            return (-1, -1)
        else :
            return (absPoint0[round(nbAbsPoint0/2)], ordPoint0[round(nbOrdPoint0/2)])
def dpRandomQuit(cap):
    cap.release()
    cv2.destroyAllWindows()

print(math.asin((357-293)/94))
absPoint0=[0]*(640*480)
ordPoint0=[0]*(640*480)

cap=dpRandomInit()
continuer=True
P0=(0,0)
teta1=0
teta2=0
while continuer :
    k=cv2.waitKey(1)
    if k == ord('q'):
        continuer=False
    P0 = dpRandom(cap , absPoint0 , ordPoint0 )
    if not(P0[0]==-1):
        print(P0[0],"-", P0[1])
    #teta1=math.asin(abs(P0[0]-P1[0])/math.sqrt(pow(abs(P0[0]-P1[0]), 2)+pow(abs(P0[1]-P1[1]), 2)))*(180/math.pi)
    #print(teta1 , round(math.sqrt(pow(abs(P0[0]-P1[0]), 2)+pow(abs(P0[1]-P1[1]), 2))))
    #teta2=math.asin(abs(P1[0]-P2[0])/math.sqrt(pow(abs(P1[0]-P2[0]), 2)+pow(abs(P1[1]-P2[1]),2 )))*(180/math.pi)
    #print(teta2 , round(math.sqrt(pow(abs(P1[0]-P2[0]), 2)+pow(abs(P1[1]-P2[1]),2 ))))



dpRandomQuit(cap)


