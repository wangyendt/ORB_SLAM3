"""
@author: wangye(Wayne)
@license: Apache Licence
@file: compare_imu_and_slam_quat.py
@time: 20230209
@contact: wang121ye@hotmail.com
@site:  wangyendt@github.com
@software: PyCharm

# code is far away from bugs.
"""

import pandas as pd
import matplotlib

matplotlib.use('MacOSX')
import matplotlib.pyplot as plt
from ahrs.filters import EKF, Mahony, Madgwick
from ahrs import QuaternionArray
from ahrs.common import Quaternion
import numpy as np

path = r'/Users/wayne/Documents/work/data/slam/mate20/dataset/indoor_walking_loop_staticinit_2/mav0/imu0/data.csv'
data = pd.read_csv(path).values
ts = data[:, 0]
# ts -= ts[0]
ts /= 1e9
gyro = data[:, 1:4]
acc = data[:, 4:]
ahrs = Madgwick(gyro, acc, frequency=500)

img_path = r'/Users/wayne/Documents/work/data/slam/mate20/dataset/indoor_walking_loop_staticinit_2/mav0/imu0/f_dataset-mate20_monoi.txt'
img_data = pd.read_csv(img_path, delimiter=' ', header=None).values
img_ts = img_data[:, 0]
# img_ts -= img_ts[0]
img_ts /= 1e9
img_pos = img_data[:, 1:4]
img_quat = img_data[:, 4:]
for i in range(img_quat.shape[0]):
    if i and np.sum(np.abs(img_quat[i] - img_quat[i - 1])) > np.sum(np.abs(img_quat[i] + img_quat[i - 1])):
        img_quat[i] = -img_quat[i]
q1 = ahrs.Q
q1_inv = Quaternion(q1[-1]).conj
q1 = [Quaternion(Quaternion(q) * Quaternion(q1_inv)) for q in q1]
img_q1 = img_quat
img_q1_inv = Quaternion(img_q1[-1]).conj
img_q1 = [Quaternion(q) * Quaternion(img_q1_inv) for q in img_q1]
fig, ax = plt.subplots(3, 2, sharex='all', sharey='all')
ax = ax.flatten()
ax[0].plot(ts, q1)
ax[1].plot(ts, QuaternionArray(q1).to_angles())
ax[2].plot(img_ts, img_q1)
ax[3].plot(img_ts, QuaternionArray(img_q1).to_angles())
ax[4].plot(ts, q1, 'r')
ax[4].plot(img_ts, img_q1, 'b')
ax[5].plot(ts, QuaternionArray(q1).to_angles(), 'r')
ax[5].plot(img_ts, QuaternionArray(img_q1).to_angles(), 'b')
plt.show()
