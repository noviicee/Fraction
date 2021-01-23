#23-01-2021
#Class for Fractions

class Fraction:
	def __init__(self,num,den):
		self.num=num
		self.den=den
		"""As a special constraint on constructors, no value may be returned; doing so will cause a TypeError to be raised at runtime.
		But, of course, adding the return None doesn't buy you anything.
		__init__ doesn't return anything and should always return None"""

	def __str__(self): #It is overridden to return a printable string representation of any user defined class.
		return("{}/{}".format(self.num,self.den))

	def __add__(self,other):
		temp_num=(self.num*other.den)+(self.den*other.num)
		temp_den=self.den*other.den
		return("{}/{}".format(temp_num,temp_den))

	def __sub__(self,other):
		temp_num=(self.num*other.den)-(self.den*other.num)
		temp_den=self.den*other.den
		return("{}/{}".format(temp_num,temp_den))

	def __mul__(self,other):
		temp_num=(self.num*other.num)
		temp_den=self.den*other.den
		return("{}/{}".format(temp_num,temp_den))

	def __truediv__(self,other): #there is no need of // and % in case of fractions, since the return value will always be a fraction.
		temp_num=(self.num*other.den)
		temp_den=self.den*other.num
		return("{}/{}".format(temp_num,temp_den))

	def __pow__(self,other):
		temp_num=self.num**other
		temp_den=self.den**other
		return("{}/{}".format(temp_num,temp_den))

	def __gt__(self,other):
		if self.num/self.den > other.num/other.den :
			return True
		return False

	def __ge__(self,other):
		if self.num/self.den >= other.num/other.den :
			return True
		return False

	def __lt__(self,other):
		if self.num/self.den < other.num/other.den :
			return True
		return False

	def __le__(self,other):
		if self.num/self.den <= other.num/other.den :
			return True
		return False

	def __eq__(self,other):
		if self.num/self.den == other.num/other.den :
			return True
		return False

	def __ne__(self,other):
		if self.num/self.den != other.num/other.den :
			return True
		return False
