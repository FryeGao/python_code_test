"""
1.如何拆分含有多种分隔符的字符串
2.判断字符串a是否以字符串b开头或者结尾
3.如何调整字符串中文本的格式
4.如何将多个小字符串拼接成一个大字符串
5.如何对字符串进行左、右、居中对齐
6.如何去掉字符串中不需要的字符1
"""
# 1 s = 'ab;cd|efg|hi,jkl|mn\top'  ==》 'abcdefghijkmntop'
# 解决方法1：连续使用str.split()方法，每次处理一种分隔符号
# split后会返回一个list ，再对结果进行循环遍历和切割，会返回一个二维列表，这样维度会很大
#  所以可以考虑先新建一个空列表，然后使用extend函数进行拼接，或者使用sum求和，但是初值要改成一个[]
def my_split(s:str,seps:list):
    res = [s]
    for sep in seps:
        t = []
        list(map(lambda ss:t.extend(ss.split(sep)),res))
        res = t
    return res
# 解决方法2：使用正则表达式中的split(可以一次性切割多个字符串)
import re
s = 'ab;cd|efg|hi,jkl|mn\top'
re.split("[:|\t,]+",s)

# 2
# 解决方法：可以使用startswith() 和 endswith() 对字符串进行判断 (匹配多个字符串时传入元祖)
str2 = 'Class_Solution.py'
str2.startswith('Class')
str2.startswith('.py')
str2.startswith(('.py','.java'))

# 3
# 把软件中的log文件其中的日期格式改变 'yyyy-mm-dd' ==》 'mm/dd/yyyy'
# 2016-05-21 10:39:26 status unpacked
# 2016-05-23 10:49:25 status half
# 解决方法：可以使用正则表达式 re.sub() 方法对字符串替换。利用re的捕获组，捕获每个部分内容
import re
log = open('')
res = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\2/\3/\1',log)

# 4
# 方案1：迭代列表，将每个小字符串使用‘+’拼接每一个字符串
l4 = ['abc','def','ghi']
res4 =''
for i in l4:
    res += i
# 方案2 ：使用str中的join方法
"".join(l4)

# 5
# 方案1：使用字符串中的str.ljust(), str.rjust() , str.center() 进行左右居中对齐
s5 = 'abc'
s5.ljust(10)
len(s5.ljust(10))  # 验证s5的长度，为10
s5.ljust(10,'*')  #  指定*，表示abc之后的(10-3)个空白，使用7填充
# 方案2：使用format函数
format(s5,'<10')  # 'abc       '

# 6
    # 可以使用strip,lstrip,rstrip去掉两端字符
    # 删除单个固定位置的字符，可以使用切片+拼接的方式
    # 字符串的replace方法或者正则表达式re.sub()删除任意子串
    # 字符串的translate方法，可以同时删除多个不同字符

