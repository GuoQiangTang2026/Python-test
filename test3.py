# 实验三 Python GUI 界面设计（多图形选项版）
import sys
import numpy as np
import matplotlib.pyplot as plt
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QPushButton, QTextEdit, QFrame)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# 图形画布类（用于显示图表）
class MatplotlibCanvas(FigureCanvas):
    def __init__(self, parent=None):
        self.fig = plt.figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        super().__init__(self.fig)

# 主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI界面设计实验 - 多图形选项")
        self.resize(850, 650)
        self.init_ui()

    def init_ui(self):
        # 主容器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # ========== 1. 按钮区域（多图形按钮） ==========
        btn_layout = QHBoxLayout()
        
        self.btn_info = QPushButton("显示信息")
        self.btn_sin = QPushButton("绘制正弦曲线")
        self.btn_cos = QPushButton("绘制余弦曲线")
        self.btn_parabola = QPushButton("绘制抛物线")
        self.btn_bar = QPushButton("绘制柱状图")
        self.btn_clear = QPushButton("清空内容")

        # 绑定事件
        self.btn_info.clicked.connect(self.show_text)
        self.btn_sin.clicked.connect(self.draw_sin)
        self.btn_cos.clicked.connect(self.draw_cos)
        self.btn_parabola.clicked.connect(self.draw_parabola)
        self.btn_bar.clicked.connect(self.draw_bar)
        self.btn_clear.clicked.connect(self.clear_all)

        # 添加到布局
        btn_layout.addWidget(self.btn_info)
        btn_layout.addWidget(self.btn_sin)
        btn_layout.addWidget(self.btn_cos)
        btn_layout.addWidget(self.btn_parabola)
        btn_layout.addWidget(self.btn_bar)
        btn_layout.addWidget(self.btn_clear)
        main_layout.addLayout(btn_layout)

        # ========== 2. 信息显示框 ==========
        self.text_box = QTextEdit()
        self.text_box.setPlaceholderText("信息显示区域")
        main_layout.addWidget(self.text_box)

        # ========== 3. 图形显示框 ==========
        self.graph_frame = QFrame()
        self.graph_frame.setFrameShape(QFrame.Box)
        self.graph_layout = QVBoxLayout(self.graph_frame)
        self.canvas = MatplotlibCanvas()
        self.graph_layout.addWidget(self.canvas)
        main_layout.addWidget(self.graph_frame)

    # 显示信息
    def show_text(self):
        info = """✅ GUI界面运行成功！
📌 包含组件：按钮 + 信息显示框 + 图形显示框
📌 图形选项：正弦曲线、余弦曲线、抛物线、柱状图
📌 实验内容：Python GUI界面设计"""
        self.text_box.setText(info)

    # 1. 绘制正弦曲线
    def draw_sin(self):
        self.canvas.ax.clear()
        x = np.linspace(0, 2*np.pi, 100)
        y = np.sin(x)
        self.canvas.ax.plot(x, y, 'b-', linewidth=2, label="sin(x)")
        self.canvas.ax.set_title("正弦曲线")
        self.canvas.ax.legend()
        self.canvas.ax.grid(True)
        self.canvas.draw()
        self.text_box.setText("已绘制：正弦曲线")

    # 2. 绘制余弦曲线
    def draw_cos(self):
        self.canvas.ax.clear()
        x = np.linspace(0, 2*np.pi, 100)
        y = np.cos(x)
        self.canvas.ax.plot(x, y, 'r-', linewidth=2, label="cos(x)")
        self.canvas.ax.set_title("余弦曲线")
        self.canvas.ax.legend()
        self.canvas.ax.grid(True)
        self.canvas.draw()
        self.text_box.setText("已绘制：余弦曲线")

    # 3. 绘制抛物线
    def draw_parabola(self):
        self.canvas.ax.clear()
        x = np.linspace(-5, 5, 100)
        y = x ** 2
        self.canvas.ax.plot(x, y, 'g-', linewidth=2, label="y = x²")
        self.canvas.ax.set_title("抛物线")
        self.canvas.ax.legend()
        self.canvas.ax.grid(True)
        self.canvas.draw()
        self.text_box.setText("已绘制：抛物线 y = x²")

    # 4. 绘制随机柱状图
    def draw_bar(self):
        self.canvas.ax.clear()
        x = ['A', 'B', 'C', 'D', 'E']
        y = np.random.randint(1, 10, 5)
        self.canvas.ax.bar(x, y, color='orange')
        self.canvas.ax.set_title("随机柱状图")
        self.canvas.ax.grid(True, axis='y')
        self.canvas.draw()
        self.text_box.setText("已绘制：随机柱状图")

    # 清空内容
    def clear_all(self):
        self.text_box.clear()
        self.canvas.ax.clear()
        self.canvas.draw()
        self.text_box.setText("已清空所有内容！")

# 运行程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())