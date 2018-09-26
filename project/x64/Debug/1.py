from ctypes import *
from reportlab.pdfgen import canvas
dll =cdll.LoadLibrary("C://Users//tianyang//Documents//Visual Studio 2017//Project//Dll3//x64//Debug//Dll3.dll")
readfile=dll.pl
readfile.argtypes=[c_char_p]
readfile.restype=c_int
s=(c_char * 20)(*bytes("x.xml","utf-8"))
h=readfile(s)
c=canvas.Canvas("test.pdf")
c.drawString(100,20,str(h))
c.showPage()
c.save()
print("save now")
print(h)
#readfile=dll.fl
#readfile.argtypes=[c_char_p]
#readfile.restype=c_float
#h=readfile(s)
#print(h)
