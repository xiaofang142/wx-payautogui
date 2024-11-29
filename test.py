import pyautogui
import time


def Open_Wechat():
    #使用快捷键打开微信。这个微信的默认设置的快捷键。
    pyautogui.hotkey('ctrl', 'alt', 'w')
    time.sleep(1)

def Chat_Who(ContactPerson):
    #使用快捷键打开查找，找一个叫Tom的联系人。
    pyautogui.hotkey("ctrl","f")
    pyautogui.write(ContactPerson)
    time.sleep(1)
    pyautogui.hotkey('Enter')
    time.sleep(1)

def Sent_Msg(Msg):
    #给Tom发消息，然后回车发送。
    pyautogui.write(Msg)
    pyautogui.hotkey('Enter')

if __name__ == '__main__':
    Open_Wechat()
    ContactPerson = "文件传输助手"
    Chat_Who(ContactPerson)
    msg = "hello,thank you."
    Sent_Msg(msg)