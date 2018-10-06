#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
	'''
	Функция проверяет содержится ли в команде слово из списка ignore.
	command - строка. Команда, которую надо проверить
	ignore - список. Список слов
	Возвращает True, если в команде содержится слово из списка ignore, False - если нет'''
	return any(word in command for word in ignore)
fclr=open('config_r1_cleared','w')
f=open('config_r1.txt')
for comm in f:
	if ignore_command(comm, ignore)==False and comm.find('!')==-1:
		fclr.write(comm)
fclr.close()

def dict_comm(command):
	f=open(command)
	dict_command1={}
	list_command1=[]
	for line in f:
		if not line.startswith(' '):
			line1=line.strip()
			dict_command1[line1]=[]
		elif line.count(' ',0,2)==1:
			line2=line.strip()
			dict_command1[line1].append(line2.strip())
		elif line.count(' ',0,2)==2:
			dict_command1[line1]={}
			list_command1.append(line.strip())
			dict_command1[line1][line2]=list_command1
	#print(dict_command1)
	for key in dict_command1.keys():
		print(key, dict_command1[key])
		print('\n')


dict_comm('config_r1_cleared')
