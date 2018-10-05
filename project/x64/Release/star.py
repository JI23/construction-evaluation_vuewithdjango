from ctypes import *
dll =cdll.LoadLibrary("./x64//Release//Dll3.dll")
s=(c_char * 20)(*bytes("p.xml","utf-8"))

CostStar=dll.TryGetCostStar
CostStar.argtypes=[c_char_p]
CostStar.restype=c_int
h=CostStar(s)
h="CostStar"+h+""
print("CostStar:",h)

TimeStar=dll.TryGetTimeStar
TimeStar.argtypes=[c_char_p]
TimeStar.restype=c_int
h1=TimeStar(s)
h1="TimeStar"+h1+""
print("TimeStar:",h)

CalsualtyStar=dll.TryGetCalsualtyStar
CalsualtyStar.argtypes=[c_char_p]
CalsualtyStar.restype=c_int
h2=CalsualtyStar(s)
h2="CalsualtyStar"+h2+""
print("CalsualtyStar:",h)

FinalStar=dll.TryGetFinalStar
FinalStar.argtypes=[c_char_p]
FinalStar.restype=c_int
h3=FinalStar(s)
h3="FinalStar"+h3+""
print("FinalStar:",h)
