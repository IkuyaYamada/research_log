import time
from OutputClass_beta import Output

Output().multiple_input()

# check duplication 
Output().check()

# gather achivement
n_of_lines = 5
time_str = time.asctime()
# weather = Output().weather()
separate = "----------------------------------------------------------------------------------"
improvement = input("\nany improvement?<free>\n"+separate+"\n")
finding = input("\nnew findings?\n"+separate+"\n")
material = input("\nlearning material?<paper, textbook, online course, etc.>\n"+separate+"\n")
place = input("\nwhere?<Kashiwa, Home, Hongo,>\n"+separate+"\n")
plan = input("\ntomorrow?\n"+separate+"\n")
comment = input("\nany comment?\n"+separate+"\n")

# output on the console
op = Output("\nimprovement: {}\nmaterial: {}\nplace: {}\nplan: {}\ncomment: {}"\
	.format(improvement, material, place, plan, comment))
op.show()

# output to the csv
current_time = op.time()
data_list = [current_time, improvement, material, place, plan, comment]
columns_list = ["time", "improvement", "materials", "working place", "tomorrow's plan", "comment"]
inintal = op.initializaion(data_list, columns_list, True)
inintal = op.initializaion(data_list, columns_list, False)
if inintal == False:
	op.csv(data_list, columns_list)
op.encouraging_phrase()

