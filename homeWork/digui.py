import  math
def jiecheng(x):
    if x == 1 :
        return 1
    else:
        return x*jiecheng(x-1)
# print(jiecheng(int(input("请输入数字:"))))



# #递归十进制转2进制
# def Dec2Bin(dec):
#  2     result = ''
#  3
#  4     if dec:
#  5         result = Dec2Bin(dec//2)
#  6         return result + str(dec%2)
#  7     else:
#  8         return result
#  9
# 10 print(Dec2Bin(62))
#
# def Dec2Bin(dec):
#     result = ''
#     if dec :
#         result = Dec2Bin(dec//2)
#         return result + str(dec%2)
#     else:
#         return result
# # print(Dec2Bin(int(input("请输入数字:"))))
#
#
# def askAge(n):
#     if n -1 == 0:
#         return 10
#     else:
#         return 2 + askAge(n-1)
#
# print(askAge(5))


# 数学宝塔
# 1、数学宝塔，从最顶上走到最底层，每次只能走到下一层的左边或右边的数字，求出使所走到的所有数字之和为60的途径。
#         7                         1
#        4  6                       2
#       6  9  3                     3
#      6  3  7  1                   4
#     2  5  3  2  8                 5
#    5  9  4  7  3  2               6
#   6  4  1  8  5  6  3             7
#  3  9  7  6  8  4  1  5           8
# 2  5  7  3  5  7  8  4  2         9


list = [[7],[4,6],[6,9,3],[6,3,7,1],[2,5,3,2,8],[5,9,4,7,3,2],[6,4,1,8,5,6,3],[3,9,7,6,8,4,1,5],[2,5,7,3,5,7,8,4,2]]
def mathjzt(x,crtIndex,zcount,sr):
    'x 表示行数  y表示该行中第一个数的index  z该数值'
    listLength = len(list)
    if x == 0:
        for i in range(2):
            crtStr = "左" if i == 0 else "右"
            tempSr =  str(x) + crtStr
            sumCount = list[0][0]
            mathjzt(x+1,0+i,sumCount,tempSr)
    elif x == listLength -1:
        # print('++')
        # for i in range(2):
        #     crtStr = "左" if i == 0 else "右"
        # tempSr =  sr + str(x) + crtStr
        sumCount = list[x][crtIndex] + zcount
            # print('***' + sr + '*****' + str(sumCount))
        if sumCount == 60:
            print(sr+'==='+str(sumCount))
    else:
        for i in range(2):
            crtStr = "左" if i == 0 else "右"
            tempSr =  sr + str(x) + crtStr
            sumCount = list[x][crtIndex] + zcount
            mathjzt(x+1,crtIndex+i,sumCount,tempSr)
mathjzt(0,0,0,'')