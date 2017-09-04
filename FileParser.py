#!/usr/bin/python
import ast
import os
import sys

class auxVisitor(ast.NodeVisitor):

    def __init__(self):
        self.dictionary = {}

    def visit_Call(self, node):        
        call_name = self.get_call_name(node)
        self.dictionary[call_name] = 1 if call_name not in self.dictionary else self.dictionary[call_name]+1
        super(auxVisitor, self).generic_visit(node)

    def get_call_name(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return node.func.attr
        else:
            raise NotImplementedError("Could not extract call-name from node: " + str(node))

    def getDictionary(self):
        return self.dictionary

class MyCustomVisitor(ast.NodeVisitor):
    
    def __init__(self):
    	self.count = 0
        self.dictionary = {}
        self.names = []
        self.numberOfArguments = {}
    
    # Aux function
    def get_call_name(self, node):
        if isinstance(node.func, ast.Name):
            return node.func.id
        elif isinstance(node.func, ast.Attribute):
            return node.func.attr
        else:
            raise NotImplementedError("Could not extract call-name from node: " + str(node))
        
    def get_variable_context(self, node):
        if isinstance(node.ctx, ast.Load):
            return 'Load'
        elif isinstance(node.ctx, ast.Store):
            return 'Store'
        elif isinstance(node.ctx, ast.Del):
            return 'Del'

    def print_Call(self):
        print("\tAll defined functions called in this code:")
        for name in self.dictionary:
            print("\t\t{0} was called.".format(name))
            for mydict in self.dictionary[name]:
                print("\t\t\t{0} was called {1}x.".format(mydict, self.dictionary[name][mydict]))
            
    def visit_Call(self, node):  
    	self.count += 1      
        call_name = self.get_call_name(node)
        print("\t'{0}' was called.".format(call_name))
        self.numberOfArguments[call_name] = len(node.args)
        super(MyCustomVisitor, self).generic_visit(node)

    def visit_ClassDef(self, node):
        print("\tClass '{0}' was defined.".format(node.name))
        super(MyCustomVisitor, self).generic_visit(node)

    def visit_Import(self, node):
        for item in node.names:
            print("\tImport {0} was found.".format(item.name))
        super(MyCustomVisitor, self).generic_visit(node)

    def visit_ImportFrom(self, node):
        sys.stdout.write("\tImport {0} from ".format(node.module))
        for item in node.names:
            sys.stdout.write(item.name)
        print()
        super(MyCustomVisitor, self).generic_visit(node)

    def visit_Name(self, node):
        context = self.get_variable_context(node)
        print("\t'{0}' was found with {1} context.".format(node.id, context))
        super(MyCustomVisitor, self).generic_visit(node)
        self.names.append(node.id)

    def visit_FunctionDef(self, node):
        aux = auxVisitor()
        for item in node.body:
            aux.visit(item)
            mydict = aux.getDictionary()
        self.dictionary[node.name] = mydict 
        
        
if __name__ == "__main__":
    
    import glob
    
    if len(sys.argv) == 2 :
    	os.chdir(sys.argv[1])
        input_files = glob.glob('./*.py')
    else :
        input_files = glob.glob('./*.py')

    ##print("Processing file: " + input_path)
    for file in input_files:
        print("Opening:{}".format(file))
        with open(file, "r") as input:

            # reads the content of this file
            file_str  = input.read()

            # parses the content of this file
            root = ast.parse(file_str)

            # visits the Abstract Syntax Tree
            visitor = MyCustomVisitor()
            visitor.visit(root)
            visitor.print_Call()

