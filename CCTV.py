import cv2

url = 'rtsp://admin:savezaa2616@192.168.1.64:554/Streaming/Channels/1' #RTSP URL ที่ได้มาจากข้อก่อนหน้า
capture = cv2.VideoCapture(url) 

while True:
  ret, frame = capture.read()
  cv2.imshow('Output', frame)
  k = cv2.waitKey(10) &0xFF
  if k == 27:
     break
   
capture.release()
cv2.destroyAllWindows()

