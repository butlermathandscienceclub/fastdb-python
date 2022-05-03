import json
class db:
	def __init__(self):
		self.dict = { }
	def set_val(self, key,val):
		self.dict[key] = val
		with open("kdb.json",'w') as file2:
			
			file2.write(json.dumps(self.dict))
	def get_val(self, key):
		
		return self.dict[key]
	def load(self):
		with open("kdb.json",'r') as file:
			self.dict = json.load(file)
	def save(self):
		with open("kdb.json",'w') as file2:
			
			file2.write(json.dumps(self.dict))
	def print_db(self, types=False):
		for it in self.dict:
			if types == True: type_ = type(it).__name__
			else: type_ = ''
			print(f"{it} : {self.dict[it]} {type_}")


