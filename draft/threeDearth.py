import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm


def create_simple_earth():
    # 创建球面坐标
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    # 创建图形
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制地球表面（使用蓝色渐变模拟海洋）
    surf = ax.plot_surface(x, y, z, cmap=cm.Blues, alpha=0.8,
                           linewidth=0, antialiased=True)

    # 添加经纬线
    # 经线
    for i in range(0, 360, 30):
        theta = np.radians(i)
        x_line = np.outer(np.cos(theta), np.sin(v))
        y_line = np.outer(np.sin(theta), np.sin(v))
        z_line = np.outer(np.ones(len(v)), np.cos(v))
        # 展平数组进行绘制
        ax.plot(x_line.flatten(), y_line.flatten(), z_line.flatten(),
                'k-', alpha=0.3, linewidth=0.5)

    # 纬线
    for i in range(-60, 90, 30):
        phi = np.radians(i)
        r = abs(np.cos(phi))
        if r > 0.01:  # 避免极点问题
            z_const = np.sin(phi) * np.ones(len(u))
            x_circle = r * np.cos(u)
            y_circle = r * np.sin(u)
            ax.plot(x_circle, y_circle, z_const, 'k-', alpha=0.3, linewidth=0.5)

    # 设置标题和标签
    ax.set_title('3D Earth Model', fontsize=16, pad=20)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    # 设置坐标轴比例
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])

    # 添加颜色条
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()


def create_realistic_earth():
    # 创建球面坐标 - 确保维度正确
    theta = np.linspace(0, 2 * np.pi, 200)  # 经度 (0 to 2π)
    phi = np.linspace(0, np.pi, 100)  # 纬度 (0 to π)

    # 创建球面坐标
    x = np.outer(np.cos(theta), np.sin(phi)).T
    y = np.outer(np.sin(theta), np.sin(phi)).T
    z = np.outer(np.ones(len(theta)), np.cos(phi)).T

    # 创建纹理 - 关键：确保维度与坐标匹配
    # 重新创建正确的网格
    Theta, Phi = np.meshgrid(theta, phi)

    # 创建地球表面的地形纹理
    texture = (np.sin(3 * Theta) * np.cos(2 * Phi) +
               0.5 * np.sin(5 * Theta + Phi) +
               0.3 * np.sin(7 * Theta) * np.cos(3 * Phi))
    texture = (texture - texture.min()) / (texture.max() - texture.min())

    # 创建图形
    fig = plt.figure(figsize=(14, 12))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制地球表面 - 使用标准颜色而不是facecolors
    surf = ax.plot_surface(x, y, z, cmap=cm.terrain,
                           alpha=0.9, linewidth=0, antialiased=True,
                           vmin=0, vmax=1)

    # 添加经纬线
    # 主要经线（每45度一条）
    phi_line = np.linspace(0, np.pi, 100)
    for i in range(0, 360, 45):
        theta_line = np.radians(i)
        x_line = np.sin(phi_line) * np.cos(theta_line)
        y_line = np.sin(phi_line) * np.sin(theta_line)
        z_line = np.cos(phi_line)
        ax.plot(x_line, y_line, z_line, 'white', alpha=0.6, linewidth=1)

    # 主要纬线（每30度一条）
    theta_circle = np.linspace(0, 2 * np.pi, 100)
    for lat in [-60, -30, 0, 30, 60]:
        phi_circle = np.radians(90 - lat)  # 转换为球坐标
        r = np.sin(phi_circle)
        z_const = np.cos(phi_circle) * np.ones(len(theta_circle))
        x_circle = r * np.cos(theta_circle)
        y_circle = r * np.sin(theta_circle)
        ax.plot(x_circle, y_circle, z_const, 'white', alpha=0.6, linewidth=1)

    # 添加地轴
    ax.plot([0, 0], [0, 0], [-1.5, 1.5], 'r-', linewidth=2, alpha=0.7)

    # 添加北极和南极标记
    ax.scatter([0], [0], [1.1], color='white', s=50, alpha=0.8)
    ax.scatter([0], [0], [-1.1], color='white', s=50, alpha=0.8)

    # 设置视角和标题
    ax.view_init(elev=25, azim=45)
    ax.set_title('Realistic 3D Earth Model', fontsize=18, pad=30)

    # 隐藏坐标轴
    ax.set_axis_off()

    # 设置坐标范围
    ax.set_xlim([-1.3, 1.3])
    ax.set_ylim([-1.3, 1.3])
    ax.set_zlim([-1.3, 1.3])

    plt.tight_layout()
    plt.show()


def create_basic_colored_earth():
    """一个更简单的彩色地球版本"""
    # 创建球面坐标
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 50)
    x = np.outer(np.cos(u), np.sin(v))
    y = np.outer(np.sin(u), np.sin(v))
    z = np.outer(np.ones(np.size(u)), np.cos(v))

    # 创建颜色数据（基于z坐标，模拟地球的明暗变化）
    colors = z

    # 创建图形
    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    # 绘制地球表面
    surf = ax.plot_surface(x, y, z, facecolors=cm.terrain(colors),
                           alpha=0.8, linewidth=0, antialiased=True)

    # 设置标题
    ax.set_title('3D Earth Model - Basic Version', fontsize=16, pad=20)

    # 隐藏坐标轴
    ax.set_axis_off()

    # 设置视角
    ax.view_init(elev=25, azim=45)

    plt.tight_layout()
    plt.show()


# 运行不同的版本
if __name__ == "__main__":
    print("选择要运行的地球模型:")
    print("1. 简单版本")
    print("2. 高级版本")
    print("3. 基础彩色版本")

    choice = input("请输入选择 (1/2/3): ")

    if choice == "1":
        pass
    elif choice == "2":
        create_realistic_earth()
    elif choice == "3":
        create_basic_colored_earth()
    else:
        print("运行默认简单版本...")
        #create_simple_earth()