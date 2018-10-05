from ctypes import *
dll =cdll.LoadLibrary("Dll3.dll")
s=(c_char * 20)(*bytes("p.xml","utf-8"))

CostStar=dll.TryGetCostStar
CostStar.argtypes=[c_char_p]
CostStar.restype=c_int
h=CostStar(s)
h="CostStar:"+str(h)
print(h)

TimeStar=dll.TryGetTimeStar
TimeStar.argtypes=[c_char_p]
TimeStar.restype=c_int
h1=TimeStar(s)
h1="TimeStar:"+str(h1)
print(h1)

CalsualtyStar=dll.TryGetCalsualtyStar
CalsualtyStar.argtypes=[c_char_p]
CalsualtyStar.restype=c_int
h2=CalsualtyStar(s)
h2="CalsualtyStar:"+str(h2)
print(h2)

FinalStar=dll.TryGetFinalStar
FinalStar.argtypes=[c_char_p]
FinalStar.restype=c_int
h3=FinalStar(s)
h3="FinalStar:"+str(h3)
print(h3)
