import re
import urllib.request
#
s = r't[io]p'
result = re.findall(s, 'tip top twp teq tpp')
print(result)

s = r't[^io]p'
result = re.findall(s, 'tip top twp teq tpp tgp')
print(result)
#start of the line
s = r'^hello'
result = re.findall(s, 'hello world, hello boy')
print(result)
#end of the line
s = r'boy$'
result = re.findall(s, 'hello world, hello boy')
print(result)

#元字符：
#. ^ $ * + ? {} {} \ | ()
#元字符在字符集中不起作用： 比如[akm$], 这个时候$不再表示结尾
#但是有个例外，当^出现在[]里开始位置时，
#表示补集匹配不在此范围内的字符，比如[^abc]，表示除了abc外其他字符
s = r't[abc$^]'
#此时$不再表示结尾
#^不在开始，只是表示匹配这个字符，所以下面例子会找到2个串
result = re.findall(s, 'tax tbb t$a t^1234 t^^')
print(result)

s = r'x[0-9]x'
result = re.findall(s, 'xxx xbc x0x x1x')
print(result)

#\本身是转义字符
#但是有特殊用法：
#\d匹配任何十进制数，相当[0-9]
#\D匹配任何非数字字符，相当[^0-9]
#\w匹配任何字母数字字符，相当[a-zA-Z0-9_]
#\W匹配任何非字母数字字符，相当[^a-zA-Z0-9_]

#{}表示重复
#比如电话号码
r = r'^755-\d{8}'
result = re.findall(r, '755-12345678')
print(result)

# * 用法
#指定前一个字符可以被匹配0次或多次
r = r'a[bcd]*x'
result = re.findall(r, 'abbcddxxxabcddsceaxv')
print(result)
r = r'^755-*\d{8}$'
result = re.findall(r, '755-12345678')
print(result)
r = r'^755-*\d{8}$'
result = re.findall(r, '755-123456789')
print(result)
r = r'^755-*\d{8}$'
result = re.findall(r, '75512345678')
print(result)
#出问题了，- 我只希望出现一次或者没有，但是用* 可以匹配多个,所以应该用?
r = r'^755-*\d{8}$'
result = re.findall(r, '755--12345678')
print(result)

#？ 用法
#匹配一次或0次，即表示可选
r = r'^755-?\d{8}$'
result = re.findall(r, '755--12345678')
print(result)
result = re.findall(r, '755-12345678')
print(result)
result = re.findall(r, '75512345678')
print(result)
#最小匹配，非贪婪模式
r=r'ab+'
result = re.findall(r, '755--12345678')
print(result)
# + 用法
# 指定前一个字符可以被匹配1次或多次
r = r'a[bcd]+x'
result = re.findall(r, 'abbcddxxxabcddsceaxv')
print(result)

#贪婪匹配，匹配尽量多
r = r'ab+'
result = re.findall(r, 'abbbbbb')
print(result)

#最小匹配，非贪婪模式
r = r'ab+?'
result = re.findall(r, 'abbbbbb')
print(result)

#{m,n}
#m和n是整数，表示至少m次重复，至多n次重复
#如果忽略m，会认为至少0次重复
#忽略n，可以无限次重复
#{0,}等于*作用，{1,}等于+, 而{0,1}等于?
r = r'a{1,3}'
result = re.findall(r, 'ab')
print(result)
result = re.findall(r, 'aaab')
print(result)
result = re.findall(r, 'aaaab')
print(result)

#编译成对象，运行速度提升
p_r = re.compile(r)
print(p_r)
result = p_r.findall('aaab')
print(result)

#忽视大小写
p_r = re.compile(r'csvt', re.I)
result = p_r.findall('CSVT csvt CsVt cSvT')
print(result)

#RE里的函数
#match() ：在字符串开始位置匹配
#search(): 扫描字符串，找到匹配的位置
#findall(): 找到所有子串，作为列表返回
#finditer(): 找到所有子串，作为迭代器返回
result = p_r.match('CSVT123')
if result:
    print(result.group())
result = p_r.match('abCSVT123')
if result:
    print(result.group())
else:
    print(result)

result = p_r.search('abCSVT123')
print(result)

result = p_r.finditer('CSVT csvt CsVt cSvT')
print(result)
for i in result :
    print(i.group())

#原始的替换方法，不涉及正则表达式
s = 'hello csvt'
s.replace('csvt', 'python')
print(s)

#用正则方式替换
p_r = re.compile(r'c..t')
s = p_r.sub('python', 'csvt ccct cavt cdcc')
print(s)

#非正则切割, 只能指定一个切割符
ip = '1.2.3.4'
s = ip.split('.')
print(s)

#正则切割, 可以指定多个切割符
ip = '1.2.3.4'
p_r = re.compile(r'\.')
s = p_r.split(ip)
print(s)

ip = '1+2-3*4'
p_r = re.compile(r'[\+\-\*]')
s = p_r.split(ip)
print(s)

#.通常不匹配换行符\n等
#如果要匹配的话，需要用到 re.S
ip = 'csvt\nhello'
p_r = re.compile(r'csvt.hello')
s = p_r.findall(ip)
print(s)

s = p_r.findall(ip, re.S)
print(s)

r1 = r"csvt.hello"
s = re.findall(r1, ip, re.S)
print(s)

# M: 多行匹配，影响^和$
str = 'hello csvt\ncsvt hello\nhello csvt hello\ncsvt hehe'
r = r'^csvt'
s = re.findall(r, str)
print(s)

s = re.findall(r, str, re.M)
print(s)

# X: 能够使用正则的verbose状态，使得被组织得更清晰易懂
r = r'''\d{3,4}
    -?
    \d{8}$'''
s = re.findall(r, '0755-12345678')
print(s)
print(r)
s = re.findall(r, '0755-12345678', re.X)
print(s)

# ()：分组
email = r"\w{3}@\w+(\.com|\.cn|\.org)"
s = re.match(email, 'abc@jstao2000.cn')
if s:
    print(s.group())
else:
    print(s)
# 注意findall也是匹配整个正则表达式，但是只返回()里的数据
s = re.findall(email, 'abc@jstao.com')
print(s)
#比如：
str = '''fdsakjf
df hello src=csvt yes sjal
kfjdad src=123 yes dfkg
src=234 yes
hello src=python yes ksa
'''
print(str)
r1 = r'hello src=.+ yes'
s = re.findall(r1, str)
print(s)
#如果我们只想返回=后面的值，那么可以用()的方法
r1 = r'hello src=(.+) yes'
s = re.findall(r1, str)
print(s)

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'img class=\"BDE_Image\" src="(.*?\.jpg)" size'
    imgre = re.compile(reg)
    html = html.decode('utf-8')  # python3
    imglist = re.findall(imgre, html)
    return imglist


