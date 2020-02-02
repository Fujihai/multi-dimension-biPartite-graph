import json
import random
from random import choice

# 预期数据
# [
#   {
#     'sex': '男'，
#     'city': '北京',
#     'age': '1至44岁'，
#     'pv': 'xxxx',
#     'uv': 'xxxx',
#     'vv': xxxx
#   }
#   ...
# ]

# 城市
city_arr = ['北京', '深圳', '广州', '成都', '杭州', '武汉', '天津', '南京' ]

# 性别
sex_arr = ['男', '女', '未知']

# 年龄段
age_arr = ['18岁以下', '1至18岁', '19至30岁', '31至45岁', '46至60岁', '61岁以上']

# 最大记录条数
max_count_size = 10000

# 随机区间范围内数值生成
def random_value(min, max):
  if(min < 0 or max < 0 or max < min):
    return
  return random.randint(min, max)

results = []

# 目标数据生成
for i in range(max_count_size):
  record = {
    'sex': choice(sex_arr),
    'city': choice(city_arr),
    'age': choice(age_arr),
    'pv': random_value(1, 10000),
    'vv': random_value(1, 500)
  }
  results.append(record)

# print(results)

f = open('results.json', 'w')
f.write(json.dumps({"data": results}))
f.close()