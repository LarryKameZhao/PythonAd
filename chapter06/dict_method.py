
a = {"bobby1":{"company":"imooc"},
     "qiyue":{"company":"imooc2"}
     }




#copy返回浅拷贝
# new_dict = a.copy()
# new_dict["bobby1"]["company"]="imooc3"
pass

import copy

new_dict = copy.deepcopy(a)
new_dict["bobby1"]["company"]="imooc3"


newdic = dict.fromkeys(new_dict,{'company':'immooc'})
print(newdic)
#get默认值为空
# value = new_dict.get("bobby1")
# print(value)
#
# default_value = newdic.setdefault("bobby","msft")
# print(newdic)
# newdic.update([('bobby','orcl')])
# print(newdic)

user_dict = {}

users = ["b1","b2","b1","b3","b4","b1"]

# for user in users:
#     if user not in user_dict:
#         user_dict[user] =1
#     else:
#         user_dict[user] +=1

from collections import defaultdict

# for user in users:
#     user_dict.setdefault(user,0)
#     user_dict[user] += 1




default_dic = defaultdict(int)

for user in users:
     default_dic[user] += 1

print(default_dic)

def gen_default():
     return {
          'name':'b1',
          'num':0
     }
default_dic =defaultdict(gen_default)
default_dic['group']
print(default_dic)