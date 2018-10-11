from ctypes import *
from reportlab.pdfgen import canvas
dll =cdll.LoadLibrary("Dll3.dll")
s=(c_char * 20)(*bytes("project.xml","utf-8"))

readfile=dll.TryGetCostStar
readfile.argtypes=[c_char_p]
readfile.restype=c_int
h1=readfile(s)
CostStar="CostStar:"+str(h1)

readfile=dll.TryGetTimeStar
readfile.argtypes=[c_char_p]
readfile.restype=c_int
h2=readfile(s)
TimeStar="TimeStar:"+str(h2)

readfile=dll.TryGetCalsualtyStar
readfile.argtypes=[c_char_p]
readfile.restype=c_int
h3=readfile(s)
CalsualtyStar="CalsualtyStar:"+str(h3)

readfile=dll.TryGetFinalStar
readfile.argtypes=[c_char_p]
readfile.restype=c_int
h4=readfile(s)
FinalStar="FinalStar:"+str(h4)

h=CostStar+"    "+TimeStar+"    "+CalsualtyStar+"    "+FinalStar
print(h)

c=canvas.Canvas("test.pdf")
c.drawString(100,500,h)
c.showPage()
c.save()
print("save now")
