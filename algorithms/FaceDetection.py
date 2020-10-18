import requests
import base64
import json


def Get_API():  # 取得API

    client_id = 'yumZRsADUevI5s0rgPnac0MW'
    client_secret = 'ZrUNa8xMiC6M9OkyX0pIBHl4648WEXsL'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        client_id, client_secret)

    response = requests.get(host)
    access_token = eval(response.text)['access_token']
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/detect'
    API = request_url + "?access_token=" + access_token

    return API


def Image_coding(img):  # 将图片转化为BASE64格式
    f = open(r'%s' % img, 'rb')
    pic = base64.b64encode(f.read())
    f.close()
    params = json.dumps(
        {"image": str(pic, "utf-8"), "image_type": 'BASE64', "face_field": "age,beauty,gender,glasses,face_shape","face_type": "LIVE"}
    )
    return params


def FaceDetection(img):#Demo
    API=Get_API()
    if(img is not ''):
        params=Image_coding(img)
        content = requests.post(API, params).text
        num=eval(content)['result']['face_num']
        age=eval(content)['result']['face_list'][0]['age']
        beau=eval(content)['result']['face_list'][0]['beauty']
        faceshape=eval(content)['result']['face_list'][0]['face_shape']['type']
        gender=eval(content)['result']['face_list'][0]['gender']['type']
        glasses=eval(content)['result']['face_list'][0]['glasses']['type']
        #print eval(content)['result']
        return '图中有%s张脸，\n年龄为%s,\n美貌分数为%s,\n脸型为%s,\n性别为%s,\n眼镜是否戴上: %s' % (str(num),str(age),str(beau),str(faceshape),str(gender),str(glasses))
    else:
        return '请输入照片'