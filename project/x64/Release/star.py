from ctypes import *
<<<<<<< HEAD
dll =cdll.LoadLibrary("./x64//Release//Dll3.dll")
=======
dll =cdll.LoadLibrary("Dll3.dll")
>>>>>>> 97ca1ef2bc62eb429b8a02c9063b105d7dc0b82c
s=(c_char * 20)(*bytes("p.xml","utf-8"))

CostStar=dll.TryGetCostStar
CostStar.argtypes=[c_char_p]
CostStar.restype=c_int
h=CostStar(s)
<<<<<<< HEAD
h="CostStar"+h+""
print("CostStar:",h)
=======
h="CostStar:"+str(h)
print(h)
>>>>>>> 97ca1ef2bc62eb429b8a02c9063b105d7dc0b82c

TimeStar=dll.TryGetTimeStar
TimeStar.argtypes=[c_char_p]
TimeStar.restype=c_int
h1=TimeStar(s)
<<<<<<< HEAD
h1="TimeStar"+h1+""
print("TimeStar:",h)
=======
h1="TimeStar:"+str(h1)
print(h1)
>>>>>>> 97ca1ef2bc62eb429b8a02c9063b105d7dc0b82c

CalsualtyStar=dll.TryGetCalsualtyStar
CalsualtyStar.argtypes=[c_char_p]
CalsualtyStar.restype=c_int
h2=CalsualtyStar(s)
<<<<<<< HEAD
h2="CalsualtyStar"+h2+""
print("CalsualtyStar:",h)
=======
h2="CalsualtyStar:"+str(h2)
print(h2)
>>>>>>> 97ca1ef2bc62eb429b8a02c9063b105d7dc0b82c

FinalStar=dll.TryGetFinalStar
FinalStar.argtypes=[c_char_p]
FinalStar.restype=c_int
h3=FinalStar(s)
<<<<<<< HEAD
h3="FinalStar"+h3+""
print("FinalStar:",h)
=======
h3="FinalStar:"+str(h3)
print(h3)
>>>>>>> 97ca1ef2bc62eb429b8a02c9063b105d7dc0b82c
