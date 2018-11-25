# 10.3.5  处理FileNotFoundError 异常

filename = 'alice.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)	
# 10.3.6 分析文本
else:
	# 计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + 
		" words.")
	
	

