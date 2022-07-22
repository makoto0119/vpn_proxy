from telnetlib import theNULL
from turtle import end_fill
import webbrowser
import time
import pyautogui as pag

# proxy を解除
webbrowser.open('ms-settings:network-proxy')
time.sleep(3) #描画を待つ

p = pag.locateOnScreen(r'c:\Users\10001231983\Documents\VPN\proxy_on.png')
if p: 
    x, y = pag.center(p)
    print(p)
    pag.click(x, y) 

#    pag.press('tab',presses=2)
#    pag.press('space')

# vpn 開始
webbrowser.open('ms-settings:network-vpn')
time.sleep(2) #描画を待つ
pag.press('tab')
pag.press('space')
pag.press('tab')
pag.press('space')

time.sleep(5) #VPN の再接続を待つ

# proxy を戻す
webbrowser.open('ms-settings:network-proxy')
time.sleep(1) #描画を待つ

pag.press("tab", presses=2)
pag.press("space")
pag.press("tab", presses=5)
pag.press("space")

time.sleep(3) #画面確認時間
pag.hotkey('alt', 'f4')

print('end')