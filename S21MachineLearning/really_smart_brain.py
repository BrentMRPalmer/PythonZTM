# New Version:
# imageai.Prediction no longer exists, replaced by imageai.Classification
from imageai.Classification import ImageClassification
import os
 
exec_path = os.getcwd()
 
prediction = ImageClassification()
# SqueezeNet model also no longer exists, now the fastest is MobileNetV2
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(exec_path, 'mobilenet_v2-b0353104.pth'))
prediction.loadModel()
 
predictons, probabilities = prediction.classifyImage(os.path.join(exec_path,'house.jpg'), result_count=5)
for eachPred, eachProb in zip(predictons, probabilities):
    print(f'{eachPred} : {eachProb}')