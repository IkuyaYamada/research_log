import time
from read_csv import Example

time_str = time.asctime()
print("current time: {}".format(time_str)) 
improvement = input("any improvement?<free>\n")
material = input("learning material?<paper, textbook, online course, etc.>\n")
place = input("where?<Kashiwa, Home, Hongo,>\n")
plan = input("tomorrow?\n")

ex = Example("improvement: {}\nmaterial: {}\nplace: {}\nplan: {}"\
	.format(improvement, material, place, plan))
ex.show()