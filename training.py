import os
import cv2
import numpy as np
from PIL import Image

recognizer=cv2.face.LBPHFaceRecognizer_create()
path='Dataset'
if not os.path.exists('./recognizer'):
    os.makedirs('./recognizer')

def getImagewithID(path):
    imagepaths=[os.path.join(path,f) for f in os.listdir(path)]
    Faces=[]
    Id=[]
    for imagepath in imagepaths:
        faceImg=Image.open(imagepath).convert('L')
        faceNP=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagepath)[-1].split('.')[1])
        Faces.append(faceNP)
        Id.append(ID)
        cv2.imshow('train',faceNP)
        cv2.waitKey(10)
    return np.array(Id),Faces

Id,Faces=getImagewithID(path)
recognizer.train(Faces,Id)
recognizer.save('recognizer/trainingData.yml')
print('Training Completed Successfully')
cv2.destroyAllWindows()