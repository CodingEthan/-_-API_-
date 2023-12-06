import io
import requests, json, base64
from flask import send_file
    # 获取人脸关键点


class aiface(): #建立换脸类

    def __init__(self,path_face,path_changed_face):
        self.path_face=path_face
        self.path_changed_face = path_changed_face
        #构造函数

    def find_face(self, imgpath):
        http_url = "https://api-cn.faceplusplus.com/facepp/v3/detect" #api接口位置
        imgname = imgpath.split("/")[-1]
        data = {"api_key": "NGW3RejLaxJn_arqCmMQbb9bXShvCqGR",  ##所需的api_key
                "api_secret": "go3oAYS6KXDcdojb4pzJL7RvPc91DGII",##所需的api_secret
                "image_url": imgname, 
                "return_landmark":1} 
        
        files = {"image_file": open(imgpath, "rb")} # 打开文件，设置字典
        response = requests.post(http_url, data=data, files=files) # 向api请求
        req_con = response.content.decode('utf-8') #解码
        this_json2 = json.loads(req_con) #将返回的json转化为字典
        faces = this_json2['faces'] #取出人脸关键点信息
        list01 = faces[0] #取出第一张脸
        rectangle = list01['face_rectangle']
        return rectangle
        # 换脸，图片的大小应不超过 2M，number 表示换脸的相似度

    def merge_face(self,number):
        ff1 = self.find_face(self.path_changed_face)
        ff2 = self.find_face(self.path_face) #找到两张图片的脸关键点信息
        rectangle1 = str(str(ff1['top']) + "," + str(ff1['left']) + "," + str(ff1['width']) + "," + str(ff1['height']))
        rectangle2 = str(ff2['top']) + "," + str(ff2['left']) + "," + str(ff2['width']) + "," + str(ff2['height'])
        url_add = "https://api-cn.faceplusplus.com/imagepp/v1/mergeface" #人脸融合API
        f1 = open(self.path_changed_face, 'rb') 
        f1_64 = base64.b64encode(f1.read())
        f1.close()
        f2 = open(self.path_face, 'rb')
        f2_64 = base64.b64encode(f2.read())
        f2.close()
        #将两个文件转化API要求的数据流
        data = {"api_key": "NGW3RejLaxJn_arqCmMQbb9bXShvCqGR", #所需的api_key
                "api_secret": "go3oAYS6KXDcdojb4pzJL7RvPc91DGII", #所需的api_secret
                "template_base64": f1_64, "template_rectangle": rectangle1,
                "merge_base64": f2_64, "merge_rectangle": rectangle2, "merge_rate": number}

        response = requests.post(url_add, data=data)  #向API请求
        req_con1 = response.content.decode('utf-8') #解码
        req_dict = json.JSONDecoder().decode(req_con1) #转为字典
        result = req_dict['result']
        imgdata = base64.b64decode(result) #解码数据流
        return imgdata  #返回数据流
