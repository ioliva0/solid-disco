from ultralytics import YOLO
import cv2

model = YOLO("runs/detect/train4/weights/best.pt")

results = model("/home/robotics/Downloads/test3.jpg")

# Visualize the results on the frame
annotated_frame = results[0].plot()

# Display the annotated frame
cv2.imshow("YOLOv8 Inference", annotated_frame)
cv2.waitKey(0)
cv2.destroyAllWindows()