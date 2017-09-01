from FileParser import *
import sys

class Examiner():

	myVisitor = MyCustomVisitor()

	def __init__(self, root):
		self.root = root

	def badNameDetection(self):
		self.myVisitor.visit(root)
		for name in self.myVisitor.names:
			if(len(name)<=3 or len(name)>=20):
				print("Bad Name Definition in: {}".format(name))



if __name__ == "__main__" :
	import glob
	if len(sys.argv) == 2 :
		os.chdir(sys.argv[1])
		input_files = glob.glob('./*.py')
	else:
		input_files = glob.glob('./*.py')
	for file in input_files:
		print("Opening:{}".format(file))
		with open(file, "r") as input:
			# reads the content of this file
			file_str  = input.read()
			# parses the content of this file
			root = ast.parse(file_str)
			detector = Examiner(root)
			detector.badNameDetection()

