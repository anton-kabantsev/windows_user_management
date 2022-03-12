import os, sys, get_user_info

def scan_dir(dir):
    #os.chdir(initial_dir)
    for root, dirs, files in os.walk(dir, topdown=True,onerror=None,followlinks=True):
       for name in dirs:
         sys.path.append(dir+'\\'+name)
         scan_dir(dir+'\\'+name)
         # dct[ind] = os.path.join(root, name)
         # ind = ind + 1

scan_dir(sys.path[1])#('C:\\Users\\Антон\\AppData\\Local\\Temp\\python')
#rint(sys.path)

path_to_file = ''
do_not_continue = False
#  первым делом парсим ввод коммандной строки
try:
    path_to_file = sys.path[1]+'\\user_data.txt'#sys.argv[1]     # Путь к файлу для выгрузки данных
    if path_to_file == 'help':
        print('Параметры для работы парсера: 1. Полный путь к файлу')
        do_not_continue = True # прервать выполнение кода
except :
    print('Не введены параметры работы. Выполните с параметром help для получения описания')   # Если что-то не так вываливаемся в исключение и выключаемся
    do_not_continue = True # прервать выполнение кода

if do_not_continue == False:
    get_user_info.user_info(path_to_file)
    #get_user_info(path_to_file)
    file_flg = sys.path[1]+'\\work_done.txt'#sys.argv[2]
    flg = open(file_flg, "w")
    flg.write(' ')
    flg.close()
    print(path_to_file)

