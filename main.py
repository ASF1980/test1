import os


# функция для подчета
def calculateFileSizes(folder_path):
	# изначальный размер всех файлов
	total_size = 0
	file_sizes = []

	for path, dirs, files in os.walk(folder_path):
		for f in files:
			fp = os.path.join(path, f)
			total_size += os.path.getsize(fp)
			file_sizes.append((f, os.path.getsize(fp)))

	return total_size, file_sizes


result = calculateFileSizes("C:/test")
total_size = result[0]
file_sizes = result[1]
# переворачиваем массив
file_sizes.sort(key=lambda x: x[1], reverse=True)

# вывод на экран
print(f"Весь размер каталога: {total_size} кБ")
print("----------")
for file, size in file_sizes:
	print(f"Размер {file} - {size} кб")

# # указываем размер
# size = 0

# # указывем калог для подсчета
# Folderpath = 'C:/Test/'

# # получаем размер
# for path, dirs, files in os.walk(Folderpath):
# 	for f in files:
# 		fp = os.path.join(path, f)
# 		size += os.path.getsize(fp)

# # выводим на экран
# print("Размер каталога: " + str(size))
# directory = r'.'
# groups = [1000, 10000, 100000, 1000000]
# groups += [float("inf")]
# result = dict.fromkeys(groups, 0)

# # обходим всю иерархию подкаталогов
# for path_from_top, subdirs, files in os.walk(directory):
# 	for file in files:
# 		path = os.path.join(path_from_top, file)
# 		size = os.path.getsize(path)
# # вычисляем ближайшее большее число
# to_group = min(filter(lambda x: size < x, groups))
# result[to_group] += 1
# prev_size = 0
# for size in groups:
# 	print(f"Файлов размером (байт) от {prev_size:10} до {size:10} : {result[size]}")
# 	prev_size = size
# 	path = "C:/Test/"
# 	fun = lambda x : os.path.isfile(os.path.join(path,x))
# 	files_list = filter(fun, os.listdir(path))

# # создаем лист информации с рамерами
# size_of_file = [
# (f,os.stat(os.path.join(path, f)).st_size)
# for f in files_list
# ]
# # вывод на экран
# for f,s in size_of_file:
# 	print("{} : {}MB".format(f, round(s/(1024*1024),3)))
# def file_info(filename, flags):
# 	file_binary = "/usr/bin/file"
# 	(file_stdout, file_stderr) = subprocess.Popen( \
# 	[file_binary, flags, filename], \
# 	stdout=subprocess.PIPE,\
# 	stderr=subprocess.PIPE).communicate()
# 	return file_stdout.split(",")[0].strip('\n')


# def sizeof_fmt(num, readable):
# 	if not readable:
# 		return num

# a = "b"
# for x in ['bytes','KB','MB','GB','TB']:
# 	if sum < 1024.0:
# 		a = f"{sum} {x}"
# 	sum /= 1024.0