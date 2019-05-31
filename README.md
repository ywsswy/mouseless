# 用键盘控制鼠标

当鼠标或者触控板坏了怎么办，手上没有鼠标怎么办？

本代码使用python的pynput库实现"键盘控制鼠标"

## 使用说明

|键盘组合键|等价于鼠标的操作|
|-|-|
|Ctrl + 'm'|鼠标向左移动|
|Ctrl + ','|鼠标向下移动|
|Ctrl + '.|鼠标向上移动|
|Ctrl + '/'|鼠标向右移动|
|Ctrl + ':'|按下鼠标左键|
|Ctrl + '\''|按下鼠标右键|
|Scroll Lock|终止程序|

## tips

为什么会选择以上按键来控制鼠标呢？熟悉使用Vim的人知道，文本编辑器中，控制光标移动的按键就是'h','j','k','l'，而如果选用Ctrl + 'h','j','k','l'会与chrome浏览器中的快捷键冲突，所以最终决定选择'h','j','k','l'右下方的四个按键。键位图如下，熟悉Vim的人很容易就能上手。

![image](https://user-images.githubusercontent.com/25153243/58677090-40111700-838d-11e9-8e65-becbd93bc85b.png)
