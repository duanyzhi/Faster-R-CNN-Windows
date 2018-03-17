from lib.config import config as cfg
import numpy as np
weight = np.loadtxt(cfg.FLAGS.dis_weight)


def reg(bbox, heights, weights):
    (x_left, y_top, x_right, y_bottom) = bbox  # # x_left, y_top, x_right, y_bottom   height:def 375, weight 500
    print(heights, weights, x_left, y_top, x_right, y_bottom)
    x_left = x_left * 500 / weights
    x_right = x_right * 500 / weights
    y_top = y_top * 375 / heights
    y_bottom = y_bottom * 375 / heights
    print(heights, weights, x_left, y_top, x_right, y_bottom)
    x_c = (250 - (x_left + x_right)/2)*0.03019/1000
    y_c = (375 - y_bottom)/1000
    img_dis = np.array([y_c, y_c**2, y_c**3, y_c**4, np.sqrt(y_c)])
    dis_y = sum(weight[:5]*img_dis) + weight[-1]
    dis = np.sqrt(x_c**2 + dis_y**2)
    dis = dis * 50 / 10
    dis = dis * 1.5 * (dis - 1)*0.8
    return dis
