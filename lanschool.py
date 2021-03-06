# python 3.6.8(32-bit) pywinauto 0.5.4 Windows
# oj13@foxmail.com
# automation for testing Lanschool Teacher Console 8.0.2.6

from pywinauto.application import Application
from pywinauto import taskbar, findwindows
import time
from time import sleep

# start the program
# app = Application().start("C:\\Program Files (x86)\\LanSchool\\teacher.exe")

# or, connect to existing program
app = Application().connect(title='LanSchool Teacher Console')
lskmainteacherwindowclass = app[u'LanSchool Teacher Console']
lskmainteacherwindowclass.Maximize()
toolbarwindow = lskmainteacherwindowclass['ToolBar']

# =====================================================

def Show(app, toolbarwindow):
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
def Show_Student(app, toolbarwindow, lskmainteacherwindowclass):
	print("show students..")
	lskmainteacherwindowclass.ClickInput(coords=(160,335)) # select first client
	toolbar_button = toolbarwindow.Button(u'Show Student')
	toolbar_button.ClickInput()
	sleep(3)
	app.Dialog.Stop.ClickInput()
	# toolbar_button.ClickInput()
	sleep(3)
	print("pass!\n")

# Toolbar - Vote
def Vote(app, toolbarwindow, lskmainteacherwindowclass):
	print("Vote..")
	toolbar_button = toolbarwindow.Button(5)
	toolbar_button.ClickInput()
	app.Dialog.Edit.TypeKeys('"Random question"', with_spaces = True)
	sleep(1)
	app.Dialog.Button2.ClickInput() # Save..
	sleep(1)
	app.Dialog.Edit.TypeKeys("vote " + str(time.time()))
	sleep(1)
	app.Dialog.Save.ClickInput()
	sleep(1)
	app.Dialog.Edit.SetText("")
	app.Dialog.Button0.ClickInput() # Load..
	sleep(1)
	app.Dialog.Edit.TypeKeys("question.lsq")
	app.Dialog.Open.ClickInput()
	sleep(1)
	app.Dialog.Button4.ClickInput() # Send
	sleep(3)
	app.Dialog.Button5.ClickInput() # Details..
	sleep(1)
	app.Dialog.Close() # not finish yet
	sleep(1)
	app.Dialog.Close()
	print("pass!\n")

# Toolbar - Run
def Run(app, toolbarwindow, lskmainteacherwindowclass):
	print("Run..")
	toolbar_button = toolbarwindow.Button(8)
	toolbar_button.ClickInput()
	sleep(1)
	app.Dialog.OK.ClickInput()
	sleep(1)
	print("pass!\n")

# Toolbar - Control
def Control(app, toolbarwindow, lskmainteacherwindowclass):
	print("control..")
	toolbar_button = toolbarwindow.Button(u'Control')
	toolbar_button.ClickInput()
	sleep(1)
	lskmainteacherwindowclass.RightClickInput(coords=(765,962)) # creat a folder on mac 
	sleep(1)
	lskmainteacherwindowclass.ClickInput(coords=(785,972))
	sleep(1)
	toolbar_button.ClickInput()
	sleep(1)
	print("pass!\n")

# Toolbar - Snapshot
def Snapshot(app, toolbarwindow, lskmainteacherwindowclass):
	print("snapshot..")
	toolbar_button = toolbarwindow.Button(u'Snapshot')
	toolbar_button.ClickInput()
	sleep(1)
	app.Dialog.Save.ClickInput()
	print("pass!\n")

# Toolbar - Message
def Message(app, toolbarwindow, lskmainteacherwindowclass):
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
def Speak(app, toolbarwindow, lskmainteacherwindowclass):
	print("speak..")
	toolbar_button = toolbarwindow.Button(15)
	toolbar_button.Click()
	sleep(0.5)
	toolbar_button.Click()
	sleep(0.5)
	print("pass!\n")

# Toolbar - Blank Screen
def Blank_Screen(app, toolbarwindow, lskmainteacherwindowclass):
	print("blank screen..")
	toolbar_button = toolbarwindow.Button(17)
	toolbar_button.Click()
	sleep(0.5)
	toolbar_button.Click()
	sleep(0.5)
	print("pass!\n")

# Toolbar - Limit Web
def Limit_Web(app, toolbarwindow, lskmainteacherwindowclass):
	print("Limit Web - Save/Load Allowed List")
	menu_item = lskmainteacherwindowclass.MenuItem(u'&Restrict->Configure Web Limiting...')
	menu_item.ClickInput()
	sleep(1)

	# allow list
	window = app.Dialog
	edit = window.Edit.SetText("")
	edit = window.Edit.TypeKeys("google.com\nbaidu.com", with_newlines=True)
	button = window.Button2 # save button
	button.ClickInput()
	sleep(1)
	window = app.Dialog
	edit = window.Edit.SetText(time.time()) 
	button3 = window.Button
	button3.ClickInput()
	sleep(1)
	window = app.Dialog
	edit = window.Edit.SetText("")
	window.Button.ClickInput()
	sleep(1)
	app.Dialog.Edit.TypeKeys("allow.lsu")
	app.Dialog.Open.ClickInput()
	sleep(1)

	# block list
	app.Dialog.RadioButton3.ClickInput()
	app.Dialog.Edit2.SetText("")
	app.Dialog.Edit2.TypeKeys("google.com\nbaidu.com", with_newlines=True)
	app.Dialog.Button4.ClickInput() # Save button
	sleep(1)
	app.Dialog.Edit2.SetText(time.time()) 
	app.Dialog.button3.ClickInput()
	sleep(1)
	window = app.Dialog
	app.Dialog.Edit2.SetText("")
	window.Button3.ClickInput()
	sleep(1)
	app.Dialog.Edit2.TypeKeys("block.lsu")
	app.Dialog.Open.ClickInput()
	sleep(1)
	app.Dialog.RadioButton2.ClickInput()
	sleep(1)
	app.Dialog.OK.ClickInput()

	print("pass!\n")

# Toolbar - Limit Apps
def Limit_Apps(app, toolbarwindow, lskmainteacherwindowclass):
	print("limit apps..")
	toolbar_button = toolbarwindow.Button(19)
	toolbar_button.Click()
	sleep(0.5)
	toolbar_button.Click()
	sleep(0.5)
	print("pass!\n")

# Toolbar - Limit Print
def Limit_Print(app, toolbarwindow, lskmainteacherwindowclass):
	print("limit print..")
	toolbar_button = toolbarwindow.Button(20)
	toolbar_button.Click()
	sleep(0.5)
	toolbar_button.Click()
	sleep(0.5)
	print("pass!\n")

# Toolbar - Limit Drives
def Limit_Drives(app, toolbarwindow, lskmainteacherwindowclass):
	print("limit drives..")
	toolbar_button = toolbarwindow.Button(21)
	toolbar_button.Click()
	sleep(1)
	app.Dialog[u'&No'].ClickInput()
	sleep(1)
	print("pass!\n")

# Toolbar - Mute
def Mute(app, toolbarwindow, lskmainteacherwindowclass):
	print("mute..")
	toolbar_button = toolbarwindow.Button(22)
	toolbar_button.Click()
	sleep(0.5)
	toolbar_button.Click()
	sleep(0.5)
	print("pass!\n")

# Toolbar - Clear Desktop
def Clear_Desktop(app, toolbarwindow, lskmainteacherwindowclass):
	print("clear Desktop..")
	toolbar_button = toolbarwindow.Button(24)
	toolbar_button.ClickInput()
	sleep(1)
	toolbar_button.ClickInput()
	print("pass!\n")

# Toolbar - Show Video
def Show_Video(app, toolbarwindow, lskmainteacherwindowclass):
	print("show video..")
	toolbar_button = toolbarwindow.Button(25)
	toolbar_button.ClickInput()
	sleep(1)
	app.Dialog.CloseButton.ClickInput()
	print("pass!\n")

# Toolbar - Class List
def Class_List(app, toolbarwindow, lskmainteacherwindowclass):
	print("class list..")
	toolbar_button = toolbarwindow.Button(27)
	toolbar_button.ClickInput()
	sleep(1)
	app.PopupMenu.MenuItem("Manage Class Lists...").ClickInput()
	sleep(2)
	app.Dialog.CloseButton.ClickInput()
	sleep(1)
	print("pass!\n")

# Toolbar - Files
def Files(app, toolbarwindow, lskmainteacherwindowclass):
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
	lskmainteacherwindowclass.ClickInput(coords=(160,335)) # reset
	print("pass!\n")

# Test - Doc
def Doc(app, toolbarwindow, lskmainteacherwindowclass):
	menu_item = lskmainteacherwindowclass.MenuItem(u'&Help->About LanSchool')
	menu_item.ClickInput()
	sleep(1)
	app.Dialog.Close()
	sleep(1)

Show(app, toolbarwindow)
Show_Student(app, toolbarwindow, lskmainteacherwindowclass)
Vote(app, toolbarwindow, lskmainteacherwindowclass)
Run(app, toolbarwindow, lskmainteacherwindowclass)
Control(app, toolbarwindow, lskmainteacherwindowclass)
Snapshot(app, toolbarwindow, lskmainteacherwindowclass)
Message(app, toolbarwindow, lskmainteacherwindowclass)
Speak(app, toolbarwindow, lskmainteacherwindowclass)
Blank_Screen(app, toolbarwindow, lskmainteacherwindowclass)
Limit_Web(app, toolbarwindow, lskmainteacherwindowclass)
Limit_Apps(app, toolbarwindow, lskmainteacherwindowclass)
Limit_Print(app, toolbarwindow, lskmainteacherwindowclass)
Limit_Drives(app, toolbarwindow, lskmainteacherwindowclass)
Mute(app, toolbarwindow, lskmainteacherwindowclass)
Clear_Desktop(app, toolbarwindow, lskmainteacherwindowclass)
Show_Video(app, toolbarwindow, lskmainteacherwindowclass)
Class_List(app, toolbarwindow, lskmainteacherwindowclass)
Files(app, toolbarwindow, lskmainteacherwindowclass)
Doc(app, toolbarwindow, lskmainteacherwindowclass)

print("all function above has been test\n")

# ===============================================

# # Toolbar - Test Create (toolbar glitch in test builder)
# print("testing..")
# lskmainteacherwindowclass.ClickInput(coords=(160,335)) # unselect first client
# toolbarwindow.Button(6).ClickInput() # open test
# sleep(1)
# app.PopupMenu.MenuItem("Create Test...").ClickInput()
# sleep(1)
# app = Application().Connect(title='LanSchool Test Builder')
# testbuilder = app[u'LanSchool Test Builder']
# testbuilder.Toolbar.Button(u'Open Test').ClickInput() # open test
# sleep(1)
# app.Dialog.Edit.TypeKeys("test.lst")
# app.Dialog.Open.ClickInput()

# testbuilder.Toolbar.Button(9).ClickInput() # edit button
# sleep(1)
# app.Dialog.Button.ClickInput() # browse..
# sleep(1)
# app.Dialog.Edit.TypeKeys("sample.jpg")
# app.Dialog.Open.ClickInput()
# sleep(1)
# app.Dialog.Save.ClickInput()
# sleep(1)

# testbuilder.MenuItem(u'&File->Save Test As...').ClickInput() # save test
# sleep(1)
# app.Dialog.edit.TypeKeys("test " + str(time.time())) # TODO
# app.Dialog.Save.ClickInput()
# sleep(1)
# app.Dialog.OK.ClickInput()

# testbuilder.Toolbar.Button(9).ClickInput() # edit delete image
# sleep(1)
# app.Dialog.Edit10.SetText("") 
# sleep(1)
# app.Dialog.Save.ClickInput()
# sleep(1)

# testbuilder.Toolbar.Button(10).ClickInput() # delete test
# sleep(1)
# app.Dialog.Yes.ClickInput()
# sleep(1)

# testbuilder.Toolbar.Button(0).ClickInput() # new test
# sleep(1)
# app.Dialog.Button2.ClickInput()
# sleep(1)
# app.Dialog.Edit.TypeKeys("Random Question", with_spaces=True)
# sleep(1)
# app.Dialog.RadioButton2.ClickInput()
# app.Dialog.CheckBox1.ClickInput()
# app.Dialog.CheckBox2.ClickInput()
# app.Dialog.CheckBox3.ClickInput()
# sleep(1)
# app.Dialog.Save.ClickInput()
# testbuilder.Close()
# sleep(1)

# lskmainteacherwindowclass.ClickInput(coords=(160,335)) # select first client
# app = Application().connect(title='LanSchool Teacher Console')

# print("pass!\n")
