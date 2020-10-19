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
    request_url = 'https://aip.baidubce.com/rest/2.0/face/v3/search'
    API = request_url + "?access_token=" + access_token

    return API


def Image_coding(img):  # 将图片转化为BASE64格式
    f = open(r'%s' % img, 'rb')
    pic = base64.b64encode(f.read())
    f.close()
    params = json.dumps(
        {"image": str(pic, "utf-8"), "image_type": 'BASE64', "group_id_list": "DEMO", "face_type": "LIVE"}
    )
    return params



def FaceComparsion(img):  # 在数据库中搜索照片
    API = Get_API()
    if(img is not ''):
        params=Image_coding(img)
        content = requests.post(API, params).text
        try:
            score=eval(content)['result']['user_list'][0]['score']
            if score >= 80 and score is not 'null':
                to=eval(content)['result']['face_token']
                uid=eval(content)['result']['user_list'][0]['user_id']
                gid=eval(content)['result']['user_list'][0]['group_id']
                return '找到相匹配的人脸！\n用户id为:%s\n所在组的id为:%s\n相似度为:%s' % (str(uid),str(gid),str(score))
            else:
                return '未能找到相匹配的人脸'
        except IOError:
            return '未能写入文件'
        except NameError:
            return '未找到人脸'
    else:
        return '请选择人脸'