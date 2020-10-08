# 用键盘控制鼠标

当鼠标或者触控板坏了怎么办，手上没有鼠标怎么办？

本代码使用python的pynput库实现"键盘控制鼠标"

## 使用说明

|键盘组合键|等价于鼠标的操作|
|-|-|
|Ctrl + ←|鼠标向左移动|
|Ctrl + ↓|鼠标向下移动|
|Ctrl + ↑|鼠标向上移动|
|Ctrl + →|鼠标向右移动|
|Ctrl + pageup|按下鼠标左键|
|Ctrl + pagedown|按下鼠标右键|
|Ctrl + <|终止程序|

* Windows10测试成功的环境是在官网下载的Python3中安装pynput库（如果用WSL或者Anaconda Prompt则不成功）
