### Automated test framework by Fengling

<br>

### 最想说的话：

# 想做的太多，能做的却少之又少，还得沉淀

<br>

### 技术栈：

<b><kbd>selenium</kbd> + <kbd>unittest</kbd> + <kbd>poium</kbd> + <kbd>XTestRunner</kbd></b>

### change tips:

- [ ] <kbd>unittest</kbd> ➡ <kbd>pytest</kbd>
- [ ] <kbd>poium</kbd> ➡ <kbd>nopo</kbd>

<br>

### 功能点及细节完善的地方：

| 已实现 | 待完善 |
| :----: | :----: |
| 测试用例的自动化 | 输入数据input_str()的封装还可以更完美，比如说：根据传入的数据列表中元素的个数，实现数据的动态输入，一劳永逸！ |
| 错误截图及错误定位 | ~~等待时间的优化，用显式等待封装可以最大限度地节省等待时间~~ |
| 测试数据的读取 | ~~使用poium对页面基类进行一个大改造（这个解决的话，第二点也会自动解决）（已完成）~~ |
| 测试日志文件的生成 | ~~断言的封装（已完成）~~ |
| 测试报告的生成 | 使用饭佬的wqrfnium对元素的定位实现自动更新，解决因前端代码更改导致的元素定位失败问题，一劳永逸！ |
| 测试报告的邮箱发送 | 制作元素类的自动生成器，通过读取excel自动创建 类名 以及 英文元素名变量 到Elements_and_Data.py里 |
| 验证码的自动识别(该功能未稳定) |  |

<br>

### 文件说明：

##### Config：ini配置文件 以及 全局路径配置<kbd>globalconfig.py</kbd>

##### Data：excel类型的<kbd>测试数据集</kbd>以及页面的元素定位<kbd>elements_xpath_loc.xlsx</kbd>

##### Public：

> ###### common：各种公共方法的封装
> ###### pages：<kbd>basepage</kbd>为<kbd>页面基类</kbd>，继承于虫师的poium的<kbd>Page</kbd>，并在此之上添加了其他的方法，其中<kbd>get_element_text()</kbd>能够更好地与断言配合工作，其他类是在此页面基类的基础上进行继承、重写

##### Report：

> ###### ErrorScreenShot：错误截图
> ###### Log：日志，用的是<kbd>loguru</kbd>模块
> ###### TestHtmlReport：HTML格式的<kbd>测试报告</kbd>，用的是<kbd>XTestRunner</kbd>模块

##### TestCase：测试用例包，在此之下有各模块的<kbd>测试用例</kbd>

##### run.py：测试框架的<kbd>执行程序</kbd>

