from flask import request, render_template, session, jsonify, render_template, redirect,send_file
from app.router import app

from app.models.model import db
from app.models.user import User
from app.models.aiface import aiface

import hashlib
import os
import io
import base64
from PIL import Image 
import numpy as np 

@app.route('/')
def add_user():
    user = User('ccb', 'ccb', 'ccb', 'ccb', 'ccb')
    db.session.add(user)
    db.session.commit()
    return redirect("首页")

@app.route('/首页')
def shouye():
    return render_template('首页.html')

@app.route("/user/register", methods = ['GET', 'POST'])
def user_register():
    if request.method == 'GET':
        return render_template('user/register.html')
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        re_password = request.form.get("rePassword")
        email = request.form.get('email')
        tel = request.form.get("tel")
        birthdate = request.form.get('birthdate')
        
        err_msg = ''
        if password != re_password:
            err_msg = '两次输入密码不一致'
        
        if  len(User.query.filter(User.username == username).all()) > 0:
            err_msg = '用户名已存在'
        
        if err_msg != '':
            return render_template('user/register.html', err_msg=err_msg)
        else:
            password = calc_md5(password)
            user = User(username, password, email, tel, birthdate)
            db.session.add(user)
            db.session.commit()
            return render_template('user/login.html')

@app.route("/user/login", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template('user/login.html')
    else:
        username = request.form.get("username")
        session['username'] = username
        return redirect("../首页")

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update((password + 'my-salt').encode('utf-8'))
    return md5.hexdigest()

@app.route("/forgetpwd")
def forgetpwd():
    return render_template('forgetpwd.html')

@app.route("/contact_us")
def contact():
    return render_template('contact_us.html')

@app.route("/merge_face",methods = ['POST'])
def merge_face():
    try:
        image_name = request.form['selected-image']
        photo_choose_src = 'app/static/img/' + image_name
        face = "app/static/img/user_upload_picture/%s/user_picture" %session['username']
        aif = aiface(face,photo_choose_src)
        result_data = aif.merge_face(100)
        encoded_image = base64.b64encode(result_data).decode('utf-8')
        return jsonify({"id":1,"result":encoded_image})
    except:
        return jsonify({"id":0,"result":"请检查图片是否为人脸并稍后重试"})

@app.route('/uplord_face',methods = ['GET','POST'])
def uplord_face():
    if request.method=="GET":
        return render_template('首页.html')
    else:
        if 'username' not in session:
            return jsonify({"result":"请先进行登录"})
        if 'file' in request.files:
            folder_path = "app/static/img/user_upload_picture/%s" %session['username']
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            objpath = "app/static/img/user_upload_picture/%s/user_picture" %session['username']
            obj = request.files['file']
            obj.save(objpath)
            return jsonify({"result":"上传成功"})
        else:
            return jsonify({"result":"上传错误，请重试"})

