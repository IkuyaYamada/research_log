import time
from OutputClass_beta import Output

inputs = Output().multiple_input

# check duplication 
Output().check()

# gather achivement
n_of_lines = 5
time_str = time.asctime()

# caution
print("the redo function does not work as you expect, avoid using it")

# weather = Output().weather()
separate = "-"*50
improvement = inputs("\nany progress?")
print(separate)
finding = inputs("\nnew findings?")
print(separate)
material = inputs("\nlearning material? <paper, textbook, online course, etc.>")
print(separate)
place = inputs("\nwhere? <Kashiwa, Home, Hongo,>")
print(separate)
plan = inputs("\ntomorrow?")
print(separate)
comment = inputs("\nany comment?")

# output on the console
op = Output("\nimprovement: {}\nmaterial: {}\nfindings: {}\nplan: {}\ncomment: {}"\
	.format(improvement, material, finding, plan, comment))
op.show()

# output to the csv
current_time = op.time()
data_list = [current_time, "\n".join(improvement), "\n".join(finding), "\n".join(material)\
	, "\n".join(place), "\n".join(plan), "\n".join(comment)]
columns_list = ["time", "improvement", "findings", "materials", "working place", "tomorrow's plan", "comment"]
inintal = op.initializaion(data_list, columns_list, True)
inintal = op.initializaion(data_list, columns_list, False)
if inintal == False:
	op.csv(data_list, columns_list)
op.encouraging_phrase()

