import cv2

names = []
i = 5
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('c'):
       names.append(str(i+1))
       cv2.imwrite('{}.png'.format(names[i]),frame)
       i = i+1
       
    if cv2.waitKey(1) == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
