import os
import pandas as pd
from pandas import DataFrame as df
import time 
import random

class Output:
	
	"""class use training"""

	def __init__(self, *show):
		self.__show = show

	def initializaion(self, data_list, columns_list):
		path ="/Users/yamadaikuya/Desktop/research_log.csv"
		if os.path.exists(path)==True:
			return False
		else:
			data = self.store(data_list, columns_list)
			data_ = data
			data_.to_csv("/Users/yamadaikuya/Desktop/research_log.csv", mode="a", header=True ,index=False)
			return True


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
		data = pd.read_csv("temporal_log.csv", index_col=False)
		if data["time"][0][5]==str(localtime[1]) and data["time"][0][7]==str(localtime[2]):
			while True:
				input_ = input("---CAUTION---\n"+\
					"it appears you have already filled in, do you want to continue? <y or n>\n")
				if input_=="n":
					self.encouraging_phrase()
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
		return data
	
	def csv(self, data_list, columns_list):
		data_ = self.store(data_list, columns_list)
		data_.to_csv("temporal_log.csv", index=False) #毎回一応とっておく。
		data_.to_csv("/Users/yamadaikuya/Desktop/research_log.csv", mode="a", header=False ,index=False)

	def encouraging_phrase(self):
		phrases = [
		"Where there is a will, there is a way.",
		"No Pain, No Gain.",
		"You will lose nothing. So what? Just do it!",	
		"The only one who can beat me is me.",
		"You can’t make an omelette without breaking eggs."
		]
		print("-----\n"+random.choice(phrases)+"\n-----")













