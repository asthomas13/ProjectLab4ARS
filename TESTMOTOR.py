

import serial
import time
from time import sleep
import cv2
from ultralytics import YOLO

# Configure the serial port
serialInst = serial.Serial()
serialInst.baudrate = 9600
serialInst.port = '/dev/ttyACM0'  # Change this to match your Arduino's serial port
serialInst.open()

time.sleep(2)

def read_coordinates(filename):
    with open(filename, 'r') as file:
        coordinates = file.readlines()
    return coordinates

def process(coordinates):
    for coordinate in coordinates:
        x,y = map(int, coordinate.strip()[1:-1].split(','))
        print(x,y)
        move_to(x,y)
try:
        def move_to(target_x, target_y):
            #print(x,y)
            start_x, start_y = 0,0
            move_x= (target_x- start_x) * (1/5) 
            move_y= (target_y - start_y) * (1/5) 
            print(move_y)
            y1=0
            x1=0
            while move_y > y1:
                sleep(4)
                y1 += 20
                print(y1)
                #The following 4 lines lets all motors go forward
                message = "Forward"
                serialInst.write(message.encode())
            while move_x > x1:
                x1 += 20
                sleep(5)
                print(x1)
                message = "Left"
                serialInst.write(message.encode())
            while (move_x == x1) & (move_y == y1):
                sleep(5)
                move_x = x1
                move_y = y1
                message = "Stop"
                serialInst.write(message.encode())
                print ("GOT HERE")
                # Initialize webcam capture
                cap = cv2.VideoCapture(0)

                # State the path/location of where the video output file will be saved
                # Insert your own path by copy and pasting the file path address from File Explorer
                video_path = r'/home/aaron/Desktop/WebcamVideo.mp4'   # add video name at the end!

                # State what video codec to use (mp4, h.264, av1, etc.)
                fourcc = cv2.VideoWriter_fourcc(*'mp4v')

                # video_out = (video_path, fourcc, FPS, (Frame Width, Frame Height), isColor = T/F)
                video_out = cv2.VideoWriter(video_path, fourcc, 20, (960,720), isColor=True)

                # Load the pretrained YOLOv8 model (yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.)
                model = YOLO(r'/home/aaron/Desktop/yolov8s.pt', task='detect')
                while True:
                    # Read frame from webcam
                    ret, frame = cap.read()

                    if ret:   # Check if frame is captured successfully
                        # Run YOLOv8 Object Detection on the frame
                        # 'results' saves information about the detected objects
                        results = model(frame)
                        
                        # Visualize the results on the frame
                        annotated_frame = results[0].plot()

                        # Convert the annotated frame colors from BGR to RGB
                        annotated_frame = cv2.cvtColor(annotated_frame,cv2.COLOR_BGR2RGB)

                        # Write the annotated frame to the video output
                        video_out.write(annotated_frame)

                        # Display the annotated frame in a window
                        # cv2.imshow("YOLOv8 Webcam Tracking", annotated_frame)
                        for r in results:
                                
                                boxes = r.boxes
                                for box in boxes:
                                    
                                    c = box.cls
                                    if (model.names[int(c)]) == 'bottle':
                                        print("\nFOUND\n")
                                        while 0 < y1:
                                            sleep(4)
                                            y1 -= 20
                                            print(y1)
                                            message = "Backwards"
                                            serialInst.write(message.encode())
                                        while 0 < x1:
                                            x1-= 20
                                            sleep(5)
                                            print(x1)
                                            message = "Right"
                                            serialInst.write(message.encode())
                                        while x1 & y1 == 0:
                                            sleep(5)
                                            message = "Stop"
                                            serialInst.write(message.encode())
                        # Break the loop if 'x' is pressed
                        if cv2.waitKey(1) & 0xFF == ord("x"):
                            break

                    else:
                        # Indicate no frame was received
                        print("No frame received")               
            # while 0 < y1:
            #     sleep(4)
            #     y1 -= 20
            #     print(y1)
            #     message = "Backwards"
            #     serialInst.write(message.encode())

            # while 0 < x1:
            #     x1-= 20
            #     sleep(5)
            #     print(x1)
            #     message = "Right"
            #     serialInst.write(message.encode())
            # while x1 & y1 == 0:
            #     sleep(5)
            #     message = "Stop"
            #     serialInst.write(message.encode())

                # Initialize webcam capture
                # cap = cv2.VideoCapture(0)

                # # State the path/location of where the video output file will be saved
                # # Insert your own path by copy and pasting the file path address from File Explorer
                # video_path = r'/home/aaron/Desktop/WebcamVideo.mp4'   # add video name at the end!

                # # State what video codec to use (mp4, h.264, av1, etc.)
                # fourcc = cv2.VideoWriter_fourcc(*'mp4v')

                # # video_out = (video_path, fourcc, FPS, (Frame Width, Frame Height), isColor = T/F)
                # video_out = cv2.VideoWriter(video_path, fourcc, 20, (960,720), isColor=True)

                # # Load the pretrained YOLOv8 model (yolov8n.pt, yolov8s.pt, yolov8m.pt, etc.)
                # model = YOLO(r'/home/aaron/Desktop/yolov8s.pt', task='detect')
                # while True:
                #     # Read frame from webcam
                #     ret, frame = cap.read()

                #     if ret:   # Check if frame is captured successfully
                #         # Run YOLOv8 Object Detection on the frame
                #         # 'results' saves information about the detected objects
                #         results = model(frame)

                #         # Visualize the results on the frame
                #         annotated_frame = results[0].plot()

                #         # Convert the annotated frame colors from BGR to RGB
                #         annotated_frame = cv2.cvtColor(annotated_frame,cv2.COLOR_BGR2RGB)

                #         # Write the annotated frame to the video output
                #         video_out.write(annotated_frame)
                #         for r in results:
                                
                #                 boxes = r.boxes
                #                 for box in boxes:
                                    
                #                     c = box.cls
                #                     if (model.names[int(c)]) == 'bottle':
                #                         print("\nFOUND\n")
                                            
                #         # Display the annotated frame in a window
                #         cv2.imshow("YOLOv8 Webcam Tracking", annotated_frame)

                #         # Break the loop if 'x' is pressed
                #         if cv2.waitKey(1) & 0xFF == ord("x"):
                #             break

                #     else:
                #         # Indicate no frame was received
                #         print("No frame received")
                    
        coordinates = read_coordinates('coordinates.txt')
        process(coordinates) 
except KeyboardInterrupt:        
    GPIO.cleanup()
    
# Close the serial port
serialInst.close()
