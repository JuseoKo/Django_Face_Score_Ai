import cv2
import numpy as np
import re
from keras.models import load_model

def Ai(img):
    #모델 경로
    model = load_model('/Users/maria/Desktop/Code/DjangoFileUpload/Core/ai.h5')

    #이미지 경로 , 이미지를 담아둘 배열
    main_img = []
    img_path = img
    #이미지 불러오기
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #이미지 리사이징
    img_resized = cv2.resize(img, (350, 350))
    img_resized = img_resized.astype(np.float32) / 255.
    main_img.append(img_resized)
    main_img = np.array(main_img, dtype=np.float32)

    #모델을 활용한 결과 출력과 전처리
    data = model.predict(main_img)
    data = str(data)
    data = re.sub('\]','', data)
    data = re.sub('\[','', data)
    data = round(float(data), 2)

    return data
