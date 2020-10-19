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
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/faceset/user/add'
    API = request_url + "?access_token=" + access_token

    return API


def Image_coding(img,str1):  # 将图片转化为BASE64格式
    f = open(r'%s' % img, 'rb')
    pic = base64.b64encode(f.read())
    f.close()
    params = json.dumps(
        {"image": str(pic, "utf-8"), "image_type": 'BASE64', "group_id": "DEMO", "user_id": str1, "face_type": "LIVE"}
    )
    return params



def FaceSignUp(img,str1):  # 在数据库中搜索照片
    API = Get_API()
    if(img is not '' and str1 is not ''):
        params=Image_coding(img,str1)
        content = requests.post(API, params).text
        try:
            token=eval(content)['result']['face_token']
            if token is not '':
                return '上传成功！'
            else:
                return '上传失败！'
        except IOError:
            return '未能写入文件'
        except NameError:
            return '未找到人脸'
    else:
        return '请选择人脸或输入名字！'