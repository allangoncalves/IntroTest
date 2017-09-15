from Visitors import *
import sys
import glob
import json

class Examiner():

	myVisitor = ClassVisitor()
	root = ast.AST()

	def projectParser(self, projectFolder):
		os.chdir(projectFolder)
		for directory, folderName, file in os.walk("."):
			for name in file:
				if name.endswith(".py"):
					print(os.path.join(directory, name))
					print("Opening file:{}".format(name))
					with open(name, "r") as input:
						# reads the content of this file
						file_str  = input.read()
						# parses the content of this file
						self.root = ast.parse(file_str)
						self.myVisitor.visit(self.root)
						#self.myVisitor.print_Call()
					print(self.myVisitor.superclasses)



if __name__ == "__main__" :
	
	detector = Examiner()
	detector.projectParser(sys.argv[1])
	os.chdir(sys.argv[1])
	with open("eae","w") as input:
		input.write(json.dumps(detector.myVisitor.superclasses, ensure_ascii=False, indent=4))	


