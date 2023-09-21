import time
import win32com.client as comctl
import os

print('начну через 5с')

print('ВАЖНО!!!!\nЕсли текст на русском но переключи раскалдку на русский, если англ то на английскую!')

time.sleep(4)


wsh = comctl.Dispatch("WScript.Shell")

print('spamming')

for i in range(1000):
    time.sleep(0.8)
    wsh.SendKeys('ТУТ ТЕКСТ')
    time.sleep(0.8)
    wsh.SendKeys("{enter}")