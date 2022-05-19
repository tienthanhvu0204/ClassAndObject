class Student:
    def __init__(self, mssv = "none", hoVaTen = "none", ngaySinh = "none", queQuan = "none", chuyenNganh = "none", lop = "none"):
        self.mssv = mssv
        self.hoVaTen = hoVaTen
        self.ngaySinh = ngaySinh
        self.queQuan = queQuan
        self.chuyenNganh = chuyenNganh
        self.lop = lop
    
    def thongtin (self):
        return ["MSSV: {}, Họ và tên: {}, Ngày sinh: {}, Quê quán: {}, Chuyên ngành: {}, Lớp: {}".format \
            (self.mssv, self.hoVaTen, self.ngaySinh, self.queQuan, self.chuyenNganh, self.lop)]
class StudentList:
    def __init__(self, studentList = []):
        self.list = studentList
    
    def show (self):
        for student in self.list:
            print (student.thongtin ())
        return
        
    def add (self, students = []):
        self.list += (students)
        return

    def update (self, mssv, newInfor):
        for i in range (len(self.list)):
            if self.list[i].mssv == mssv:
                self.list[i] = newInfor
                break
        return

    def deleteStudent (self, mssv):
        for student in self.list:
            if student.mssv == mssv:
                self.list.remove (student)
                break

    def search (self, mssv):
        for student in self.list:
            if student.mssv == mssv:
                print (student.thongtin ())
                break
    
    def sort (self, reverse = 0):
        __doc__ = "reverse = 0, sắp theo thứ tự MSSV tăng dần, reverse = -1 sắp theo thứ tự MSSV giảm dần."
        if reverse == 0:
            for i in range (len(self.list)):
                for j in range (len(self.list) - i - 1):
                    if self.list[j].mssv > self.list[j+1].mssv:
                        x = self.list[j]
                        self.list[j] = self.list[j+1]
                        self.list[j+1] = x
        elif reverse == -1:
            for i in range (len(self.list)):
                for j in range (len(self.list) - i - 1):
                    if self.list[j].mssv < self.list[j+1].mssv:
                        x = self.list[j]
                        self.list[j] = self.list[j+1]
                        self.list[j+1] = x
        else:
            return print ("ERROR")

thanh = Student (2008298, "Vu Tien Thanh", "01/03/1990", "Dong Nai")
thuy = Student (2008300, "Tran Thanh Thuy", "17/02/1990", "Nha Trang")
thao = Student (2008198, "Nguyen Phuong Thao", "14/07/1990", "Da Lat")
tuan = Student (2008327, "Lai Duy Tuan", "29/11/1989", "Lam Dong")

danhsachlop = StudentList ()

danhsachlop.add ([thanh])
danhsachlop.add ([thuy, thao])
danhsachlop.show ()
danhsachlop.update (2008298, tuan)
print ()
danhsachlop.show ()
danhsachlop.sort ()
print ()
danhsachlop.show ()
print ()
danhsachlop.deleteStudent(2008327)
print ()
danhsachlop.show ()
print ()
danhsachlop.search(2008300)

