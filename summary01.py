"""
1.如何在列表、字典、集合中筛选数据
2.根据字典中值的大小，对字典中的项进行排序
3.统计序列中元素的频度,并取出出现频率前三高的元素
4.快速找到多个字典中的公共键
5.如何让字典保持有序
6.如何实现用户的历史记录功能（最多n条）
"""
# 1
import random
list1 = [random.randint(-10,10) for _ in range(20)]
# 筛选list1中小于0的所有数据。可以使用列表解析进行筛选，也可以使用filter函数进行筛选
res1_list1 = [i for i in list1 if i < 0]
res1_list2 = filter(lambda x:x<0,list1)
# 过滤字典,得到分数在90分以上的同学
dic = {k:random.randint(60,100) for k in 'abcdefg'}
res_dic = {k:v for k,v in dic.items() if v > 90}
# 使用filter过滤
res_dic2 = filter(lambda item:item[1]>90,dic.items())
# 集合的过滤方法和列表差不多，代码就不写了

# 2
#  有多种方法，第一种是将字典转换成元祖。然后使用列表解析+sorted函数或者使用zip函数+sorted得到解
            #  第二种是通过py内置的sorted函数
d = {k:random.randint(60,100) for k in 'abcdefg'}
l = [(v,k) for k,v in d.items()]  # 使用列表解析将字典转成列表套元祖的格式
sorted(l)
l2 = list(zip(d.values(),d.keys()))  # 使用zip函数将字典转成列表套元祖的格式
res2 = sorted(l2)

res = sorted(d.items(),key=lambda x:x[1])  # 使用sorted函数一步到位 ,res即为排好序的字典
#  如果现在需要返回排好序字典的名次呢？  ---- 可以使用enumerate函数
list(enumerate(res,1))
#  如果一个列表套元祖的列表是  [(81, 'e'), (88, 'c'), (94, 'g'), (95, 'b'), (95, 'f'), (98, 'a'), (98, 'd')]
# 我想把它转换成字典，同时字母作为key，数字作为value应该怎样操作呢
tup =[(81, 'e'), (88, 'c'), (94, 'g'), (95, 'b'), (95, 'f'), (98, 'a'), (98, 'd')]
res_tup = {i[1]:i[0] for i in tup}

# 3
# 有多种方法，可以将序列转化为字典（key为序列中的元素，value为频度）。还可以使用collections中的Counter函数
data = [random.randint(0,20) for _ in range(30)]
dic = {}
dic = dic.fromkeys(data,0)
for i in data:
    dic[i] += 1 # 之后再按着2结束的方法排序取前3就好了
# 按照2排序取前3的方法效率不高，可以采用堆排序提高效率
import heapq
heapq.nlargest(3,((v,k) for k,v in dic.items()))

from collections import Counter   #  使用Counter库
res3 = Counter(dic)
res3.most_common(3)

# 4  有多种方法，最容易想到的肯定是一个一个遍历，一个一个找
d1 = {k:random.randint(1,3) for k in random.sample('abcdefgh',3)}
d2 = {k:random.randint(1,3) for k in random.sample('abcdefgh',3)}
d3 = {k:random.randint(1,3) for k in random.sample('abcdefgh',3)}
res4 = []
for i in d1:
    if (i in d2) and (i in d3):
        res4.append(i)
# 上面这种写法有一个问题，就是如果d的数量很大，第二行的if代码要无限写下去
#  换一种方法
dl = [d1,d2,d3]
res4_2 = [k for k in dl[0] if all(map(lambda x:k in d,dl[1:]))]
# 还可以使用集合的交集操作获取字典的公共键
# 可以使用集合的交集操作获取字典的公共键
# step1 : 使用字典的keys（）方法，得到一个字典的keys的集合
# step2： 使用map函数，得到每个字典keys的集合
# step3 ： 使用reduce函数，取所有字典的keys集合的交集
from functools import reduce
res4_3 = reduce(lambda a,b:a&b,map(dict.keys,dl))

# 5
# python3.6之前的字典是无序的 python3.6之后的字典都是有序的
from collections import OrderedDict
od = OrderedDict()
players = list('abcdefg')
random.shuffle(players)
for i,p in enumerate(players):
    od[p] = i
print(od)
# 再来介绍一个islice的函数，可以返回指定顺序的元素
from itertools import islice
#  比如返回一个列表中排名第3-6位的元素
l = [i for i in range(10)]
islice_list = list(islice(l,3,6))
print(islice_list)
# 实现一个函数，功能为按照字典的名次来查找
def query_by_order(d,a,b = None):
    a -= 1
    if b is None:
        b = a+1
    return list(slice(d,a,b))

#  6  如何实现用户的历史记录功能（最多n条)
# 解决方案： 使用容量为n的双端队列（deque）存储历史记录
# 双端队列：左右两端都可以进/可以出的队列
from collections import deque
q = deque([],5)
n = random.randint(0,10)
q.append(n)
