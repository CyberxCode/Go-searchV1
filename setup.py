import sys
import os
from Colors import*

class application():

	def operation(self,type_,string,path):#Select command
		op_cmd="grep -r --include=" #command
		Op_type="*.{}".format(type_) #command
		op_str=' "{}"'.format(string) #command
		op_path=" {}".format(path) #command
		command=(op_cmd+Op_type+op_str+op_path)
		os.system(command)


def main():
	print("*".center(60,"*"))
	print(Formatting.Bold,Base.WARNING,"Welcome to Go-Search V1".center(60," "),Base.END, Formatting.Reset)
	print("""You can use this script to search for files within  extension 
  php,html,py,txt,docx,xml,xls,xlsx,xlsb,xlt,ppt,java,jar
                on Linux platform """)
	print(Color.F_Red,"This script in development phase".center(60," "),GColor.END)
	print("*".center(60,"*"))
	try:
		def user_input(argv):#Requesting data
			recovery=input("Please entr your {} :".format(argv))
			return(recovery)
		app=application()
		#list of types Permissible Extensions
		extension_type=["php","html","py","txt","docx","xml","xls","xlsx","xlsb","xlt","ppt","java","jar"]
		rec_type=user_input("type")	#Take type
		if rec_type in extension_type:
			rec_str=user_input("str")#Take string for search
			rec_path=user_input("path")#Take path files
			app.operation(rec_type,rec_str,rec_path)
		else:
			print(Formatting.Bold,Base.FAIL,"extension file Not supported :/",Base.END, Formatting.Reset)
	except Exception as e:
		print("ERROR !")
if __name__ == '__main__':
	main()