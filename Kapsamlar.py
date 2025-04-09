"""
kapsamlar
"""

"""
Global Kapsam
"""
def B():
    global b
    b = 300
    print( b)
B()
print(b)

"""
yerel için
"""
def fonk():
    c = 300
    print(c)
fonk()
"""
İşlev İçinde İşlev
"""

def fonk2():
    D = 120
    def fonk3():
        print(D)
    fonk3()
fonk2()
"""
Küresel Kapsam
"""

x = 300
def A():
    print( x)
A()
