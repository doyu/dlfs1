#!/usr/bin/env python
# coding: utf-8

# coding: utf-8
import numpy as np
import matplotlib.pylab as plt


def step_function(x):
    return np.array(x > 0, dtype=int)


X = np.arange(-5.0, 5.0, 0.1)
X[:9]


Y = step_function(X)
Y


plt.plot(X, Y)
plt.ylim(-0.1, 1.1)  # 図で描画するy軸の範囲を指定
plt.show()

