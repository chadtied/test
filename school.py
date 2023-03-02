from pynput.keyboard import Controller
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

google_map= "https://www.google.com.tw/maps/@23.546162,120.6402133,8z?hl=zh-TW"
address= "https://www.gstatic.com/images/icons/material/system_gm/2x/place_gm_blue_24dp.png"
phone= "https://www.gstatic.com/images/icons/material/system_gm/2x/phone_gm_blue_24dp.png"
web= "https://www.gstatic.com/images/icons/material/system_gm/2x/public_gm_blue_24dp.png"
workbook= openpyxl.load_workbook('C:/Users/user/Desktop/project/information.xlsx')
workpage1= workbook["工作表1"]
key_shift= Key.shift
keyboard= Controller()
driver= uc.Chrome(use_subprocess= True)
driver.get(google_map)

WebDriverWait(driver,20,0.5).until(EC.presence_of_element_located((By.ID,"searchboxinput")))
searchbox= driver.find_element(By.ID,"searchboxinput")
searchbutton= driver.find_element(By.ID,"searchbox-searchbutton")
searchbox.send_keys("台中補習班")
driver.execute_script("arguments[0].click();", searchbutton)

def screen_open():
    keyboard.press(key_shift)
    keyboard.release(key_shift) 

def find_sample():
    try:
        WebDriverWait(driver,30,0.5).until(EC.presence_of_element_located((By.CLASS_NAME,"hfpxzc")))
        pre_flag= -1
        cur_flag= 0
        while cur_flag!= pre_flag:
            pre_flag= cur_flag
            sample= driver.find_elements(By.CLASS_NAME, "hfpxzc")
            cur_flag= len(sample)
            driver.execute_script("arguments[0].scrollIntoView();",sample[-1])
            screen_open()
            time.sleep(8)
        return sample
    except:
        print("can't get any information")
        return -1

def input_data(data,title_name,count):
    print("data"+str(count+1)+" is operating")
    workpage1.cell(count+2,1).value= title_name
            
    for i in range(0,len(data)):
        try:
            img= data[i].find_element(By.CSS_SELECTOR, "div.cXHGnc > div > img").get_attribute('src')
        except:
            print("no data")
        
        try:
            if(img== address):
                #print("address:"+ data[i].text)
                workpage1.cell(count+2,3).value= data[i].text
            elif(img== web):
                #print("web:"+ data[i].text)
                workpage1.cell(count+2,5).value= data[i].text
            elif(img== phone):
                #print("phone:"+ data[i].text)
                workpage1.cell(count+2,7).value= data[i].text
        except:
            print("data not find")
    
def find_idividual(sample):
    try:
        for count in range(0,len(sample)):
            driver.execute_script("arguments[0].click();", sample[count])
            screen_open()
            time.sleep(10)
            
            data= driver.find_elements(By.CLASS_NAME,"AeaXub")
            title= driver.find_element(By.CLASS_NAME,"tAiQdd")
            title_name= title.find_element(By.CSS_SELECTOR,"div.lMbq3e > div:nth-child(1) > h1").text
            input_data(data,title_name,count)
    except:
        print("Can't find any information")

    
    
#main function
sample= find_sample()
if sample!= -1:
    find_idividual(sample)
    
    workbook.save('C:/Users/user/Desktop/project/new.xlsx')
else:
    print("Wrong message!!!")


input()
