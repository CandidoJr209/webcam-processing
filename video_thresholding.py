import cv2

def nothing(a):
    pass

def main():
    
    cap = cv2.VideoCapture(0)

    cv2.namedWindow("adjust")
    cv2.resizeWindow("adjust", 640,240)
    cv2.createTrackbar("gain","adjust",10,20,nothing)
    cv2.createTrackbar("bias","adjust",0,100,nothing)


    while(True):

        ret, frame = cap.read()

        value = cv2.getTrackbarPos("gain","adjust")
        alpha = 0.1*value

        beta = cv2.getTrackbarPos("bias","adjust")

        frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

        frame = cv2.flip(frame,1)

        cv2.imshow('video', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()

    cv2.destroyAllWindows()
 
 
if __name__ == __main__:
    main()
