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
|Ctrl + ':'|按下鼠标右键|
|Ctrl + '\''|按下鼠标左键|
|Scroll Lock|终止程序|

## tips

* 为什么会选择以上按键来控制鼠标呢？熟悉使用Vim的人知道，文本编辑器中，控制光标移动的按键就是'h','j','k','l'，而如果选用Ctrl + 'h','j','k','l'会与chrome浏览器中的快捷键冲突，所以最终决定选择'h','j','k','l'右下方的四个按键。键位图如下，熟悉Vim的人很容易就能上手。

![image](https://user-images.githubusercontent.com/25153243/58677090-40111700-838d-11e9-8e65-becbd93bc85b.png)

* 为什么会左键在右侧，右键在左侧呢？因为电脑上按下Ctrl + ':'后无法继续按下'.'，这就导致无法在按下左键之后向上移动鼠标，所以把':'换成了右边的'\''。

* 如下软件可能有冲突的快捷键，使用时记得把其他软件的快捷键进行修改。
|快捷键|冲突|
|-|-|
|Ctrl +'m'|爱奇艺万能播放器的静音键|

* Ctrl快捷键是操作windows文件的快捷键，所以为避免冲突轻易不要在windows文件夹中使用Ctrl快捷键，而是使用方向键加回车来代替。

* 为什么不使用Alt而是使用Ctrl，因为Alt会触发菜单选项。

* 为什么不使用Shift而是使用Ctrl，因为Shift加字符会直接输出内容到光标处。

* 如果键盘上没有Scroll Lock键怎么办。。。这个Alt+Space杀死程序吧。

* Windows10测试成功的环境是在Anaconda Prompt中安装pynput库成功（如果用WSL则不成功）。
