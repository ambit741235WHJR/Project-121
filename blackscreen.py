# Importing Modules
import numpy as np, cv2

# Starting the Video Capture
cap = cv2.VideoCapture(0)
image = cv2.imread("image.jpg")

# While Condition when video is turned on
while (cap.isOpened()):
    # Reading the frames of the video
    ret, frame = cap.read()
    
    # Resizing the image and the video to 640, 480
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))

    # Creating an array of RGB of faint black color shade and dark shade of black and storing in the variables l_black and u_black respectively.
    u_black = np.array([104, 153, 70])
    l_black = np.array([30, 30, 0])

    # Creating a mask using cv's inRange() function and passing the frame l_black and u_black as the parameters
    mask = cv2.inRange(frame, l_black, u_black)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Using np.where() function to return frame or image if the value of f is 0
    f = frame - res
    f = np.where(f == 0, image, f)

    # Displaying the masked video and the real video
    cv2.imshow("MASKED VIDEO", f)
    cv2.imshow("REAL VIDEO", frame)

    # If the user presses q, the video will be closed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()