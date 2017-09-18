#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hmac, os, json, sys

class Guarda():

	def __init__(self):
		self.files = {}
		self.early = {}

	def getBack(self):
		with open(".table", "r") as input:
			file_str  = input.read()
			self.files = json.loads(file_str)
			self.early = self.files

	def projectParser(self, projectFolder):
			os.chdir(projectFolder)
			self.getBack()
			for directory, folderName, file in os.walk("."):
				for name in file:
					fullName = os.path.join(directory, name) 
					#print(os.path.join(directory, name))
					print("Opening file:{}".format(name))
					with open(fullName, "r") as input:
						file_str  = input.read()
						myhash = hmac.new(file_str).hexdigest()
						if fullName not in self.files:
							self.files[fullName] = myhash
							print("{} foi adicionado".format(fullName))
						elif not self.files[fullName].compare_digest(myhash):
							print("{} foi alterado".format(fullName))
							ans = input("Deseja salvar as alterações?(S/N)")
							if(ans == "S"):
								self.files[fullName] = myhash
			diff = set(self.files.items()) ^ set(self.early.items())
			for d in diff:
				print("{} foi removido".format(d))

if __name__ == '__main__':

	if len(sys.argv) >= 2:
		g = Guarda()
		g.projectParser(sys.argv[1])
		g.verify()
		j = json.dumps(g.files, ensure_ascii=False, indent=4)
		f = open(".table", "w")
		f.write(j)
		f.close()
		#"/home/allangoncalves/Downloads"
	else:
		print("Insira o diretório a ser guardado")