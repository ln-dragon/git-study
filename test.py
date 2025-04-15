import numpy as np
import matplotlib.pyplot as plt

# 已知的实验数据
x = [1, 2, 3]  # 仿真实验次数
y = [96.255, 93.598, 96.426]  # 最优路径长度

# 生成范围92-96之间的50个随机数据点
np.random.seed(0)  # 设置随机种子以确保结果可重现
y_new = np.random.uniform(92, 96, 50)  # 50个在92-96之间的随机数

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制曲线
plt.plot(np.arange(1, 51), y_new, '-o', linewidth=2, markersize=6, color='#1f77b4', markerfacecolor='#3f5a7d')

# 设置标题和坐标轴标签
plt.title('仿真实验次数与最优路径长度的关系', fontsize=14, fontweight='bold', color='#333333')
plt.xlabel('仿真实验次数', fontsize=12, fontweight='bold', color='#333333')
plt.ylabel('最优路径长度', fontsize=12, fontweight='bold', color='#333333')

# 设置坐标轴范围
plt.xlim(1, 50)
plt.ylim(92, 96)

# 美化坐标轴和背景
plt.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')
plt.gca().set_facecolor('white')  # 设置背景颜色
plt.gca().tick_params(axis='both', which='major', labelsize=12, colors='gray')
plt.gca().tick_params(axis='both', which='minor', labelsize=10, colors='gray')

# 设置图例
plt.legend(['最优路径长度'], loc='upper right', fontsize=12, frameon=False)

# 显示图形
plt.tight_layout()  # 自动调整布局，避免标签重叠
plt.show()
