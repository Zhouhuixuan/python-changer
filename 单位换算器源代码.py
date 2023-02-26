import time
import math
time.sleep(0.5)
print('这是一个单位换算器，by Huixuan，输入start可继续使用')
a=(input(''))
time.sleep(1)
if a=='start':
        print("------------------------------------------------------------------------------------------------------------------------------")
        print('GitHub地址https://github.com/Zhouhuixuan/python-changer')
        #正文
print()
print('1.长度')
print('2.面积')
print('3.重量')
print('4.温度（正在制作）')
print()
time.sleep(1)
while True:
    print()
    ask=input('选择单位，输入quit退出')
    #长度
    if ask=='1':
        print()
        print('1.厘米')
        print('2.分米')
        print('3.米')
        print('4.千米')
        print()
        ask1=input('请选择第一个长度单位(序号)：')
    
        if ask1=='1':
            print()
            print('你选择了 厘米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='2':
                print()
                print(ask3,'厘米等于',ask3/10,'分米')
                time.sleep(1)

            if ask4=='3':
                print()
                print(ask3,'厘米等于',ask3/100,'米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'厘米等于',ask3/100000,'米')
                time.sleep(1)

        if ask1=='2':
            print()
            print('你选择了 分米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'分米等于',ask3*10,'厘米')
                time.sleep(1)

            if ask4=='3':
                print()
                print(ask3,'分米等于',ask3/10,'米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'分米等于',ask3/10000,'千米')
                time.sleep(1)

        if ask1=='3':
            print()
            print('你选择了 米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'米等于',ask3*100,'厘米')
                time.sleep(1)

            if ask4=='2':
                print()
                print(ask3,'米等于',ask3*10,'分米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'米等于',ask3/1000,'千米')
                time.sleep(1)

        if ask1=='4':
            print()
            print('你选择了 千米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'千米等于',ask3*100000,'厘米')
                time.sleep(1)

            if ask4=='2':
                print()
                print(ask3,'千米等于',ask3*10000,'分米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'千米等于',ask3*1000,'米')
                time.sleep(1)
#面积
    if ask=='2':
        print()
        print('1.平方厘米')
        print('2.平方分米')
        print('3.平方米')
        print('4.平方千米')
        print()
        ask1=input('请选择第一个面积单位(序号)')
    
        if ask1=='1':
            print()
            print('你选择了 平方厘米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='2':
                print()
                print(ask3,'平方厘米等于',ask3/100,'平方分米')
                time.sleep(1)

            if ask4=='3':
                print()
                print(ask3,'平方厘米等于',ask3/10000,'平方米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'平方厘米等于',ask3/10000000000,'平方千米')
                time.sleep(1)

        if ask1=='2':
            print()
            print('你选择了 平方分米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'平方分米等于',ask3*100,'平方厘米')
                time.sleep(1)

            if ask4=='3':
                print()
                print(ask3,'平方分米等于',ask3/100,'平方米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'平方分米等于',ask3/100000000,'平方千米')
                time.sleep(1)

        if ask1=='3':
            print()
            print('你选择了 平方米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'平方米等于',ask3*10000,'平方厘米')
                time.sleep(1)

            if ask4=='2':
                print()
                print(ask3,'平方米等于',ask3*100,'平方分米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'平方米等于',ask3/1000000,'平方千米')
                time.sleep(1)

        if ask1=='4':
            print()
            print('你选择了 平方千米')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input(' 换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'平方千米等于',ask3*10000000000,'平方厘米')
                time.sleep(1)

            if ask4=='2':
                print()
                print(ask3,'平方千米等于',ask3*100000000,'平方分米')
                time.sleep(1)

            if ask4=='4':
                print()
                print(ask3,'平方千米等于',ask3*1000000,'平方米')
                time.sleep(1)

#重量
    if ask=='3':
        print()
        print('1.克')
        print('2.千克')
        print('3.吨')
        print()
        ask1=input('请选择第一个重量单位(序号)')
    
        if ask1=='1':
            print()
            print('你选择了 克')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='2':
                print()
                print(ask3,'克等于',ask3/1000,'千克')
                time.sleep(1)

            if ask4=='3':
                print()
                print(ask3,'克等于',ask3/1000000,'吨')
                time.sleep(1)

            

        if ask1=='2':
            print()
            print('你选择了 千克')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？(序号)：')
            if ask4=='1':
                print()
                print(ask3,'千克等于',ask3*1000,'克')
                time.sleep(1)

            if ask4=='3':
                print()
                print(ask3,'千克等于',ask3/1000,'吨')
                time.sleep(1)

            
        if ask1=='3':
            print()
            print('你选择了 吨')
            print()
            time.sleep(1)
            ask3=int(input('请输入这个单位的数值'))
            ask4=input('换成？：')
            if ask4=='1':
                print()
                print(ask3,'吨等于',ask3*1000000,'克')
                time.sleep(1)

            if ask4=='2':
                print()
                print(ask3,'吨等于',ask3*1000,'千克')
                time.sleep(1)

 #退出  
    if ask=='quit':
        print()
        print('正在退出')
        time.sleep(1)
        break


        
