# python 3.6.8(32-bit) pywinauto 0.5.4 Windows
# oj13@foxmail.com
# automation for testing Lanschool Teacher Console 8.0.1.54

from pywinauto.application import Application
from pywinauto import taskbar, findwindows
from time import sleep

# start the program
# app = Application().start("C:\\Program Files (x86)\\LanSchool\\teacher.exe")

# or, connect to existing program
app = Application().connect(title='LanSchool Teacher Console')

# invoke from systray(taskbar)
# print (taskbar.RunningApplications.Texts())
# taskbar.ClickSystemTrayIcon("LanSchool Teacher Console")
# systrayicons.ClickSystemTrayIcon("CDL")
# systrayicons.Button('test').ClickInput()

lskmainteacherwindowclass = app[u'LanSchool Teacher Console']
# lskmainteacherwindowclass.Restore()
lskmainteacherwindowclass.SetFocus()
lskmainteacherwindowclass.Maximize()

# Close any dialog

# if app.dialog:
# 	app.dialog.Close()
# 	sleep(1)

# ______________________________________________________________________

toolbarwindow = lskmainteacherwindowclass['ToolBar']

# Toolbar - Show
print("Show..")
toolbar_button = toolbarwindow.Button(2)
toolbar_button.ClickInput()
sleep(1)
window = app.Dialog
window.SetFocus()
app.Dialog.Restore()
button = window.CheckBox
button.ClickInput()
sleep(1)
button.ClickInput()
sleep(1)
button2 = window.CheckBox5
button2.ClickInput()
window2 = app.DrawOnScreen
sleep(2)

# Letter - L
window2.PressMouseInput(coords=(1130, 700))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1130, 800))
sleep(0.1)
window2.PressMouseInput(coords=(1130, 800))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1180, 800))
sleep(0.1)

# Letter - S
window2.PressMouseInput(coords=(1330, 700))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1280, 700))
sleep(0.1)
window2.PressMouseInput(coords=(1280,700))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1280, 750))
sleep(0.1)
window2.PressMouseInput(coords=(1280, 750))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1330, 750))
sleep(0.1)
window2.PressMouseInput(coords=(1330, 750))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1330, 800))
sleep(0.1)
window2.PressMouseInput(coords=(1330, 800))
sleep(0.1)
window2.ReleaseMouseInput(coords=(1280, 800))
sleep(0.1)

app.DrawOnScreen.Button.ClickInput()

sleep(2)
app.Dialog.Stop.ClickInput()
sleep(1)
lskmainteacherwindowclass = app[u'LanSchool Teacher Console']
# lskmainteacherwindowclass.Restore()
lskmainteacherwindowclass.SetFocus()
lskmainteacherwindowclass.Maximize()
sleep(2)
print("pass!\n")

# Toolbar - Show Student (First in the list)
# select first client
print("show students..")
lskmainteacherwindowclass.ClickInput(coords=(160,335))
toolbar_button = toolbarwindow.Button(u'Show Student')
toolbar_button.ClickInput()
sleep(3)
toolbar_button.ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Vote
print("Vote..")
toolbar_button = toolbarwindow.Button(5)
toolbar_button.ClickInput()
app.Dialog.Edit.TypeKeys('"Random question"', with_spaces = True)
sleep(2)
app.Dialog.Button6.ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Testing
print("testing..")
toolbar_button = toolbarwindow.Button(6)
toolbar_button.ClickInput()
# print(findwindows.find_windows(best_match="PopupMenu"))
# sleep(1)
# app.PopupMenu.MenuItem("Ask Students to Take Test...").ClickInput()
sleep(1)
app.Dialog.Load.ClickInput()
sleep(1)
app.Dialog.Edit.TypeKeys("Computers.lst", with_spaces = True)
sleep(1)
app.Dialog.Open.ClickInput()
sleep(1)
app.Dialog.Start.ClickInput()
sleep(1)
app.Dialog.Sotp.ClickInput()
sleep(1)
app.Dialog.ClickInput(coords=(1313, -20))
sleep(1)
print("pass!\n")

# Toolbar - Run
print("Run..")
toolbar_button = toolbarwindow.Button(8)
toolbar_button.ClickInput()
sleep(1)
app.Dialog.OK.ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Control
print("control..")
toolbar_button = toolbarwindow.Button(u'Control')
toolbar_button.ClickInput()
sleep(1)
lskmainteacherwindowclass.RightClickInput(coords=(765,962))
sleep(1)
lskmainteacherwindowclass.ClickInput(coords=(785,972))
sleep(1)
toolbar_button.ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Snapshot
print("snapshot..")
toolbar_button = toolbarwindow.Button(u'Snapshot')
toolbar_button.ClickInput()
sleep(1)
app.Dialog.Save.ClickInput()
print("pass!\n")

# Toolbar - Message
print("message..")
toolbar_button = toolbarwindow.Button(13)
toolbar_button.ClickInput()
sleep(1)
app.Dialog.Edit.TypeKeys("pay attention please!!", with_spaces = True)
sleep(2)
window = app.Dialog
button1 = window.CheckBox
button1.ClickInput()
sleep(0.5)
button2 = window.CheckBox2
button2.ClickInput()
sleep(1)
button = window[u'S&end']
button.ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Speak
print("speak..")
toolbar_button = toolbarwindow.Button(15)
toolbar_button.Click()
sleep(0.5)
toolbar_button.Click()
sleep(0.5)
print("pass!\n")

# Toolbar - Blank Screen
print("blank screen..")
toolbar_button = toolbarwindow.Button(17)
toolbar_button.Click()
sleep(0.5)
toolbar_button.Click()
sleep(0.5)
print("pass!\n")

# Toolbar - Limit Web
print("limit web..")
toolbar_button = toolbarwindow.Button(18)
toolbar_button.Click()
sleep(0.5)
toolbar_button.Click()
sleep(0.5)
print("pass!\n")

# Toolbar - Limit Apps
print("limit apps..")
toolbar_button = toolbarwindow.Button(19)
toolbar_button.Click()
sleep(0.5)
toolbar_button.Click()
sleep(0.5)
print("pass!\n")

# Toolbar - Limit Print
print("limit print..")
toolbar_button = toolbarwindow.Button(20)
toolbar_button.Click()
sleep(0.5)
toolbar_button.Click()
sleep(0.5)
print("pass!\n")

# Toolbar - Limit Drives
print("limit drives..")
toolbar_button = toolbarwindow.Button(21)
toolbar_button.Click()
sleep(1)
app.Dialog[u'&No'].ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Mute
print("mute..")
toolbar_button = toolbarwindow.Button(22)
toolbar_button.Click()
sleep(0.5)
toolbar_button.Click()
sleep(0.5)
print("pass!\n")

# Toolbar - Clear Desktop
print("clear Desktop..")
toolbar_button = toolbarwindow.Button(24)
toolbar_button.ClickInput()
sleep(1)
toolbar_button.ClickInput()
print("pass!\n")

# Toolbar - Show Video
print("show video..")
toolbar_button = toolbarwindow.Button(25)
toolbar_button.ClickInput()
sleep(1)
app.Dialog.CloseButton.ClickInput()
print("pass!\n")

# Toolbar - Class List
print("class list..")
toolbar_button = toolbarwindow.Button(27)
toolbar_button.ClickInput()
# app.PopupMenu.test.Click
# print(findwindows.find_windows(best_match="PopupMenu"))
sleep(1)
app.PopupMenu.MenuItem("Manage Class Lists...").ClickInput()
sleep(2)
app.Dialog.CloseButton.ClickInput()
sleep(1)
print("pass!\n")

# Toolbar - Files
print("files..")
toolbar_button = toolbarwindow.Button(29)
toolbar_button.ClickInput()
sleep(1)
app.Dialog.Button2.ClickInput()
sleep(1)
app.Open.Cancel.ClickInput()
sleep(1)
app.Dialog.Cancel.ClickInput()
sleep(1)
lskmainteacherwindowclass.ClickInput(coords=(160,335))
print("pass!\n")

print("all function in toolbar has been test\n")
#_________________________________________________
