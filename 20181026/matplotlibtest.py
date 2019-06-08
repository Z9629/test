'''matplotlib笔记'''
'''基本线图绘制'''

import numpy as np


def main():
    #line
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi,np.pi,256,endpoint=True)
    #定义余弦函数和正弦函数
    c,s = np.cos(x),np.sin(x)
    plt.figure(1)
    plt.plot(x,c,color="blue",linewidth=1.0,linstyle="-",label="COS",alpha=0.5)
    plt.plot(x,s)
    plt.title("COS&SIN")    #标题
    plt.show()



if __name__ == '__main__':
    main()