import os
import sys
import time
import platform
lenn = 11 if '-extended' in sys.argv else 8
is_win = ('windows' in platform.system().lower()) 
if not is_win:
	os.chmod('data', 754)
test_paras = [
	('0', 3, 'n = 3, m = 3, num = 3'), 
	('1', 3, 'n = 5, m = 5, num = 3'),	
	('2', 3, 'n = 3, m = 3, num = 9'), 
	('3', 3, 'n = 5, m = 5, num = 25'),	
	('4', 3, 'n = 10, m = 10, num = 50'),
	('A', 50, 'n = 100, m = 50, occupied: 5%'),
	('B', 30, 'n = 1000, m = 500, occupied: 5%'),
	('C', 20, 'n = 10000, m = 5000, occupied: 1%'),
	('D', 10, 'n = 100, m = 50, extended'),
	('E', 6, 'n = 1000, m = 500, extended'),
	('F', 4, 'n = 10000, m = 5000, extended')
]
os.system("javac AddSparseMatrix.java")
def check(file1, file2):
	with open(file1, 'r') as fin:
		lines1 = fin.read()
		lines1 = ''.join(lines1.split('\n'))
		lines1 = ''.join(lines1.split(' '))
	with open(file2, 'r') as fin:
		lines2 = fin.read()
		lines2 = ''.join(lines2.split('\n'))
		lines2 = ''.join(lines2.split(' '))
	return lines1 == lines2
	
def test(name, times, info):
	print('test case: '+ name + ': ' + info)
	for t in range(times):
		print('Case#'+name+'['+str(t+1)+']', end=': ')
		if is_win: os.system('data.exe ' + name)
		else: os.system('./data ' + name)
		rtime = -time.time()
		os.system('java -Xms128m -Xmx128m AddSparseMatrix input1.in input2.in output.out')
		rtime += time.time()
		if check('output.out', 'stdop.out'):
			print('\033[;32mAccepted.\033[0m %.3fs'%rtime)
		else:
			print('\n\033[;31mError\033[0m')
			exit(0)
for k, t, info in test_paras[:lenn]:
	test(k, t, info)