#!/usr/bin/python
import ast
import os

class ClassVisitor(ast.NodeVisitor):

	superclasses = {}

	def visit_ClassDef(self, node):
		for n in node.bases:
			if n.attr not in self.superclasses:
				self.superclasses[n.attr] = [node.name]
			else:
				self.superclasses[n.attr].append(node.name)



	def printDict(self):
		print(self.superclasses)
		

if __name__ == "__main__":
    
    import glob
    import sys
    

    if len(sys.argv) == 2 :
    	os.chdir(sys.argv[1])
    input_files = glob.glob('./*.py')

    for file in input_files:
        print("Opening:{}".format(file))
        with open(file, "r") as input:
    		# reads the content of this file
        	file_str  = input.read()

	        # parses the content of this file
	        root = ast.parse(file_str)

	        # visits the Abstract Syntax Tree
	        v = ClassVisitor()
	        v.visit(root)
	        v.printDict()