
#Khởi tạo bảng 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
 
 
db = SQLAlchemy()
 

#mỗi class là 1 bảng 

class Student(db.Model): 
    __tablename__ = "Thông tin sinh viên"
    Msv = db.Column(db.Integer, primary_key=True) 
    Name = db.Column(db.String, nullable=False)     
    Birth  = db.Column(db.DATE, nullable=False)
    Class = db.Column(db.String, nullable=False)
    Phone = db.Column(db.Integer, nullable=False)

class Teacher(db.Model):
    __tablename__="Thông tin giảng viên"
    MGV = db.Column(db.Integer,primary_key = True)
    NameGV = db.Column(db.String,nullable = False) 
    Class = db.Column(db.String,nullable = False)
    Phone = db.Column(db.Integer,nullable = False)  
    Address = db.Column(db.String,nullable = False)


class Subjectname(db.Model): 
    __tablename__ = "Tên môn học"
    MaMH = db.Column(db.Integer, primary_key=True)
    NameMH = db.Column(db.String, nullable=False)
    SoTin = db.Column(db.Integer, nullable=False)
    GiangVien = db.Column(db.String, nullable=False)
    Time = db.Column(db.String, nullable=False)

class Dangkymh(db.Model): 
    __tablename__="Đăng ký môn học"
    NameSV = db.Column(db.String, nullable=False)
    Msv = db.Column(db.Integer,db.ForeignKey("Thông tin sinh viên.Msv"),primary_key=True)#Liên kết với Thông tin sinh viên
    Class = db.Column(db.String, nullable=False)
    Birth  = db.Column(db.DATE, nullable=False)
    NameMH = db.Column(db.String,nullable=False)

 

 

    
     
      

    



   
     



 