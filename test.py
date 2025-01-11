#TODO: Lớp Khóa học và Học viên
#Khóa học
class KhoaHoc:
    #Phương thức khởi tạo
    def __init__(self, maKH, tenKH, hinhThuc, hocPhi):
        self.maKH = maKH
        self.tenKH = tenKH
        self.hinhThuc = hinhThuc
        self.hocPhi = hocPhi
        
    #Thông tin chi tiết khóa học
    def thongtinKhoaHoc(self):
        KH.append({
            "maKH" : self.maKH,
            "tenKH" : self.tenKH,
            "hinhThuc" : self.hinhThuc,
            "hocPhi" : self.hocPhi,
        })
        
   
        
    
#Học viên
class HocVien:
    #Phương thức khởi tạo
    def __init__(self, maHV, tenHV, ngaySinh):
        self.maHV = maHV
        self.tenHV = tenHV
        self.ngaySinh = ngaySinh
        self.khoaHoc = []
        
    #Đăng kí khóa học
    def dangKiKhoaHoc(self, ma):
        self.khoaHoc.append(ma)
        print(f"Học viên {self.tenHV} đã đăng kí khóa học", ma)
        
    def hienthiKhoaHoc(self):
        print(f"Học viên {self.tenHV} đã đăng kí các khóa:")
        for item in self.khoaHoc:
            print(item)
    
        

#TODO: CÁC KHÓA HỌC CỦA TRUNG TÂM ĐÀO TẠO
KH = [] #List lưu trữ thông tin các khóa học của trung tâm đào tạo
print("\n")
print("*** THÔNG TIN CÁC KHÓA HỌC ONLINE ***")
'''KHÓA HỌC TOÁN ONLINE'''
khoaHoc1 = KhoaHoc("T", "Toán", "Online", 200)
khoaHoc1.thongtinKhoaHoc()

'''KHÓA HỌC VĂN ONLINE'''
khoaHoc2 = KhoaHoc("V", "Văn", "Online", 150)
khoaHoc2.thongtinKhoaHoc()

'''KHÓA HỌC ANH ONLINE'''
khoaHoc3 = KhoaHoc("A", "Anh", "Online", 750)
khoaHoc3.thongtinKhoaHoc()

'''KHÓA HỌC LÝ ONLINE'''
khoaHoc4 = KhoaHoc("L", "Lý", "Online", 340)
khoaHoc4.thongtinKhoaHoc()
def hienthiKhoaHoc():
    for item in KH:
        print(f"""-------------------------------
Mã khóa học: {item["maKH"]}
Tên khóa học: {item["tenKH"]}
Hình thức: {item["hinhThuc"]}
Học phí: {item["hocPhi"]}""")
        
hienthiKhoaHoc() 

#TODO:CÁC HỌC VIÊN ĐÃ ĐĂNG KÍ KHÓA HỌC CỦA TRUNG TÂM

#Thông tin sinh viên
hocVien1 = HocVien(1, "Đỗ Hồng Nhất", "15/7/2005")
hocVien2 = HocVien(2, "Phạm Xuân Long", "12/12/2005")
hocVien3 = HocVien(3, "Huỳnh Trung Tá", "4/5/2005")
hocVien4 = HocVien(4, "Nguyễn Duy Tiến", "2/3/2005")

#Đăng kí khóa học
print("\n")
print("*** CÁC KHÓA HỌC ĐÃ ĐĂNG KÍ ***")
hocVien1.dangKiKhoaHoc("Lý")
hocVien2.dangKiKhoaHoc("Toán")
hocVien3.dangKiKhoaHoc("Anh")
hocVien4.dangKiKhoaHoc("Văn")
hocVien1.dangKiKhoaHoc("Toán")
hocVien3.dangKiKhoaHoc("Lý")

#Hiển thị danh sách các khóa học đã đăng kí
print("\n")
print("*** DANH SÁCH CÁC KHÓA HỌC ĐÃ ĐĂNG KÍ ***")
hocVien1.hienthiKhoaHoc()
hocVien2.hienthiKhoaHoc()
hocVien3.hienthiKhoaHoc()
hocVien4.hienthiKhoaHoc()

