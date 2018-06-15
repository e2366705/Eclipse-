# Eclipse--Set
Eclipse的那些设置



1-#查看版本号
import sys
print(sys.version)

-------------------------------------------------------------------------------------------------------分割线-----
2-导出Eclipse的各种自定义配置(省去以后自己各种设置的烦恼) : 
将workspace/.metadata/.plugins/org.eclipse.core.runtime中的.settings文件夹拷贝出来，
里面就是所有的配置文件，新建工作空间的时候将该.settings文件夹替换掉新工作空间中的.settings文件夹即可.
（有网友是将.plugings文件夹替换,但是.plugings文件夹太大了，实际上就是替换.settings文件夹，.settings只有几百k。）
 
 比如  :  
 现在我的Eclipse的设置配置保存在 : 
C:\DiSanFangSoftWoreYXBYXBYXBYxb\AboutPythonPPPPPP\Eclipse IDE for Java EE Developers__2\eclipse__Py_2__workspace\.metadata\.plugins\org.eclipse.core.runtime

-------------------------------------------------------------------------------------------------------分割线-----

3-
Eclipse设置Debug断点的快捷键 (Eclipse系统默认的) : 
设置断点：在该行最前面边框双击  或快捷键：Ctrl+Shift+B

-------------------------------------------------------------------------------------------------------分割线-----

4-改PyDev注释颜色
PyDev插件安装上后，默认注释的颜色是灰色，看注释非常费力，于是又找到改注释颜色办法。
windows->peferences->PyDev->Editor
Appearance color options:
选择Comments，在color里选择颜色，然后apply

-------------------------------------------------------------------------------------------------------分割线-----

5-Eclipse设置当前光标所在行的颜色 : 
current line highlight (当前行突出显示)
方法 : Window——Preference，选择General——Editors——Text Editors




