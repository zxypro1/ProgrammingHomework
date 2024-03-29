import requests
import base64
import json
#此文件为人脸对比功能的算法文件
def Get_API():  # 取得API

    client_id = 'yumZRsADUevI5s0rgPnac0MW'
    client_secret = 'ZrUNa8xMiC6M9OkyX0pIBHl4648WEXsL'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (
        client_id, client_secret)

    response = requests.get(host)
    access_token = eval(response.text)['access_token']
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/match'
    API = request_url + "?access_token=" + access_token

    return API


def Image_coding(img1, img2):  # 将图片转化为BASE64格式
    f = open(r'%s' % img1, 'rb')
    pic1 = base64.b64encode(f.read())
    f.close()
    f = open(r'%s' % img2, 'rb')
    pic2 = base64.b64encode(f.read())
    f.close()
    params = json.dumps([
        {"image": str(pic1, "utf-8"), "image_type": 'BASE64', "face_type": "LIVE"},
        {"image": str(pic2, "utf-8"), "image_type": 'BASE64', "face_type": "LIVE"}])
    return params



def Image_contrast(img1, img2):  # 图片对比

    API = Get_API()
    if(img1 is not '' and img2 is not ''):
        params = Image_coding(img1, img2)
        content = requests.post(API, params).text
        try:#异常处理
            score = eval(content)['result']['score']
            return '两人相似得分为%s' % str(score)
        except IOError:
            return '未能写入文件'
        except NameError:
            return '未找到人脸'
    else:
        return '请选择图片'