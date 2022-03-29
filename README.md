# AIprototype2022
## 👋นางสาวมลทิรา ใสสอน รหัส 613021019-9 สาขา สารสนเทศสถิติ

![275666165_506370131193071_3775731654175991787_n](https://user-images.githubusercontent.com/68935366/160226528-125e8694-467d-41fd-b894-dc23dce8fdf5.jpg)

# ➡️หัวข้อที่ 1 connecting to cloud เอกสารเพิ่มเติม [link](https://drive.google.com/file/d/14WDdcWNg2xRYRtL8WE59jri3pBFFtLGn/view?usp=sharing)

![275895070_776752703304529_2890577421474138222_n](https://user-images.githubusercontent.com/68935366/160229116-2e9b521d-7d16-4957-9604-f97224da1615.jpg)
  * ## การสมัครใช้งาน Azuer
    * สำหรับนักศึกษามหาวิทยาลัยขอนแก่น สามารถสมัครได้โดย [link](https://drive.google.com/file/d/14WDdcWNg2xRYRtL8WE59jri3pBFFtLGn/view?usp=sharing)
    * สำหรับผู้ที่อยากสมัครด้วยตยเอง สามารถสมัครได้โดย [link](https://patiwat.medium.com/%E0%B8%A7%E0%B8%B4%E0%B8%98%E0%B8%B5%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%A1%E0%B8%B1%E0%B8%84%E0%B8%A3-azure-account-free-trial-ea074faa40af)

  * ## สรุป การใช้ Cloud มีทั้งข้อดีและข้อควรระวัง ดังนี้
    * ### ประโยชน์
          1. เรื่องราคา เราสามารถทดลองใช้ทุกอย่างในราคาที่ไม่แพง
          2. ทำงานได้เร็วขึ้น
          3. มีกฎข้อบังคับที่ครอบคลุม ทำให้ผู้ใช้มีความสะดวกในการเข้าใช้งาน
          4. มีความปลอดภัยสูง
          5. สามารถทำงานทุกอย่างได้บน Browser
    * ### ข้อควรระวัง
          1. เป็นเทคโนโลยีที่ใหม่ ทำให้มีการอัพเดทอยู่เรื่อย ๆ จึงทำให้ผู้ใช้ต้องอัพเดตตามอยู่ตลอด
          2. ต้องมีอินเตอร์เน็ต
          3. ทำให้มีความเข้าใจยากในคนที่ยังคนกับคอมฯรุ่นเก่า ๆ
          4. ทุกอย่างอยู่บนอินเทอร์เน็ต หากข้องมูลสูญหายอาจจะตามคืนได้ยาก ถ้าเราให้บริการของเขาฟรี

# ➡️หัวข้อที่ 2 Cloud VM (Virtual Machine) เนื้อหา [link](https://github.com/MMoltira/AIprototype2022/blob/main/Create%20Azure.md)
![276052704_1227234431159256_7858411414632815275_n](https://user-images.githubusercontent.com/68935366/160234243-62e1bf63-1d65-47b0-8918-6ea3aec96ef9.jpg)
## Create Azure
  * ### ลงชื่อเข้าใช้ Azure portal
  * ### กดเลือก Resource groups
  * ### กด Add > ตรวจสอบ Subscription > กรอกชื่อ Resource Group > เลือก Region Southeast Asia (เพราะว่าอยู่ใกล้ไทยที่สุด) > เสร็จแล้วก็กดตกลง
  * ### เมื่อสร้าง Resource Group เสร็จแล้ว ก็เริ่มสร้าง VM เริ่มแรกให้เข้าไปที่ Virtual machines page ก่อน
  * ### ในขั้นตอนถัดมาเขาก็จะถามรายละเอียดของ VM ของเรา ซึ่งในส่วนนี้ก็ค่อยๆเลือกใส่ทีละอันเลย แล้วพอใส่เสร็จก็กดปุ่ม Review and create
       * Virtual machine name คือ ชื่อ VM ที่จะสร้าง
       * Region คือ ตัว VM นี้จะตั้งอยู่โซนไหน ถ้าไทยก็จะเลือก Region Southeast Asia
       * Username คือ ชื่อ username สำหรับ login เข้าเครื่อง
       * Password คือ รหัสผ่านสำหรับ Login เข้าเครื่อง ตอนกำหนดต้องมี ตัวอักษรตัวเล็ก ตัวอักษรตัวใหญ่ และตัวเลขด้วย
       * Size คือ คือขนาดความแรงของ VM สามารถเลือกดูได้ครับ ซึ่งเขาจะบอกราคาไว้ในนั้นเลยว่าจะเก็บเงินเราตอนสิ้นเดือนกี่บาท
  * ### กด Review + create ก็ถือว่าสร้าง VM เสร็จแล้ว
## ติดตั้ง UBUNTU
   * ### wsl --install เพื่อติดตั้งบน power shell
   * ### เมื่อ install ได้แล้ว ก็จะขึ้นให้ใส่ Username กับ Password เราสามารถสร้างขึ้นใหม่ได้
   * ### connect ด้วย IP Address ที่สร้างไว้บน VM โดยใช้ ssh เป็นตัวเชื่อมไปยังคอมฯ อีกเครื่อง

## คำสั่งต่าง ๆ ที่ใช้บ่อย ๆ
   * พิมพ์คำสั่ง ls เพื่อแสดงข้อมูลภายใน directory
   * พิมพ์คำสั่ง ls -l เพื่อดูลิสภายใน ls ว่าใครสามารถเข้าถึงได้บ้าง
   * พิมพ์คำสั่ง ls -lh ดูขนาดของไฟล์
   * พิมพ์คำสั่ง ls -lt ดูไฟล์เรียงจากใหม่ไปเก่า ls -ltr ดูไฟล์เรียงจากเก่าไปใหม่
   * พิมพ์คำสั่ง cd เพื่อแสดง Current Directory
   * พิมพ์คำสั่ง cd ตามด้วย Path จะเปลี่ยน Directory ปัจจุบันไปยัง Path นั้น
   * พิมพ์คำสั่ง cd .. จะย้อน Directory กลับขึ้นไปหนึ่งขั้น
   * พิมพ์คำสั่ง cd \ จะท าให้กลับสู่ Root Directory
   * พิมพ์คำสั่ง pwd คำสั่งแสดง directory หรือ path ที่อยู่ปัจจุบัน อยูที่ตรงไหน
   * พิมพ์คำสั่ง clear จะทำการเคลียหน้าจอ
   * พิมพ์คำสั่ง mkdir ตามด้วยชื่อ Directory (หรือชื่อ Folder อย่างที่เราคุ้นเคยกัน) จะเป็นการสร้าง Directory ใหม่ขึ้นมา
   * พิมพ์คำสั่ง dir เพื่อแสดงรายละเอียด File และ Directory ที่มีอยู่ใน Path ปัจจุบัน
   * พิมพ์คำสั่ง rm คือ ลบไฟล์ที่อยากจะลบ rm -r คือลบไฟล์ทั้งหมดออกไป
* ## SCP ตามด้วยที่อยู่ต้นทาง ตามด้วยที่อยู่ปลายทาง คือวิธีส่งไฟล์จากเครื่องตัวเองไปยังเครื่องอื่น
   * ส่งไฟล์จากเครื่องเรา เช่น SCP .xxx.jpg(ที่อยู่ของเครื่อง)---> user@ip(ที่อยู่Address) :/xxx/xxx/ (ที่อยู่ในเครื่องปลายทาง)
   * ดึงไฟล์จาก VM เช่น SCP user@ip(ที่อยู่Address) :/xxx/xxx/ (ที่อยู่ในเครื่องปลายทาง) ---> โฟลเดอร์ที่เราต้องการ
* ## screen คือการสร้างหน้าบางอย่างขึ้นมาลอย ๆ ไม่ต้องไป connect กับใคร
   * พิมพ์คำสั่ง screen -S tscreen(ตั้งชื่ออะไรก็ได้) เพื่อสร้าง session ในหน้า screen
   * พิมพ์คำสั่ง screen -R คือ ย้อนกลับไปในหน้า screen นั้น ๆ
   * กดแปป้นพิมพ์ ctrl+A ยกนิ้วขึ้นแล้ว กด D เพื่อออกจากหน้า screen
   * พิมพ์คำสั่ง screen -R tscreen(ชื่อที่ตั้งไว้) คือกลับเข้าไปใน screen ที่สร้างไว้
* ## ติดตั้ง miniconda จาก  [link](https://docs.conda.io/en/latest/miniconda.html)
   * ติดตั้งแพ็คเกจต่าง ๆ ผ่าน conda install
   * การสร้าง virtual environment เพื่อไม่ให้รบกวนคนอื่น ป้องกันงานหาย
         
         * สามารถพิมพ์ python เพื่อดูเวอร์ชันที่ใช้ได้ และพิมพ์ exit() เพื่อออกมายังหน้าเดิม
         * พิมพ์ conda create -n testpy3.7(ตั้งชื่อ) python=3.7(เวอร์ชั่นที่ต้องการ)  เป็นคำสั่งในการเริ่มสร้าง environment โดยต้องการใช้ python เวอร์ชัน 3.7
         * พิมพ์ conda activate testpy3.7(ชื่อที่ตั้งไว้) ถ้าสร้าสำเร็จมันจะขึ้นชื่อ testpy3.7 ข้างหน้า ดังรูป
        
        ![image](https://user-images.githubusercontent.com/68935366/160260909-c00e9c93-f9b3-4d3c-8ac8-bfe5fca716f6.png)
         
         * พิมพ์ pip install pandas เพื่อติดตั้งแพ็ตเกจต่าง ๆ ของ pandas
         * พิมพ์ conda install jupyter เพื่อดาวน์โหลดโค้ดที่ถูกคอมไพล์ไว้แล้ว รวมถึงแพ็คเกจอื่น ๆ ที่จำเป็นในการใช้ jupyter
         * พิพม์ conda deactivate เมื่อใช้งานแล้วเราอยากไปที่อื่นก็สามารถพิมพ์คำสั่งดังกล่าวได้
         * พิมพ์ conda info --envs เพื่อดูว่ามี virtual environment อะไรบ้าง

# ➡️หัวข้อที่ 3 Custom vision AI ML

# ➡️หัวข้อที่ 4  Python (Subprocess, OS, python.py)
  ## ใช้ Visual Studio Code ในการสร้างโค้ด 
  * python script จะคล้าย ๆ กับการเขียนสคริปท์ในภาษาอื่น เช่น ภาษาซี
  * จะมี main function ที่จะถูกรันก่อนใน python
  * argparse คือ ตัวที่กำหนดว่าตัวโปรแกรมเราสามารถรับ input ตอนสั่ง command line ภายนอกได้ [code](https://github.com/MMoltira/AIprototype2022/blob/main/python2.py)
  * subprocess คือ สำหรับรัน terminal command [code](https://github.com/MMoltira/AIprototype2022/blob/main/testsub.py)


# ➡️หัวข้อที่ 5 Git
  * ## การ setup git ครั้งแรก สำหรับคนที่ไม่เคยset git บน command line
       * พิมพ์คำสั่ง $ git config --global user.name "Moltira" คือการตั้งชื่อบน command line เพื่อให้ใช้งานบนกิตฮับได้สะดวก
       * พิมพ์คำสั่ง $ git config --global user.email Moltira@example.com คือการตั้งชื่ออีเมล์บน command line
  * ## คำสั่ง git ที่ต้องรู้
       * git clone (ตามด้วยที่อยู่ URL ของ git นั้น) คือการ clone กิตฮับของคนอื่นมาหรืองานที่เราต้องการแก้ไขต่อ เรียกอีกอย่างว่า การfork
       * git status คือ ดูว่าไฟล์ไหนที่ถูกแก้ไขไปจากต้นทางที่ clone มา
       * git add คือ การเพิ่มไฟล์ที่เราแก้ไปแล้ว หรือไฟล์ที่ต้องการอัพขึ้นไปบนกิตฮับ
       * git commit -m "(ใส่คอมเม้น)" คือ การใส่คอมเม้นหรือรายละเอียดที่เราแก้ไขไป
       * git push คือ การอัพโหลดไฟล์ที่เราแก้ไปบนกิต
       * git pull คือ เกิดขึ้นเมื่อทำงานร่วมกับคนอื่น มันจะดึงเวอร์ชันล่าสุดที่อีกคนแก้แล้วให้เห็นแล้วเราสามารถแก้ไขต่อได้โดยไม่ชนกัน


# ➡️หัวข้อที่ 6 Google colab

# ➡️หัวข้อที่ 7 API --> Flask
flask สำหรับทำเว็บแอปและเว็บเซอวิส API

# ➡️หัวข้อที่ 8 Tensorflow -Pytorch

# ➡️หัวข้อที่ 9 Latex Overleaf



   



### Connect with me:

[<img align="left" alt="Sass" width="100px" src="https://img.icons8.com/bubbles/100/000000/facebook-new.png" style="padding-right:10px;" />](https://www.facebook.com/moltira.sison)
[<img align="left" alt="Sass" width="100px" src="https://img.icons8.com/bubbles/200/000000/line-me.png" style="padding-right:10px;" />](https://line.me/ti/p/N-ql2XrDk1)


