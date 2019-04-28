class Example:
	
	"""class use training"""
	
	def __init__(self, *show):
		self.__show = show
	
	def show(self):
		self.__show = "".join(self.__show)
		print(self.__show)