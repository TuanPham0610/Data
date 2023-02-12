#sử dung flask để làm web
from flask import Flask, request, render_template
from sv2 import *
 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/dangkymonhoc"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
 

#--------------------------------------------
#Đăng nhập vào web
@app.route('/dangnhap')

def login():

    return render_template("dangnhap.html")
    
#--------------------------------------------
#Trang chủ của web
@app.route("/trangchu")

def home():

    namesv = request.args.get("NameSV")
    passw = request.args.get("Pass")

    return render_template("trangchu.html",NameSV=namesv, Pass=passw)
 
#--------------------------------------------
#Thêm thông tin sinh viên
@app.route("/thongtin")

def student():

    return render_template("thongtinsv.html")


@app.route("/addsuccess")

def addsuccess():

    name = request.args.get("Name")
    msv= request.args.get("Msv")
    birth = request.args.get("Birth")
    classs = request.args.get("Class")
    phone =  request.args.get("Phone")
  
    student = Student(Name=name, Msv=msv ,Birth=birth, Class=classs,Phone=phone)
    db.session.add(student)  
    db.session.commit()

    return render_template("dangkythanhcong.html")


# thêm môn học để đăng ký 
@app.route("/monhoc")

def subject():

    return render_template("add-new-subject.html")

@app.route("/monhoc2")

def subject2():

    nameMH = request.args.get("NameMH")
    maMH = request.args.get("MaMH")
    sotin = request.args.get("SoTin")
    gv = request.args.get("GiangVien")
    time = request.args.get("Time")
   
  
    subjectname = Subjectname(NameMH=nameMH, MaMH=maMH ,SoTin=sotin, GiangVien=gv, Time=time)
    db.session.add(subjectname)
    db.session.commit()

    return render_template("addsuccessful.html")


#Đăng ký môn học cho sinh viên
@app.route("/dangkymon")

def dk():

    return render_template("dangkymonhoc.html")

@app.route("/dangky2")
def dk2():

    name = request.args.get("NameSV")
    msv =request.args.get("Msv")
    Class =request.args.get("Class")
    nameMH =request.args.get("NameMH")
    birth = request.args.get("Birth")

    dangkymh = Dangkymh(NameSV=name, Msv=msv, Class=Class, NameMH=nameMH,Birth = birth)
    db.session.add(dangkymh)
    db.session.commit()

    return render_template("dangkythanhcong.html")


#Thêm thông tin giảng viên
@app.route('/thongtingv')
def teacher():
    return render_template("Giao_vien_Input.html")

@app.route('/thongtingv2')
def teacher2():
    name = request.args.get("NameGV")
    Class = request.args.get("Class")
    phone = request.args.get("Phone")
    address  = request.args.get("Address")
    mgv = request.args.get("MGV")


    teacher = Teacher(NameGV = name , Phone = phone, Class = Class , MGV = mgv, Address=address)
    db.session.add(teacher)
    db.session.commit()
    return render_template("addsuccessful.html")

#--------------------------------------------------------------------------------------------

@app.route('/chucnang')
def function():
    return render_template('chucnang.html')

#Chức năng xóa    
@app.route('/delete')

def deletepr():

    return render_template("delete.html")  
       

 #xóa thông tin sinh viên
@app.route('/delete1') 
def delete():
    
    Msv = request.args.get("Msv")
    dangky = Student.query.get(Msv) #query : truy vấn

    db.session.delete(dangky)

    db.session.commit()

    return render_template("dangkythanhcong.html")


#xóa thông tin giảng viên
@app.route('/delete2')  
def delete2():
    
    Mgv = request.args.get("MGV")
    teacher = Teacher.query.get(Mgv)

    db.session.delete(teacher)
    db.session.commit()

    return render_template("dangkythanhcong.html") 

 #xóa môn học
@app.route('/delete3') 
def delete3():

    MaMH = request.args.get("MaMH")
    mamh = Subjectname.query.get(MaMH)
    db.session.delete(mamh)
    db.session.commit()

    return render_template("dangkythanhcong.html")


#xóa thông tin sinh viên đăng ký môn học
@app.route('/delete4')  
def delete4():

    Msv = request.args.get("Msv")
    masv = Dangkymh.query.get(Msv)
    db.session.delete(masv)
    db.session.commit()


    return render_template("dangkythanhcong.html") 


#---------------------------------------------
# Chức Năng Update
@app.route('/update')
def update():

    return render_template("update.html")     

#Update thông tin sinh viên
@app.route('/update1')  
def update1():
    
    Name =  request.args.get("Name")
    Msv  = request.args.get("Msv")
    Birth =  request.args.get("Birth")
    Phone  =  request.args.get("Phone")
    Class =  request.args.get("Class")
     

    student = Student.query.get(Msv)
    student.Name = Name
    student.Birth = Birth
    student.Class = Class
    student.Phone = Phone
    
    db.session.commit()
    return render_template('dangkythanhcong.html') 

#Update thông tin môn học
@app.route('/update2')  
def update2():
    
    Name = request.args.get("NameMH")
    MaMH = request.args.get("MaMH")
    SoTin = request.args.get("SoTin")
    GiangVien = request.args.get("GiangVien")
    Time = request.args.get("Time")
     

    subject = Subjectname.query.get(MaMH)
    subject.NameMH = Name
    subject.SoTin = SoTin
    subject.GiangVien = GiangVien
    subject.Time = Time 
    
    db.session.commit()
    return render_template('dangkythanhcong.html')


#update thông tin giảng viên
@app.route('/update3')
def update3():
    
    Mgv = request.args.get('MGV')
    NameGV = request.args.get('NameGV')
    Class = request.args.get('Class')
    Phone = request.args.get('Phone')
    Address = request.args.get('Address')

    teacher = Teacher.query.get(Mgv)
    teacher.NameGV = NameGV
    teacher.Class = Class
    teacher.Phone = Phone
    teacher.Address = Address
    db.session.commit()
    return render_template('dangkythanhcong.html')


#update thông tin sinh viên đăng ký môn
@app.route('/update4') 
def update4():

    Msv = request.args.get("Msv")
    NameSV = request.args.get("NameSV") 
    NameMH = request.args.get("NameMH")
    Birth = request.args.get("Birth")
    Class = request.args.get("Class")

    dangky = Dangkymh.query.get(Msv)
    dangky.NameSV = NameSV
    dangky.NameMH = NameMH
    dangky.Birth = Birth
    dangky.Class = Class


    db.session.commit()
    return render_template('dangkythanhcong.html')


#---------------------------------------------
#Chức năng tìm kiếm 
@app.route('/filter')
def filter():

    return render_template("filter.html")  

#Tìm kiếm thông tin sinh viên
@app.route('/filter2')  
def filter2():

    student = Student.query.all()

    return render_template("filter2.html", Student=student)

#tìm kiếm thông tin giảng viên
@app.route('/filter3')  
def filter3():

    teacher = Teacher.query.all()
    
    return render_template("filter2.html", Teacher=teacher)  

#tìm kiếm thông tin môn học
@app.route('/filter4')  
def filter4():

    subject = Subjectname.query.all()                                       
    
    return render_template("filter2.html",Subjectname=subject)

#tìm kiếm thông tin sinh viên đăng ký môn học
@app.route('/filter5')  
def filter5():

    dangkymh = Dangkymh.query.all()                                       
    
    return render_template("filter2.html",Dangkymh=dangkymh)
 