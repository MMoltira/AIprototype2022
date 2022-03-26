# Create Azure Resource Group
    1. ลงชื่อเข้าใช้ Azure portal
    2. กดเลือก Resource groups และกด Add ดังรูป    
![image](https://user-images.githubusercontent.com/68935366/160231557-9282cb8c-d346-4862-8c88-f9b649306523.png)
    
    3. กด Add > ตรวจสอบ Subscription > กรอกชื่อ Resource Group > เลือก Region Southeast Asia (เพราะว่าอยู่ใกล้ไทยที่สุด) > เสร็จแล้วก็กดตกลง 
![1_icMm_w8DknSczegkmh-jrg](https://user-images.githubusercontent.com/68935366/160231716-0ac61cba-d5a4-4575-8229-cb24073e172d.png)

# Create Virtual Machine
    4. เมื่อสร้าง Resource Group เสร็จแล้ว ก็เริ่มสร้าง VM เริ่มแรกให้เข้าไปที่ Virtual machines page ก่อน
 ![1_W9xvM-xXfEoKpG49LNJEhg](https://user-images.githubusercontent.com/68935366/160231879-22f633ca-1433-469b-a52d-510d6816bfcc.png)
    
    5. ในขั้นตอนถัดมาเขาก็จะถามรายละเอียดของ VM ของเรา ซึ่งในส่วนนี้ก็ค่อยๆเลือกใส่ทีละอันเลย แล้วพอใส่เสร็จก็กดปุ่ม Review and create
      * Virtual machine name คือ ชื่อ VM ที่จะสร้าง
      * Region คือ ตัว VM นี้จะตั้งอยู่โซนไหน ถ้าไทยก็จะเลือก Region Southeast Asia
      * Username คือ ชื่อ username สำหรับ login เข้าเครื่อง
      * Password คือ รหัสผ่านสำหรับ Login เข้าเครื่อง ตอนกำหนดต้องมี ตัวอักษรตัวเล็ก ตัวอักษรตัวใหญ่ และตัวเลขด้วย
      * Size คือ คือขนาดความแรงของ VM สามารถเลือกดูได้ครับ ซึ่งเขาจะบอกราคาไว้ในนั้นเลยว่าจะเก็บเงินเราตอนสิ้นเดือนกี่บาท
   ![image](https://user-images.githubusercontent.com/68935366/160232153-ef8b4e9d-c012-4b72-8f38-b7eda238a564.png)
   
     6. กด Review + create ก็ถือว่าสร้าง VM เสร็จแล้ว
