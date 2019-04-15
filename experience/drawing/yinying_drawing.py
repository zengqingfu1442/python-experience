import matplotlib.pyplot as plt
import numpy as np


def init():
    plt.xlabel('X')
    plt.ylabel('Y')

    fig = plt.gcf()
    fig.set_facecolor('lightyellow')
    fig.set_edgecolor("black")

    ax = plt.gca()
    ax.patch.set_facecolor("lightgray")  # 设置ax区域背景颜色
    ax.patch.set_alpha(0.1)  # 设置ax区域背景颜色透明度
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))


# 原下半函数
def f1(px, r, a, b):
    return b - np.sqrt(r ** 2 - (px - a) ** 2)


# 斜线函数
def f2(px, m, n):
    return px * n / m


# 斜线函数2
def f3(px, m, n):
    return n - 1 * px * n / m


if __name__ == '__main__':
    r = 4  # 圆半径
    m = 8  # 宽
    n = 4  # 高
    a, b = (4, 4)  # 圆心坐标
    init()

    x = np.linspace(0, m, 100 * m)
    y = np.linspace(0, n, 100 * n)

    # 半圆形
    y1 = f1(x, r, a, b)
    plt.plot(x, y1)
    # 矩形横线
    plt.plot((x.min(), x.max()), (y.min(), y.min()), 'g')
    plt.plot((x.min(), x.max()), (y.max(), y.max()), 'g')
    plt.plot((x.max(), x.max()), (y.max() + 2, y.max() + 2), 'g')  # 画点（8,6）避免图形变形
    # 矩形纵向
    plt.plot((x.min(), x.min()), (y.min(), y.max()), 'g')
    plt.plot((x.max(), x.max()), (y.min(), y.max()), 'g')
    # 斜线方法
    y2 = f2(x, m, n)
    plt.plot(x, y2, 'purple')

    # 阴影部分填充
    xf = x[np.where(x <= 0.5 * x.max())]
    plt.fill_between(xf, y.min(), f1(xf, r, a, b), where=f1(xf, r, a, b) <= f2(xf, m, n),
                     facecolor='y', interpolate=True)
    plt.fill_between(xf, y.min(), f2(xf, m, n), where=f1(xf, r, a, b) > f2(xf, m, n),
                     facecolor='y', interpolate=True)
    # 半圆填充
    plt.fill_between(x, y1, y.max(), facecolor='r', alpha=0.25)
    plt.show()

# Draw.py