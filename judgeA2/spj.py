import os
import sys
import time
import platform

#default
is_win = ('windows' in platform.system().lower()) 
case_num = 100
stop_watch = True
over_limit = False
save_failure_data = True

if '--no_time_record' in sys.argv:
	stop_watch = False
if '--over_limit' in sys.argv:
	over_limit = True
if '--no_save' in sys.argv:
	save_failure_data = False
if '-s' in sys.argv:
	case_num = int(sys.argv[sys.argv.index('-s') + 1])
runtime_result = ''
encode_t = decode_t = 0

def compile():
	global is_win
	print("compiling...")
	if is_win:
		os.system("compile.bat")
	else:
		os.system("bash compile.sh")
	return 

def rtime(run_time):
	if run_time < 7:
		return '%.4fs'%run_time
	elif run_time <10:
		return '\033[;33m%.4fs\033[0m'%run_time
	return '\033[;31m%.4fs\033[0m'%run_time

def check(case):
	dataGenerator()
	encode_decode()
	return lengthCheck() and contentCheck()

def lengthCheck():
	global is_win
	if is_win:
		os.system(".\\lengthcheck.exe")
	else:
		os.system("./lengthcheck")
	with open("minlen.u", "r") as fin:
		length = int(fin.readline())
	with open("compressed.u", "r") as fin:
		text = fin.read()
	if(length != len(text)):
		print("\n\033[;31mError\033[0m: length limit exceeded.")
		print([text], '\n', len(text), 'expected', length)
		return False
	return True

def dataGenerator():
	if is_win:
		os.system("dataGen.exe")
	else:
		os.system("./dataGen")
	return 

def encode_decode():
	global stop_watch, runtime_result, encode_t, decode_t
	runtime_result = ''
	if stop_watch:
		encode_t = -time.time()
		os.system("java HuffmanCompression input.u dictionary.u compressed.u")
		encode_t += time.time()
		decode_t = -time.time()
		os.system("java HuffmanDecompression compressed.u dictionary.u output.u")
		decode_t += time.time()
		runtime_result = '\n\t  compression: ' + rtime(encode_t) + '\n\tdecompression: ' + rtime(decode_t)
	elif is_win:
		os.system("runcode.bat")
	else:
		os.system("bash runcode.sh")

def contentCheck():
	with open("input.u", "r") as fin:
		textI = fin.read()
	with open("output.u", "r") as fin:
		textII = fin.read()
	if textI == textII :
		return True
	print("\n\033[;31mError\033[0m: content mismatched.")
	print([textI])
	print([textII])
	return False;

def changeData(length):
	with open("data.cpp", "r") as fin:
		code = fin.readlines()
	code[8] = 'int LeN = %d;\n'%length
	with open("data.cpp", "w") as fout:
		for line in code:
			fout.write(line)
	os.system("g++ data.cpp -o dataGen")
	print("\033[;32mtesting\033[0m on random input of length %d ..."%length)

def test(test_case):
	for _case in range(test_case):
		case = _case + 1
		print("Case# %-3d/%d: "%(case, test_case), end = '')
		if check(case):
			print("\033[;32mAccepted.\033[0m" + runtime_result)
		else:
			print("\nTerminated.")
			saveInput()
			exit()

def saveInput():
	if not save_failure_data:
		return 
	with open("input.u", 'r') as fin:
		content = fin.read()
	save_path = os.path.join("source", "bugdata.txt")
	with open(save_path, "w") as fout:
		fout.write(content)
	print("\033[;33mError input file saved in %s\033[0m"%save_path)
	return 

compile()
changeData(3)
test(20)
changeData(20)
test(case_num)
changeData(100)
test(case_num)
print('testing on limit data...')
changeData(1024*100)
test(5)
if(over_limit):
	changeData(1024*200)
	test(2)
	changeData(1000*500)
	test(1)
print('testing on critical data...')
for root, _, files in os.walk("critical_data"):
	for file in files:
		if file[-2:] == '.u':
			with open(os.path.join(root, file), 'r') as fin:
				content = fin.read()
			with open('input.u', 'w') as fout:
				fout.write(content)
			with open('digit.u', 'w') as fout:
				fout.write(str(len(content)) + '\n')
				for s in content:
					c = str(ord(s))
					fout.write(c + ' ')
			print("\033[;32mtesting\033[0m on file: %s"%file, end = '')
			encode_decode()
			if lengthCheck() and contentCheck():
				print("\033[;32mAccepted.\033[0m" + runtime_result)
			else:
				print("\nTerminated.")
				saveInput()
				exit()

