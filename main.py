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
    
   
    return render_template('login.html',flag=0)
@app.route("/register")

def register():
    
   
    return render_template('register.html',flag=0,f=0,h="")

@app.route("/registered",methods=['GET','POST'])
def registered():
    if request.method=='POST':
        username=request.form.get('user')
        name=request.form.get('name')
        email=request.form.get('email')
        mobile=request.form.get('mob')
        address=request.form.get('add')
        password=request.form.get('password')
        qq=db.user
        k6=list(qq.find({"username":username}))
        if len(password)<8:
            h='Password Length should be atleast 8 characters long'
            return render_template('register.html',flag=0,f=1,h=h)
        elif len(mobile)!=10:
            h='Invalid Mobile'
            return render_template('register.html',flag=0,f=1,h=h)
        elif len(k6)!=0:
            h="Username Exists"
            return render_template('register.html',flag=0,f=1,h=h)
            
         
            
        dic={"name":name,"username":username,"password":password,"mob":mobile,"email":email,"address":address}
        
        qq.insert_one(dic)
    
        
   
    return render_template('register.html',flag=1,f=0,h="")
@app.route("/logout")
def logout():
    te=db.cu
    ju=list(te.find())
    r=db.rec
    gh={"username":ju[0]["username"],"logout":"b"}
    ty=list(r.find(gh))
    dr={"username":ju[0]["username"],"logout":"b","login":ty[0]["login"]}
    dt=datetime.now()
    dd={"username":ju[0]["username"],"logout":dt,"login":ty[0]["login"]}
   
    r.update_one(dr,{'$set':dd})
    
    te.delete_many({})
    return redirect('/login')
@app.route("/entry",methods=['GET','POST'])
def entry():
    tr=db.cu
    if request.method=='POST':
        username=request.form.get('userid')
        password=request.form.get('password')
        qw=db.user
        r=db.rec
        dt=datetime.now()
        k5=list(qw.find({"username":username}))
        if(len(k5)!=0 and password==k5[0]["password"]):
            
            de={"username":username}
            dtt={"username":username,"logout":"b","login":dt}
            r.insert_one(dtt)
            tr.insert_one(de)
            return render_template('entry.html',k5=k5)
        else:
            return render_template('login.html',flag=1)
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
        return render_template('add.html',flag=1)
    
    return render_template('add.html',flag=0)
    
     
@app.route("/exit",methods=['GET','POST'])
def exitt():
    if request.method=='POST':
        no=request.form.get('number')
        qws=db.cu
        ku=list(qws.find())
        users=ku[0]["username"]
        qs=db.user
        k6=list(qs.find({"username":users}))
        dr={"number":no,"org":k6[0]["name"],"exit":"b"}
        dt=datetime.now()
        dd={"number":no,"org":k6[0]["name"],"exit":dt}
        qww=db.data
        qww.update_one(dr,{'$set':dd})
        return render_template('exit.html',flag=1)
        
    return render_template('exit.html',flag=0)
@app.route("/history",methods=['GET','POST'])
def history():
    
    if request.method=='POST':
        no=request.form.get('number')
        qws=db.cu
        ku=list(qws.find())
        users=ku[0]["username"]
        qs=db.user
        k6=list(qs.find({"username":users}))
        dr={"number":no,"org":k6[0]["name"]}
        qww=db.data
        k5=list(qww.find(dr))
        if len(k5)!=0:
            
            return render_template('hist.html',k5=k5)
        return render_template('history.html',flag=1)
        
    
   
    return render_template('history.html',flag=0)
@app.route("/loginh")
def historylogin():
    gt=db.rec
    tu=db.cu
    lis=list(tu.find())
    users=lis[0]["username"]
    k5=list(gt.find({"username":users}))
   
    return render_template('loginhist.html',k5=k5)
app.run(debug=True)
