import json
class fastdb:
	def __init__(self):
		self.dict = { }
	def set_val(self, key,val):
		self.dict[key] = val
		with open("kdb.json",'w') as file2:
			print(self.dict)
			file2.write(json.dumps(self.dict))
	def get_val(self, key):
		return self.dict[key]
	def load(self):
		with open("kdb.json",'r') as file:
			
			self.dict = json.load(file)
	def save(self):
		with open("kdb.json",'w') as file2:
			print(self.dict)
			file2.write(json.dumps(self.dict))


