# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 21:00:00 2020

@author: HP
"""

from flask import Flask, render_template,request,session,redirect
from flask_pymongo import PyMongo
from pymongo import MongoClient
from datetime import datetime


app = Flask(__name__)
client=MongoClient("mongodb+srv://mittalabhyu:Mittal@cluster0.ocodw.mongodb.net/pms?retryWrites=true&w=majority")
db=client.get_database('pms')

@app.route("/")
def home():
    
   
    return render_template('index.html')
@app.route("/login")
def login():
    
   
    return render_template('login.html')
@app.route("/register")

def register():
    
   
    return render_template('register.html')

@app.route("/registered",methods=['GET','POST'])
def registered():
    if request.method=='POST':
        username=request.form.get('user')
        name=request.form.get('name')
        email=request.form.get('email')
        mobile=request.form.get('mob')
        address=request.form.get('add')
        password=request.form.get('password')
        dic={"name":name,"username":username,"password":password,"mob":mobile,"email":email,"address":address}
        qq=db.user
        qq.insert_one(dic)
        
   
    return render_template('register.html')
@app.route("/logout")
def logout():
    te=db.cu
    te.delete_many({})
    return render_template('login.html')
@app.route("/entry",methods=['GET','POST'])
def entry():
    tr=db.cu
    if request.method=='POST':
        username=request.form.get('userid')
        password=request.form.get('password')
        qw=db.user
        k5=list(qw.find({"username":username}))
        if(len(k5)!=0 and password==k5[0]["password"]):
            
            de={"username":username}
            tr.insert_one(de)
            return render_template('entry.html',k5=k5)
        else:
            return render_template('login.html')
    k7=list(tr.find())
    users=k7[0]["username"]
    qs=db.user
    k6=list(qs.find({"username":users}))
    
   
    return render_template('entry.html',k5=k6)
@app.route("/add",methods=['GET','POST'])
def add():
    if request.method=='POST':
        no=request.form.get('number')
        name=request.form.get('name')
        gg=db.cu
        k1=list(gg.find())
        users=k1[0]["username"]
        qs=db.user
        k6=list(qs.find({"username":users}))
        dt=datetime.now()
        qww=db.data
        dd={"name":name,"number":no,"org":k6[0]["name"],"exit":"b","entry":dt}
        qww.insert_one(dd)
    
    return render_template('add.html')
    
     
@app.route("/exit",methods=['GET','POST'])
def exitt():
    if request.method=='POST':
        no=request.form.get('number')
        
        dt=datetime.now()
        qww=db.data
        dd={"name":name,"number":no,"entry":dt,"exit":"b"}
        qww.insert_one(dd)
    
   
    return render_template('exit.html')
@app.route("/history")
def history():
    
   
    return render_template('history.html')
app.run(debug=True)
