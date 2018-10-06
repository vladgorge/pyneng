#!/usr/bin/env python3

ignore = ['duplex', 'alias', 'Current configuration']
def ignore_command(command, ignore):
	'''
	Функция проверяет содержится ли в команде слово из списка ignore.
	command - строка. Команда, которую надо проверить
	ignore - список. Список слов
	Возвращает True, если в команде содержится слово из списка ignore, False - если нет'''
	return any(word in command for word in ignore)
fclr=open('config_sw1_cleared','w')
f=open('config_sw1.txt')
for comm in f:
	if ignore_command(comm, ignore)==False and comm.find('!')==-1:
		fclr.write(comm)
fclr.close()

def dict_comm(command):
	f=open(command)
	dict_command={}
	for line in f:
		if not line.startswith(' '):
			line1=line.strip()
			dict_command[line1]=[]
		elif line.startswith(' '):
			dict_command[line1].append(line.strip())
	print(dict_command)

dict_comm('config_sw1_cleared')
