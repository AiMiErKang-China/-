# 程序开始之前的信息
print('版本号：'+'0.2.0\n') # 更新时请手动修改版本号

# 描述
print('只能运算最基础的 完全平方公式\n') # 更新时请手动修改描述

# 提示
print('提示：')
print('一次只能解一道题哦')
print('输入时请将 幂 写为如下格式：如 六的二次 方应写为 6^2\n')
print('注：输入不对，程序就会报错或自动退出，将需要重新启动\n')

# 列表
words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

# 前、后括号位置索引变量
qian_kh = 0
hou_kh = 0

# ^号判断变量
mi = 0

# 判断是否有字母、数字
word = False
number = True

# 题目内容
nei_rong = ''

fu_hao = 0 # 运算符的位置索引
fu_hao_n = '' # 运算符的名称

wen_ti = input('请输入你的问题：') # 输入问题

for i in range(len(wen_ti)): # 遍历字符串wen_ti
    if wen_ti[i] == '(':
        qian_kh = i
    if wen_ti[i] == ')':
        hou_kh = i
    if wen_ti[i] == '^':
        if wen_ti[i + 1] != ('+' or '-' or '*' or '/'):
            mi = '2' # 给 ^（幂）赋值

nei_rong = wen_ti[qian_kh + 1: hou_kh] # 添加括号内内容

for j in range(len(nei_rong)): # 遍历字符串nei_rong
    if j != 0:
        if nei_rong[j] == '+':
            fu_hao = j
            fu_hao_n = '+'
        elif nei_rong[j] == '-':
            fu_hao = j
            fu_hao_n = '-'
print(fu_hao_n)
num1 = nei_rong[: fu_hao] # 添加数字一内容
num2 = nei_rong[fu_hao + 1:] # 添加数字二内容

num1_bf = num1 # 备份数字一字符串
num1_bf1 = ''
num1_bf2 = ''
num1_jdz = num1[1:]
if num1[0] == '-':
    num1 = '(' + num1 + ')'
else:
    for w in words:
        if w in num1:
            num1 = '(' + num1 + ')'

num2_bf = num2 # 备份数字二字符串
num2_bf1 = ''
num2_bf2 = ''
for w in words:
    if w in num2:
        num2 = '(' + num2 + ')'

# 拆分数字和字母
for x in range(len(words)): # 遍历字母列表
    for y in range(len(numbers)): # 遍历数字列表
        if words[x] in num1: # 有字母
            if numbers[y] in num1: # 有数字
                num1_bf1 = num1_bf.strip(words[x])
                num1_bf2 = num1_bf.strip(numbers[y])
                word = True
            else: # 无数字
                num1_bf1 = num1_bf.strip(words[x])
                num1_bf2 = num1_bf.strip('-')
                word = True
                number = False
        if words[x] in num2: # 有字母
            if numbers[y] in num2: # 有数字
                num2_bf1 = num2_bf.strip(words[x])
                num2_bf2 = num2_bf.strip(numbers[y])
                word = True
            else: # 无数字
                num2_bf1 = num2_bf.strip(words[x])
                num2_bf2 = num2_bf.strip('-')
                word = True
                number = False

# 中间数字的字符串
num = ''
if word == True:
    if number == False:
        num = num1_bf1 + '2' + num1_bf2 + num2_bf2
    else:
        num = str(int(num1_bf1) * int(num2_bf1)) + num1_bf2 + num2_bf2
else:
    num = str(int(num1_bf) * int(num2_bf) * 2)
num_bf = num
num_jdz = num_bf.strip('-')
if '-' in num:
    num = '(' + num + ')'

# 输出题目
print('解题过程：')
print(' ' + wen_ti)

# 输出第一行
if word == True: # 有字母情况
    if number == True: # 有数字情况
        line1 = '=' + (num1 + '^' + mi) + fu_hao_n + num + '+' + (num2 + '^' + mi)
    else: # 无数字情况
        if '-' in num1: # 负数
            line1 = '=' + (num1 + '^' + mi) + fu_hao_n + num + '+' + (num2_bf2 + '^' + mi)
        else: # 正数
            line1 = '=' + (num1_bf2 + '^' + mi) + fu_hao_n + num + '+' + (num2_bf2 + '^' + mi)
elif word == False : # 无字母情况
    line1 = '=' + (num1 + '^' + mi) + fu_hao_n + num + '+' + (num2 + '^' + mi)
print(line1)

# 输出第二行
if word == False: # 无字母情况
    if '-' in num_bf: # 有负数情况
        if fu_hao_n == '-': # 减号
            line2 = '=' + str(int(num1_bf) ** int(mi)) + '+' + num_jdz + '+' + str(int(num2_bf) ** int(mi))
            print(line2)
        elif fu_hao_n == '+': # 加号
            line2 = '=' + str(int(num1_bf) ** int(mi)) + num_bf + '+' + str(int(num2_bf) ** int(mi))
            print(line2)
    else: # 无负数情况
        line2 = '=' + str(int(num1_bf) ** int(mi)) + fu_hao_n + num_bf + '+' + str(int(num2_bf) ** int(mi))
        print(line2)

else: # 有字母情况
    if '-' in num_bf: # 有负数情况
        if fu_hao_n == '-': # 减号
            if number == True: # 有数字情况
                line2 = '=' + (str(int(num1_bf1) ** int(mi)) + num1_bf2 + '^' + mi) + '+' + num_jdz + '+' + (str(int(num2_bf1) ** int(mi)) + '^' + mi)
                print(line2)
            elif number == False: # 无数字情况
                line2 = '=' + ( num1_bf2 + '^' + mi) + '+' + num_jdz + '+' + (num2_bf2 + '^' + mi)
                print(line2)
        elif fu_hao_n == '+': # 加号
            if number == True:
                line2 = '=' + (str(int(num1_bf1) ** int(mi)) + num1_bf2 + '^' + mi) + num_bf + '+' + (str(int(num2_bf1) ** int(mi)) + '^' + mi)
                print(line2)
            else:
                line2 = '=' + (num1_bf2 + '^' + mi) + num_bf + '+' + (num2_bf + '^' + mi)
                print(line2)
    else: # 无负数情况
        if number == True:
            line2 = '=' + (str(int(num1_bf1) ** int(mi)) + num1_bf2 + '^' + mi) + '+' + num_bf + '+' + (str(int(num2_bf1) ** int(mi)) + '^' + mi)
            print(line2)

# 输出最终结果
if word == False: # 无字母
    if number == True:
        if fu_hao_n == '-': # 减号
            print('=' + str((int(num1_bf) ** int(mi)) - int(num_bf) + (int(num2_bf) ** int(mi))))
        elif fu_hao_n == '+': # 加号
            print('=' + str((int(num1_bf) ** int(mi)) + int(num_bf) + (int(num2_bf) ** int(mi))))

# 占位行，避免窗口关闭
a = input('\n按下Enter以关闭程序')