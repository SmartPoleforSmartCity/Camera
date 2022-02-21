import cv2
from datetime import datetime as date

def generate_file():
    file_name = "CAM1_" + date.now().strftime("%d%m%Y-%H%M%S")+".mp4"
    return cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'DIVX'), 20, (1920,1080))
    
def run_record():
    time = 0
    writer= generate_file()
    while(True):
         # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        writer.write(frame)
        # Display the resulting frame
        cv2.imshow('frame',frame)
        time += 1
        if cv2.waitKey(1) and time == 1260:
            break
        
    print(time)
    cap.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    cap = cv2.VideoCapture()
    cap.open("rtsp://admin:savezaa2616@192.168.1.64:554/Streaming/channels/1/")
    while(True):
        run_record()
