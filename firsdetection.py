from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "coffee3.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

print(os.path.join(execution_path , "coffee3.jpg"))
for eachObject in detections:
  #  print("I started")
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )