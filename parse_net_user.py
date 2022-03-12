import subprocess
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
    #print(user_list)
    return user_list

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

def str_parse(str, user_list):
    # парсим строку образца user1    user2   user3    test user
    output = str.split('       ') #7 spaces
    for i in output:
        user = spaces_deletion(i)
        if len(user)>0:
            user_list.append(user)
            print(user)
            print(get_user_sid(user))

def get_user_sid(user_name): #wmic useraccount where name='антон' get sid
    command = ["wmic","useraccount","where","name="+"'"+user_name+"'","get","sid"]
    result = subprocess.check_output(command)
    output = result.decode('cp866').split("\n")
    return spaces_deletion(output[1])
get_users()


