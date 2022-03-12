
import winreg, subprocess, sys

def spaces_deletion(str):
    string = ''
    ind = 0
    for i in str.split():
        if ind > 0:
            string = string +' '+i.strip()
        else:
            string = string + i.strip()
        ind = ind +1
    return string

def get_users():
    result = subprocess.check_output(['net', 'user'])
    output = result.decode('cp866').split("\n")
    user_list = []
    ind = 4
    while ind != len(output):
        if output[ind].find('Команда выполнена успешно.') == 0:
            break
        else:
            str_parse(output[ind],user_list)
        ind = ind +1
    return user_list

def str_parse(str, user_list):
    # парсим строку образца user1    user2   user3    test user
    output = str.split('       ') #7 spaces
    for i in output:
        user = spaces_deletion(i)
        if len(user)>0:
            user_list.append(user)

def get_user_sid(user_name): #wmic useraccount where name='антон' get sid
    command = ["wmic","useraccount","where","name="+"'"+user_name+"'","get","sid"]
    result = subprocess.check_output(command)
    output = result.decode('cp866').split("\n")
    return spaces_deletion(output[1])

def user_info(path_to_file):
    file = open(path_to_file,'w')
    for u in get_users():
        sid = get_user_sid(u)
        subkey = r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+'\\'
        subkey = subkey + sid
        try:
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,subkey)
            ProfileImagePath = winreg.QueryValueEx(key, "ProfileImagePath")[0]
        except:
            ProfileImagePath = ''
        file.write('*****'+ '\n')
        file.write('<1>'+u + '\n')                                    # 1 user name
        file.write('<2>'+sid+ '\n')                                # 2 user sid
        file.write('<3>'+ProfileImagePath+ '\n')                      # 3 user profile path
        result = subprocess.check_output(['net', 'user', u])
        output = result.decode('cp866').split("\n")
        for i in output:
            if i.find('Полное имя') == 0:
                txt = i.replace('Полное имя','')
                file.write('<4>'+spaces_deletion(txt)+ '\n')           # 4 user full name
            elif i.find('Комментарий  ') == 0:
                txt =i.replace('Комментарий', '')
                file.write('<5>'+spaces_deletion(txt) + '\n')          # 5 user comment
            elif i.find('Учетная запись активна') == 0:
                txt =i.replace('Учетная запись активна', '')
                file.write('<6>'+spaces_deletion(txt) + '\n')          # 6 user active
            elif i.find('Последний пароль задан') == 0:
                txt =i.replace('Последний пароль задан', '')
                file.write('<7>'+spaces_deletion(txt) + '\n')          # 7 user last time password set
            elif i.find('Последний вход') == 0:
                txt =i.replace('Последний вход', '')
                file.write('<8>'+spaces_deletion(txt) + '\n')          # 8 user last time system login
            elif i.find('Членство в локальных группах') == 0:
                txt =i.replace('Членство в локальных группах', '')
                file.write('<9>'+spaces_deletion(txt) + '\n')          # 9 user groups membership
        #file.write('**********')
    file.close()

try:
    do_not_continue = False
    path_to_file = sys.argv[1]     # Путь к файлу для выгрузки данных sys.path[1]+'\\user_data.txt'#
    if path_to_file == 'help':
        print('Параметры для работы парсера: 1. Полный путь к файлу')
        do_not_continue = True # прервать выполнение кода
except :
    print('Не введены параметры работы. Выполните с параметром help для получения описания')   # Если что-то не так вываливаемся в исключение и выключаемся
    do_not_continue = True # прервать выполнение кода

if do_not_continue == False:
    user_info(path_to_file)
    #get_user_info(path_to_file)
    file_flg = sys.argv[2] #sys.path[1]+'\\work_done.txt'#
    flg = open(file_flg, "w")
    flg.write(' ')
    flg.close()



