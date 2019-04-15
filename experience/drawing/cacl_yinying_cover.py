import numpy as np


def f1(px, r, a, b):
    return b - np.sqrt(r ** 2 - (px - a) ** 2)


def f2(px, m, n):
    return px * n / m


if __name__ == '__main__':
    r = 4  # 圆半径
    m = 8  # 宽
    n = 4  # 高
    a, b = (4, 4)  # 圆心坐标
    t = 100  # 精度

    xs = np.linspace(0, m, 2 * t * m)
    ys = np.linspace(0, n, t * n)

    # 半圆形
    y1 = f1(xs, r, a, b)
    # 斜线
    y2 = f2(xs, m, n)

    numin = 0
    numtotel = 0
    side = True  # 是否计算边框
    for x in xs:
        for y in ys:
            if not side:
                if (x <= 0) | (x >= 8) | (y <= 0) | (y >= 4):
                    continue
            numtotel += 1
            if x >= 4:
                continue
            y1 = f1(x, r, a, b)
            y2 = f2(x, m, n)
            if y1 - y2 >= 0:
                if y2 - y > 0:
                    numin += 1
                if (y2 - y == 0) and side:
                    numin += 1
            elif y2 - y1 > 0:
                if y1 - y > 0:
                    numin += 1
                if (y2 - y == 0) and side:
                    numin += 1

    print(32 * numin / numtotel)