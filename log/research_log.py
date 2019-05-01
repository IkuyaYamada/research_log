import time
from OutputClass import Output

# check duplication 
Output().check()

# gather achivement
time_str = time.asctime()
# weather = Output().weather()
improvement = input("any improvement?<free>\n")
finding = input("new findings?\n")
material = input("learning material?<paper, textbook, online course, etc.>\n")
place = input("where?<Kashiwa, Home, Hongo,>\n")
plan = input("tomorrow?\n")

# output on the console
op = Output("improvement: {}\nmaterial: {}\nplace: {}\nplan: {}"\
	.format(improvement, material, place, plan))
op.show()

# output to the csv
current_time = op.time()
data_list = [current_time, improvement, material, place, plan]
columns_list = ["time", "improvement", "materials", "working place", "tomorrow's plan"]
inintal = op.initializaion(data_list, columns_list)
if inintal == False:
	op.csv(data_list, columns_list)
op.encouraging_phrase()