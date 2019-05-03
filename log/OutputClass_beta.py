import os, sys
import pandas as pd
from pandas import DataFrame as df
import time 
import random

class Output:
	
	"""class use training"""

	def __init__(self, *show):
		self.__show = show

	def initializaion(self, data_list, columns_list, temporal=False):
		if temporal==True:
			path ="/Users/yamadaikuya/Desktop/research_log_beta.csv"
		else:
			path ="/Users/yamadaikuya/gitrepos/research_log/log_beta/temporal_log_beta.csv"
		
		if os.path.exists(path)==True:
			return False
		else:
			data = self.store(data_list, columns_list)
			data_ = data.ix[[0],:]
			data_.to_csv(path, header=True ,index=False)
			self.encouraging_phrase()
			sys.exit()
			

	def show(self):
		self.__show = "".join(self.__show)
		print(self.__show)

	def time(self):
		localtime = time.localtime()
		hour, minutes = str(localtime[3]), format(localtime[4], "02")
		return ".".join(map(str, localtime[0:3]))+" "+ hour +":"+minutes

	def multiple_input(self, passage=None):
		"""to obtain multiple lines from input"""
		print(passege)
		try:
			while True:
				data = input()
				if not data:break
				yield data
		except KeyboadInterrupt:
			return

	def check(self):
		"""to check duplication"""
		localtime = time.localtime()
		path = "/Users/yamadaikuya/gitrepos/research_log/log_beta/temporal_log_beta.csv"
		if os.path.exists(path)==False:
			return 
		data = pd.read_csv("/Users/yamadaikuya/gitrepos/research_log/log_beta/temporal_log_beta.csv", index_col=False)
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
		data_.to_csv("/Users/yamadaikuya/gitrepos/research_log/log_beta/temporal_log_beta.csv", index=False) #毎回一応とっておく。
		data_.to_csv("/Users/yamadaikuya/Desktop/research_log_beta.csv", mode="a", header=False ,index=False)

	def encouraging_phrase(self):
		phrases = [
		"Where there is a will, there is a way.",
		"No Pain, No Gain.",
		"You will lose nothing. So what? Just do it!",	
		"The only one who can beat me is me.",
		"You can’t make an omelette without breaking eggs.",
		"すっごーい"
		]
		separate = "/"*100
		print("\n"+separate+"\n"+"/////// "+random.choice(phrases)+" /////////////"+"\n"+separate)








