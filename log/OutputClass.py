import pandas as pd
from pandas import DataFrame as df
import time 

class Output:
	
	"""class use training"""
	
	def __init__(self, *show):
		self.__show = show

	def show(self):
		self.__show = "".join(self.__show)
		print(self.__show)

	def time(self):
		localtime = time.localtime()
		hour, minutes = str(localtime[3]), format(localtime[4], "02")
		return ".".join(map(str, localtime[0:3]))+" "+ hour +":"+minutes

	def check(self):
		"""to check duplication"""
		localtime = time.localtime()
		data = pd.read_csv("research_log.csv", index_col=False)
		if data["time"][0][5]==str(localtime[1]) and data["time"][0][7]==str(localtime[2]):
			while True:
				input_ = input("---CAUTION---\n"+\
					"it appears you have already filled in, do you want to continue? <y or n>\n")
				if input_=="n":
					print("finish the session, Good Job!")
					exit()
				elif input_ =="y":
					print("okay, move on")
					break
				else:
					print("Please answer with 'y' or 'n'")
		else:
			pass


	def store(self, data_list, columns_list):
		"""to create csv"""
		data = df([data_list],
			columns=columns_list
			)
		data.to_csv("research_log.csv", index=False) #毎回一応とっておく。
		data.to_csv("/Users/yamadaikuya/Desktop/research_log.csv", mode="a", header=False ,index=False)