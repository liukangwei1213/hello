#encoding:utf-8


'''
def changeme( mylist ):

   "修改传入的列表"
   mylist.append([1,2,3,4])
   print("函数内取值: ", mylist)
  
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print("函数外取值: ", mylist)
'''

#斐波那契
'''
def FIB(n):
    zhi=[0,1]
    for i in range(n-2):
        zhi.append(zhi[-2]+zhi[-1])
    return zhi
print(FIB(10))
'''

# 取最大值
'''
def zuidazhi(a,b):
    return max(a,b)
print(zuidazhi(10,8))
'''



import requests
import re

def con(url):
   for i in url:
      rea_one = requests.get(i).content.decode('gbk')
      # print(rea_one)
      re_one= re.compile('<td class="L"><a href="(.*?)" title="(.*?)">(.*?)</a><a href="(.*?)" target="_blank">(.*?)</a></td>',re.S)
      lis_one = re_one.findall(rea_one)
      for i in lis_one:
         print(i)


def page():
   lis = []
   for i in range(1,100):
      name = 'http://www.x23us.com/class/1_'+str(i)+'.html'
      print(name)
      lis.append(name)
   return lis

def omian():
   aa = page()
   con(url=aa)

omian()




'''
def lkw(n):
   print('sb',n)

def dsb():
   name = input('Are you an idiot?')
   return name

def omain():
   n = dsb()
   print(n)
   lkw(n)
omain()
'''