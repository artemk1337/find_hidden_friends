import vk_api
import private
from auth import Auth

from private import\
    Login, Password, Token,\
    database, user, password, host, port


vk = Auth(login=Login, password=Password, auth_handler=True).ImplicitFlow()

# print(vk.friends.get(user_id=139132090)['items'])

target_0 = None
target_1 = None


def rec(id, curr_d, max_d):
    t_id = []
    if curr_d == max_d - 1:
        try:
            arr = vk.friends.get(user_id=id)['items']
        except Exception as e:
            print(e)
            return 0, []
        if target_1 in arr:
            return 1, [id]
        for k in arr:
            res, t_id = rec(k, curr_d + 1, max_d)
            if res == 1:
                return 1, t_id + [id]
    elif curr_d < max_d:
        try:
            arr = vk.friends.get(user_id=id)['items']
        except:
            return 0, []
        for k in arr:
            res, t_id = rec(k, curr_d + 1, max_d)
            if res == 1:
                return 1, t_id + [id]
    return 0, []


def find(id):
    t_id = []
    arr = vk.friends.get(user_id=id)['items']
    i = 1
    if target_1 in arr:
        return [id]
    while True:
        print(i)
        for k in arr:
            print(k)
            res, t_id = rec(k, 0, i)
            if res == 1:
                return t_id + [id]
        i += 1


print(find(target_0))






