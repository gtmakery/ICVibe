import cv2

def main():
    cap = cv2.VideoCapture(0)
    counter = 0

    while True:
        ret, frame = cap.read()
        
        # grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # canny_image = cv2.Canny(grayscale_image, 100, 200)

        if ret:
            cv2.imshow("Webcam Stream", frame)

        if cv2.waitKey(33) == ord('a'):
            cv2.imwrite("smile/smile_" + str(counter) + ".bmp", frame)
            counter += 1


    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()