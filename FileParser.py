#!/usr/bin/python
import ast
import os
from threading import Thread

class MyCustomVisitor(ast.NodeVisitor):
    
    def __init__(self):
        self.dictionary = {}
    
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

    def print_call(self):
        print("\tAll functions called in this code:")
        for name in self.dictionary:
            print("\t\t{0} was called {1} times.".format(name, self.dictionary[name]))
            
    def visit_Call(self, node):        
        call_name = self.get_call_name(node)
        if call_name not in self.dictionary:
            self.dictionary[call_name] = 1
        else:
            self.dictionary[call_name] += 1 
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




        
if __name__ == "__main__":
    import sys
    import glob
    
    if len(sys.argv) == 2 :
        input_files = glob.glob('./'+sys.argv[1]+'*.txt')
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
            visitor.print_call()

