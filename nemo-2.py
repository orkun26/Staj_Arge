import cv2 
import numpy as np

camera = cv2.VideoCapture("2.mp4") #video dosyadan okundu. 


def nothing(x):
    pass
cv2.namedWindow("frame")
cv2.createTrackbar("H1","frame",0,180,nothing)   #TRACKBAR OLUŞTURULDU.
cv2.createTrackbar("H2","frame",0,180,nothing)
cv2.createTrackbar("S1","frame",0,255,nothing)
cv2.createTrackbar("S2","frame",0,255,nothing)
cv2.createTrackbar("V1","frame",0,255,nothing)
cv2.createTrackbar("V2","frame",0,255,nothing)

 
while camera.isOpened():  # kamera açıldı ise 
    
    ret,frame = camera.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #rgb'yi hsvye çevirdi.
    
    H1= cv2.getTrackbarPos("H1","frame")  #TRACKBAR OKUMA İŞLEMİNİ GERÇEKLEŞTİRDİK.
    H2= cv2.getTrackbarPos("H2","frame") 
    S1= cv2.getTrackbarPos("V1","frame")
    S2= cv2.getTrackbarPos("V2","frame")
    V1= cv2.getTrackbarPos("S1","frame")
    V2= cv2.getTrackbarPos("S2","frame")
    
    lower = np.array([H1,S1,V1])       #hsv değerine göre renk tanımlandı . 
    upper = np.array([H2,S2,V2])
    mask = cv2.inRange(hsv,lower,upper)      #maskeleme işlemi yapıldı .
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow("frame",frame)   #ekrana yazdırdı. 
    cv2.imshow("hsv",hsv)       #ekrana yazdırdı. 
    cv2.imshow("mask",mask)     #maske ekrana yazdırıldı
    cv2.imshow("res",res)       #hangi renkleri geçirdiği
     
    if cv2.waitKey(25) & 0XFF == ord("q"):     # q'ya basınca çıkması saglandı.
        break
    
    
    
cv2.destroyAllWindows()       #tüm pencereler kapatıldı . 