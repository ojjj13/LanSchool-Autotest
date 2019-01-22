# java 8 build #201, sikulixide 1.1.3
# wait screenshot type delete_text loop doc 
def Show():
    click("1548124804699.png")
    wait("1548124826026.png")
    click("1548124826026.png")
    click("1548124826026.png")
    click("1548124954309.png")


def Show_Student():
    click("1548136490068.png")
    click("1548126358165.png")

    wait("1548126418191.png")
    click("1548126418191.png")
    click("1548136547539.png")

def vote():
    wait("1548126464907.png")
    click("1548126464907.png")

    wait("1548126919465.png")
    type("Random Question")
    click("1548127070370.png")
    wait("1548127112741.png")

    type("votetest")
    click("1548127253087.png")
    wait("1548127380376.png")
    click("1548127380376.png")
    sleep(1)
    click("1548137634213.png")
    type(Key.HOME,Key.SHIFT)
    sleep(1)
    type(Key.DELETE)
    wait("1548138108882.png")
    click("1548138108882.png")
    wait("1548138135136.png")
    type("votetest.lsq")
    click("1548138189195.png")
    wait("1548138232941.png")
    click("1548138232941.png")
    sleep(1)
    click("1548138270031.png")

def Test_Create():
    click("1548142167556.png")
    wait("1548142190232.png")
    click("1548142190232.png")
    wait("1548142253228.png")
    click("1548142253228.png")
    wait("1548142298252.png")
    type("1548142298252.png", "what is 1 + 1 ?")
    click("1548142346926.png")
    click("1548142367394.png")
    type("1548142439168.png","2")
    click("1548142567160.png")
    wait("1548142636040.png")
    click("1548142636040.png")
    wait("1548142655939.png")
    click("1548142655939.png")
    wait("1548142692356.png")
    click("1548142692356.png")
    wait("1548142710718.png")
    click("1548142710718.png")
    click("1548136547539.png")

def Control():
    click("1548136490068.png")
    click("1548142970069.png")
    wait("1548142995299.png")
    rightClick("1548142995299.png")
    wait("1548143020899.png")
    click("1548143020899.png")
    sleep(1)
    click("1548143081579.png")
    click("1548136547539.png")
    
def SnapShot(): 
    click("1548136490068.png")
    click("1548143189118.png")
    wait("1548143224785.png")
    click("1548143224785.png")
    click("1548136547539.png")

def Message():
    click("1548143457560.png")
    wait("1548143477701.png")
    type("pay attention!")
    click("1548143512118.png")
    click("1548143523840.png")
    click("1548143536563.png")
        
Show()
Show_Student()
vote()
Test_Create()
Control()
SnapShot()
Message()