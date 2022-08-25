""" windows10 の proxy を off にして VPN を繋ぎ、proxy を on に戻す ver1.0  """
import webbrowser
import time
import pyautogui as pag
import os
import ctypes

# 指定したウィンドウ名の範囲を取得
def GetWindowRectFromName(TargetWindowTitle:str)-> tuple:
    TargetWindowHandle = ctypes.windll.user32.FindWindowW(0, TargetWindowTitle)
    Rectangle = ctypes.wintypes.RECT()
    ctypes.windll.user32.GetWindowRect(TargetWindowHandle, ctypes.pointer(Rectangle))
    return (Rectangle.left, Rectangle.top, Rectangle.right, Rectangle.bottom)

# proxy を解除
webbrowser.open('ms-settings:network-proxy')

# 範囲指定
target_range = (GetWindowRectFromName('設定'))
time.sleep(3) #描画を待つ

p = pag.locateOnScreen(os.path.dirname(__file__)+'\proxy_on.png',
 confidence=.7, region=target_range)
#grayscale=True,

if p: 
    x, y = pag.center(p)
    print(p)
    pag.click(x, y) 

# vpn 開始
webbrowser.open('ms-settings:network-vpn')
time.sleep(2) #描画を待つ
pag.press('tab')
pag.press('space')
pag.press('tab')
pag.press('space')
pag.alert(text='VPN が接続出来たらクリック', button='OK') #VPN の再接続を待つ

# proxy を戻す
webbrowser.open('ms-settings:network-proxy')
time.sleep(1) #描画を待つ

pag.press("tab", presses=2)
pag.press("space")
pag.press("tab", presses=5)
pag.press("space")
# time.sleep(1) #画面確認時間
pag.hotkey('alt', 'f4')