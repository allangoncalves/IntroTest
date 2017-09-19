'''
class NodeNotFoundException(Exception):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return repr(self.value)
'''

class Node:
	def __init__(self, key, children=None):
		self.key = key
		self.children = children or []
	
	def __str__(self):
		return str(self.key)

class Root:
	def __init__(self, node):
		self.nodes = [node]

class BTree:

	def __init__(self):
		self.root = None
		self.size = 0

	def find_node(self, node, key):
		if node == None or node.key == key:
			return node		
		for child in node.children:
			return_node = self.find_node(child, key)
			if return_node: 
				return return_node
		return None	

	def add(self, new_key, parent_key=None):
		new_node = Node(new_key)
		if parent_key == None:
			self.root = Root(new_node)
			self.size = 1
		else:
			parent_node = self.find_node(self.root, parent_key)
			if not(parent_node):
				self.root.nodes.append(parent_key)
				self.root.nodes[len(self.root.nodes)-1].children.append(new_node)
				self.size += 2 
			else:
				parent_node.children.append(new_node)
				self.size += 1
	
	def print_tree(self, node, str_aux):
		if node == None: return ""
		str_aux += str(node) + '('
		for i in range(len(node.children)):
			child = node.children[i]
			end = ',' if i < len(node.children) - 1 else ''
			str_aux = self.print_tree(child, str_aux) + end
		str_aux += ')'
		return str_aux

	def is_empty(self):
		return self.size == 0

	def lenght(self):
		return self.size

	def __str__(self):
		str_aux = "("
		for node in self.nodes:
			if len(self.nodes)-1 == self.nodes.index(node)
				str_aux += self.print_tree(self.node, "")+")"
			else:
				str_aux += self.print_tree(self.node, "")+","

		return str_aux


if __name__ == "__main__":
    				
	tree = BTree()
	tree.add(10)
	tree.add(20, 10)
	tree.add(30, 10)
	tree.add(50, 20)
	tree.add(40, 20)
	tree.add(70, 20)
	tree.add(78, 70)
	tree.add(11, 30)

	print 'N-ary tree size:', tree.lenght()
	print tree