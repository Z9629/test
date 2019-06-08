'''numpy学习笔记'''
import numpy as np
'''# a=np.array([[[1,2,3,4],[2,3,4,5,]],[[3,4,5,6],[4,5,6,7]]])
# 
# print(a)
# a=a.transpose((0,1,2))
# print(a)'''

# a=np.array([1,2,3,4,5,6])       #创建numpy数组
# print(type(a))                  #类型
# print(a)
# print(a.shape)                  #数组长度
# print(a.reshape((2,-1)))
# a=a.reshape((2,-1))             ##2行3列
#
# print(a.shape)
# print(a)
# print(a.reshape(-1,2))          #3行2列

# a=np.array([[1,2,3,4],[2,3,4,5],[3,4,5,6]])
# print(a.shape)
# b=a[2,1]
# print(b)                  #只有元素，没有维度数组
# print(b.shape)            #()
# c=a[2:,1:2]
# print(c)
# print(c.shape)
'''结果：<class 'numpy.ndarray'>
[1 2 3 4 5 6]
(6,)
[[1 2 3]
 [4 5 6]]
(2, 3)
[[1 2 3]
 [4 5 6]]
 
 [[1 2]
 [3 4]
 [5 6]]
 
 
 (3, 4)
4
()
[[4]]
(1, 1)
'''
'''np.zeros,np.ones函数创建全为0，1的几行几列数组
np.full函数创建几行几列全为几的数组'''
# one_int = np.zeros((2,3))
# print(one_int)
# two_int = np.full((2,3),2)
# print(two_int)

# three_int = np.eye(3)       #np.eye函数产生一个3行3列的单位矩阵，对角线为1，其余元素为0
# print(three_int)
#
# four_int = np.random.random((3,4))      #np.random.random 函数产生一个3行4列的随机元素数组
# print(four_int)
'''[[0. 0. 0.]
 [0. 0. 0.]]
 
 [[2 2 2]
 [2 2 2]]
 
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
 
 [[0.02639814 0.7932826  0.9045047  0.58085109]
 [0.34476854 0.97325657 0.52372065 0.3726084 ]
 [0.73079517 0.31081164 0.38004675 0.92505706]]'''

'''numpy的索引'''
# arr =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(arr)
# arr_change = arr[-2:,1:3]       #从倒数第二行开始向下，选取[1:3]的列
# print(arr_change)


# arr[np.arange(3),1] += 10       #[0,1,2]是行，1是列  ，相当于arr[[0,1,2],[1,1,1]] += 10
# print(arr)
#
# resulet_index = arr>10          #判断条件
# print(resulet_index)            #判断
# print(arr[resulet_index])       #提取判断结果数据组成列表




'''结果：[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
[[ 6  7]
 [10 11]]
 
 
 [[ 1 12  3  4]
 [ 5 16  7  8]
 [ 9 20 11 12]]
 
 
 
 [[False  True False False]
 [False  True False False]
 [False  True  True  True]]
[12 16 20 11 12]'''


'''元素的数据类型'''
# a = np.array([1,2])
# print(a.dtype)              #a.dtype 函数判断数组a当中是什么数据类型
#
# b = np.array([1.1,2.2])
# print(b.dtype)
#
# c = np.array([1.1,2.6])     #指定c数组当中元素的数据类型为int
# c.dtype=np.int64
# print(c.dtype)

'''结果：int32
float64
int64'''



'''数组运算与常用函数'''

'''np.add(a,b) 相当于 a+b
np.subtract(a,b)相当于a-b
np.multiply(a,b) 相当于 a*b 对应位置相乘
np.divide(a,b) 相当于 a/b 对应位置相除
np.sqrt(a) 元素开方
以上仅仅是对应元素的（相同数组大小下）运算操作'''

# a=np.array([[1,2],[3,4]])
# b=np.array([[5,6],[7,8]])
# print(a+b)



#矩阵相乘
# a = np.array([[1,2,3],[4,5,6]])
# b = np.array([[1,2],[3,4]])
# # c = a.dot(b)
# print(b.dot(a))

'''
a.dot(b)不对，左边的元素列数必须要与右边元素的的行数相同
结果：[[ 9 12 15]
 [19 26 33]]
'''



#常用函数
#sum函数：对数组元素进行求和操作

# a = np.array([[1,2],[3,4]])
# print(np.sum(a))                #所有元素相加
#
# print(np.sum(a,axis=0))         #axis=0时，对列进行操作
# print(np.sum(a,axis=1))         #axis=1时，对行进行操作

'''结果：
10
[4 6]
[3 7]'''

#mean函数：求数组中所有元素的平均值

# a = np.array([[1,2],[3,4]])
# print(np.mean(a))
# print(np.mean(a,axis=0))        #axis=0时，对列进行操作，[(1+3)/2,(2+4)/2]
# print(np.mean(a,axis=1))        #axis=1时，对行进行操作，[(1+2)/2,(3+4)/2]


'''结果：2.5
[2. 3.]
[1.5 3.5]'''



#uniform函数：取随机数
# a = np.random.uniform(3,4)      #产生一个3,4之间的一个随机数
# print(a)

'''结果：3.8870728229062985
'''

#tile函数：以数组本身为一个元素输出一个数组
# a = np.array([[1,2],[3,4]] )
# print(np.tile(a,(1,2)))         #以数组a为一个整体输出一行两列的a


'''结果：[[1 2 1 2]
 [3 4 3 4]]'''


#argsort函数：将数组按由小到大的顺序排列数组元素所对应的位置
#
# a = np.array([[1,13,36,29],[10,4,8,2]])
# print(a.argsort())


'''结果：[[0 1 3 2]
 [3 1 2 0]]'''



#矩阵转置

# a = np.array([[1,4,2,7],[13,23,45,55]])
# print(a.T)
#或np.transpose(a)


'''结果：[[ 1 13]
 [ 4 23]
 [ 2 45]
 [ 7 55]]'''


#广播

a = np.array([[1,2,3],[2,3,4],[12,23,34],[2,6,7]])
b = np.array([1,2,3])
'''循环法'''
# for i in range(4):
#     a[i, : ] += b       #数组a的每一行都与数组b相加
# print(a)

'''结果：[[ 2  4  6]
 [ 3  5  7]
 [13 25 37]
 [ 3  8 10]]'''

'''使用tile函数'''
# c = a + np.tile(b,(4,1))
# print(c)

'''#结果：[[ 2  4  6]
 [ 3  5  7]
 [13 25 37]
 [ 3  8 10]]'''

#广播
print(a + b)

'''结果：[[ 2  4  6]
 [ 3  5  7]
 [13 25 37]
 [ 3  8 10]]'''




















