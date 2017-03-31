# Python 总结

- [装饰器](#a1)

- [enumerate 用法](#a2)

- [正则表达式](#a3)

- [函数式编程](#a4)

- [可变参数](#a5)

- [字符编码](#a6)

- [深拷贝和浅拷贝](#a7)

- [Python 程序的运行原理](#a8)

- [input()、raw_input() 和 sys.stdin](#a9)

- [Python 字典对象实现](#a10)

- [Socket 通信原理](#a11)

- [yield](#a12)

- [多线程](#a13)

<h2 id='a1'>装饰器</h2>

[Python 装饰器][1]

可以在不改动函数的情况下，添加功能；装饰器实际上是返回一个更高阶的函数
```python
# 日志打印装饰器
def log(func):  # 函数作为参数传入
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
```
装饰器支持语法糖 (@) 功能
```python
@log
def now():
    print '2013-12-25'
# 相当于调用 log(now)
```
**装饰器接受参数**
log 同样可以接受参数，因为它本质上是一个函数
```python
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

# 调用如下
@log('execute')
def now():
    print '2013-12-25'

#等价于 log('execute')(now)
```

<h2 id='a2'>enumerate 用法</h2>

[python enumerate用法][2]

遍历容器，返回索引以及各个元素
```python
>>> seq = ['a','b','c','d']  
>>> for i,key in enumerate(seq):  
...     print 'seq[%d]=%s' % (i, key)  
...   
seq[0]=a  
seq[1]=b  
seq[2]=c  
seq[3]=d  

>>> seq = ['a','b','c','d']  
>>> for i,key in enumerate(seq[::-1]):  
...     print 'seq[%d]=%s' % (i, key)  
...   
seq[0]=d  
seq[1]=c  
seq[2]=b  
seq[3]=a  
```

<h2 id='a3'>正则表达式</h2>

[Python正则表达式指南][3]


![enter description here][4]


<h2 id='a4'>函数式编程</h2>

[Python函数式编程指南（一）：概述][5]

[Python函数式编程指南（二）：函数][6]

**什么是函数式编程**
* 函数作为参数，返回值传递
* 匿名函数(lambda)
```python
lambda arg: expression
```
* 使用闭包

优点：模块化，函数式编程推崇简单原则，一个函数只做一件事情，将功能大的事情尽可能拆成小的模块;易于测试、调试;函数式编程产生更少的代码，更容易阅读和维护

**闭包**
[Python深入04 闭包][7]

闭包是一类特殊的函数，如果一个函数定义在另一个函数的作用域中，并且函数中引用了外部函数的局部变量，那么这个函数就是一个闭包。

* 闭包能够提高代码复用性
```python
def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)
print line1(5), line2(5)
```

**常用函数**
[python函数式编程][8]

* lambda，创建一个匿名函数，冒号左侧表示接收的参数，右侧表示返回值
* map，对参数的元素调用相同的函数
```python
map(len,'hao','fnng','cn') # 对参数中的每一个元素作为 len 函数的参数，返回值放在同一个列表中
```
* reduce，每次需要两个数据进行处理，最后的结果作为返回值
```python
add = reduce(lambda x,y:x+y,[2,3,4])
print add
# 输出结果为 9
```
* filter,获取参数中满足条件的元素，放在一个列表中作为返回值
```python
number =[2, -5, 9, -7, 2, 5, 4, -1, 0, -3, 8]
# 筛选大于 0 的元素
sum = filter(lambda x: x>0, number)
```

<h2 id='a5'>可变参数</h2>

[理解 Python 中的 *args 和 **kwargs][9]

[可变参数][10]


**用在函数参数**

`*args` 位置参数:把参数收集到一个元组，作为变量 `args`

`**kwargs` 关键字参数:包含参数名和值的字典类型，需要 `key/value` 对作为参数

**用在函数调用**
```python?linenums
>>> def test(a,b,c):
	print  a,b,c
>>> x = {'a':1,'b':2,'c':3}
>>> test(**x)
1 2 3
>>> test(*x) 
a c b
```

<h2 id='a6'>字符编码</h2>

[十分钟搞清字符集和字符编码][11]

[字符编码笔记：ASCII，Unicode和UTF-8][12]


 1. `Unicode` 对100多万个字符进行了编码，只规定了符号的二进制代码，没有规定二进制代码如何存储
 2. `UTF-8` 是对 `Unicode` 的实现方式，一种变长的编码方式


`UTF-8`、`GBK` 都是对 `Unicode` 的字符二进制进行了不同的编码


<h2 id='a7'>深拷贝和浅拷贝</h2>

[深入Python(4):深拷贝和浅拷贝][13]

在没有调用 copy 模块的 deepcopy()时，都是浅拷贝，只是增加源对象的引用计数
以下会增加引用计数
```python
y = x   #做别名
foo(x)  #做参数传递
mylis = [1,2,x,'a'] #成为容器对象的一个元素
```
以下会减少引用计数
```python
del x   #del显式销毁

bar = x 
x = True    #对象的一个别名被赋值给其他对象

mylis.remove(x) #对象被从窗口对象中移除

del mylis   #窗口对象本身被销毁
```

<h2 id='a8'>Python 程序的运行原理</h2>
[谈谈 Python 程序的运行原理][14]



<h2 id='a9'>input()、raw_input() 和 sys.stdin</h2>
[raw_input() 与 input() Python][15]

[Python 的 sys.stdout、sys.stdin 重定向][16]

raw_input() 读入的都是字符串，是对 sys.stdin.readline() 的调用
sys.stdin.readline() 读入的为字符串，且包含换行符
input() 能输入特定格式(比如:整数、字符串)，是对 raw_input() 的调用

<h2 id='a10'>Python 字典对象实现</h2>
[《Python源码剖析》阅读笔记：第五章-dict对象][17]


字典和 C++ STL 中 map 一样，是映射容器，但是原理不一样，效率要求更高，所以采用了哈希表来实现。

为了解决哈希值冲突问题，采用了**开放寻址法**。开放寻址法能更好的利用 CPU Cache，命中率较高。


<h2 id='a11'>Socket 通信原理</h2>
[Socket通信原理简介][18]

[ Socket通信原理和实践][19]

[SOCKET类型定义及应用][20]

Socket 用于网络中的不同计算机通信，应用层和传输层之间的一个抽象

![enter description here][21]

**实现过程**

![enter description here][22]

**socket 函数**

创建 socket 描述字，确定 socket 的协议类型（TCP 或 UDP)

**bind 函数**

[bind 函数说明][23]

bind 函数用于服务器端 socket 描述字和源地址、端口绑定，在多网卡的情况下也能正确的监听网卡和端口

**listen/connect 函数**

listen 监听 socket 描述字和客户端建立连接，同时确定申请连接队列长度，服务端不能及时处理的客户端，会放在一个队列中，队列满了，再申请的客户会收到 WSAECONNREFUSED 错误。

[connect 函数][24]
connect 用于连接服务器端，需要知道客户端的 socket 描述字，和服务器 socket(包括服务器的端口和 IP)


**accept 函数**
通过监听 socket 描述字产生已连接 socket 描述字，已连接 socket 用于通信

<h2 id='a12'>yield</h2>
[Python yield 使用浅析][25]

带有 yield 的函数是一个 generator，每次执行到一个 yield 语句就会中断，并返回一个迭代值，下次执行从 yield 的下一个语句继续执行

```python
def fab(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

 >>> for n in fab(5): 
 ...     print n 
 ... 
 1 
 1 
 2 
 3 
 5
 >>> f = fab(5) 
 >>> f.next() 
 1 
 >>> f.next() 
 1 
 >>> f.next() 
 2 
 >>> f.next() 
 3 
 >>> f.next() 
 5 
```

<h2 id='a13'>多线程</h2>
[python 多线程就这么简单][26]

[python 中 threading 的 setDaemon、join 的用法][27]


##  cookie 和 session 的区别

[cookie 和session 的区别详解][28]

* cokkie 存放在客户端，session 存放在服务器上
* cookie 不安全，容易被获取


```python?linenums
import threading   #  导入 threading 模块
t = threading.Thread(target,args)  # 创建一个线程对象，target 为需要运行的函数，args 为函数的参数
t.setDaemon(True)  # 在 start() 调用之前设置，
t.start()  #  运行
```

threada.join（) 表示正在运行的线程需要在线程 threada 结束后才继续运行

setDaemon（) 表示主线程结束时，字线程也会被杀死

##  socketserver 源码
[socketserver源码分析][29]

server 类有 5 种类型，还有支持事务处理的 BaseRequestHandler 类及子类，扩展成为多线程或多进程需要继承 ForkingMixIn 或 ThreadingMixIn

**Server 类**

![enter description here][30]

这些 Server 都是对 socket 的封装，并确定参数实现相关协议，在 TCP 和 UDP 中，确定 address_family、socket_type 来调用不同的协议

```python?linenums
address_family = socket.AF_INET
socket_type = socket.SOCK_STREAM
self.socket = socket.socket(self.address_family,self.socket_type)
```

实现 TCPServer 时候，只要设置好 adress、port 和请求出来函数

```python?linenums
address=('127.0.0.1',9098)
server=socketserver.TCPServer(address,myTCPHandle)      #创建一个基于TCPServer的套接字
server.serve_forever() 
```

**事务处理 RequestHandler**

服务器段每次接收到一个连接都会新创建一个 RequestHandler

```python?linenums
def __init__(self, request, client_address, server):
    self.request = request
    self.client_address = client_address
    self.server = server
    self.setup()
    try:
         self.handle()
    finally:
         self.finish()

request, client_address = self.get_request()

# 在 TCPServer 中
def get_request(self):
    return return self.socket.accept()

```
事务处理接受 reques、client 和 server 为参数，并调用 handle（） 


##  WSGI、flup、fastcgi、webpy
[WSGI、flup、fastcgi、web.py的关系][31]

Apache/lighttpd: 相当于一个request proxy，根据配置，把不同的请求转发给不同的server处理，例如静态的文件请求自己处理，这个时候它就像一个web server，对于fastcgi/python这样的请求转发给flup这样的Server/Gateway进行处理

 flup: 一个用python写的web server，也就是cgi中所谓的Server/Gateway，它负责接受apache/lighttpd转发的请求，并调用你写的程序 (application)，并将application处理的结果返回到apache/lighttpd

fastcgi: apache/lighttpd的一个模块，虽然flup可以作为一个独立的web server使用，但是对于浏览器请求处理一般都交给 apache/lighttpd处理，然后由apache/lighttpd转发给flup处理，这样就需要一个东西来把apache/lighttpd跟flup联系起来，这个东西就是fastcgi，它通过环境变量以及socket将客户端请求的信息传送给flup并接收flup返回的结果

web.py: 应该说有了上面的东西你就可以开始编写你的web程序了，但是问题是你就要自己处理浏览器的输入输出，还有cookie、session、模板等各种各样的问题了，web.py的作用就是帮你把这些工作都做好了，它就是所谓的web framework，另外一个出名的是django，不过感觉太复杂了，web.py差不多就够用了

WSGI : 除了flup Server/Gateway外还有很多其他人的写的Server/Gateway, 这个时候就会出问题了，如果你在flup上写了一个程序，现在由于各种原因你要使用xdly了，这个时候你的程序也许就要做很多痛苦的修改才能使用 xdly server了，WSGI就是一个规范，他规范了flup这个服务应该怎么写，应该使用什么方式什么参数调用你写的程序(application)等，当然同时也规范你的程序应该怎么写了，这样的话，只要flup跟xdly都遵守WSGI的话，你的程序在两个上面都可以使用了，flup就是一个WSGI server

WSGI 是python的接口规范，这个规范是针对WEB服务器和python应用（框架等）的交互的。FASTCGI则是两者底层的通信协议的规范。

##  Web.py

[【Python】Webpy 源码学习（一）][32]

**WSGI 流程**
[WSGI初探][33]

[WSGI 简介][34]

[理解Python WSGI][35]

[WSGI 简介][36]

![webpy 流程图][37]

WSGI 是一个规范，描述了 web server 如何与 web application 交互、web application 如何处理请求

**server 如何调用 application**
WSGI 规定了 server 端交互的一个对象，所有请求 server 都会把这个 application 作为唯一的入口，传递请求；最后的请求又用户编写的处理程序完成。

传递的过程中，需要服务器的当前上下文，和专有的 start_response 对象

***start_response 参数***
* status:一个字符串，表示 HTTP 响应状态字符串
* response_headers:一个列表，包含如下形式的元组：(head_name,head_value)，用来表示 HTTP 响应的 headers


**Queue 同步队列**

[8.10. Queue — 同步队列类][38]

[Python Queue模块详解][39]

[Python爬虫(五)--多线程续(Queue)][40]


**application 初始化**
```python
app = web.application(urls, globals())

# application.py  50
def __init__(self, mapping=(), fvars={}, autoreload=None):
        if autoreload is None:
            autoreload = web.config.get('debug', False)
        self.init_mapping(mapping)
        self.fvars = fvars
        self.processors = [] 
        
        self.add_processor(loadhook(self._load))
        self.add_processor(unloadhook(self._unload))
```
**app 运行**
```python
# hello.py 25
if __name__ == "__main__":
    app.run()
```
实际调用 wsgi 模块的 runwsgi(func)
```python
# application.py  310
wsgi.runwsgi(self.wsgifunc(*middleware))
```
self.wsgifunc(*middleware) 作为一个 func 被传递，在响应时才进行调用

**wsgi 调用 httpserver**
```python
# wsgi.py  25
httpserver.runsimple(func, server_addr)
```
**httpserver**
runsimple 函数首先对 func 进行了封装，再作为 server 的方法用来响应
```python
# httpserver.py  145
func = StaticMiddleware(func)
func = LogMiddleware(func)
    
server = WSGIServer(server_address, func)
```
启动 server，对 socket 进行监听
```python
# wsgiserver/__init__.py  1766
while self.ready:
    self.tick()
```
tick() 对 socket 进行监听并封装为 HTTPConnection，放在同步队列中
```python
# wsgiserver/__init__.py  1856
self.requests.put(conn)
```
多线程处理函数从同步列表中获得 conn
```python
# wsgiserver/__init__.py  1360
conn = self.server.requests.get()
conn.communicate()
```
通过 HTTPRequest 来处理请求
```python
# wsgiserver/__init__.py  1230
req = self.RequestHandlerClass(self.server, self)
req.parse_request()
req.respond()
```
通过 HTTPRequest 解析请求
```python
# wsgiserver/__init__.py  530
self.rfile = SizeCheckWrapper(self.conn.rfile,
                                      self.server.max_request_header_size)
```
调用 HTTPRequest 的 respond
```python
# wsgiserver/__init__.py  770
self.server.gateway(self).respond()
```
再由 WSGI 处理，WSGI 在 HTTPServer 和 app 中作为一个中介，屏蔽了 app 对 server 的操作细节，方便独立开发应用
```python
# wsgiserver/__init__.py  2020
response = self.req.server.wsgi_app(self.env, self.start_response)
```
最后回到 application，调用 wsgifun，其中会先调用 process
```python
# application  260
result = self.handle_with_processors()
```
应用的返回数据由 wsgi.write 返给客户端
```python
# wsgiserver/__init__.py  2030
self.write(chunk)
```
wsgi 实际把 chunk 传递给 HTTPRequest
```python
# wsgiserver/__init_.py  2090
self.req.write(chunk)
```
HTTPRequest 再把数据交给 HTTPConnection，由 socket 文件处理
```python
# wsgiserver/__init__.py  820
self.conn.wfile.sendall(chunk)

# wsgiserver/__init__.py  1220
self.wfile = makefile(sock, "wb", self.wbufsize)
```


##  OS 模块

[Python 模块学习：os模块][41]

```python
# 分离文件名与扩展名
>>> os.path.splitext('a.txt')
('a', '.txt')
# 返回文件名
>>> os.path.basename('a.txt')
'a.txt'
>>> os.path.basename('c:\\Python\\a.txt')
'a.txt'
>>> 
```

**__import 函数**

[import,reload,__import__在python中的区别][42]

__import__ 是一个函数，接受字符串作为参数；通常在动态加载时可以使用这个函数，加载不同的字符串完成不同的加载作用

```python
__import__(module_name[, globals[, locals[, fromlist]]]) #可选参数默认为globals(),locals(),[]
__import__('os')    
__import__('os',globals(),locals(),['path','pip'])  #等价于from os import path, pip
```

**__class__**
使用一个对象获得它的类，可以用来处理作为所有实例公共的变量
```python
class T:
    n = 0
    def __init__(self):
        print "__init__"

    def __call__(self):
        print "__call__"

t = T()
t() # 才会调用 __call__
print t.n # 输出 0

t.__class__.n = 5
s = T()
print s.n # 输出 5
```


  [1]: http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819879946007bbf6ad052463ab18034f0254bf355000
  [2]: http://blog.csdn.net/xyw_blog/article/details/18401237
  [3]: http://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00%00
  [4]: ./images/1472207911474.jpg "1472207911474.jpg"
  [5]: http://www.cnblogs.com/huxi/archive/2011/06/18/2084316.html
  [6]: http://www.cnblogs.com/huxi/archive/2011/06/24/2089358.html
  [7]: http://www.cnblogs.com/vamei/archive/2012/12/15/2772451.html
  [8]: http://www.cnblogs.com/fnng/p/3699893.html
  [9]: http://kodango.com/variable-arguments-in-python
  [10]: .//Passing%20arguments%20to%20Python%20functions1.pdf
  [11]: http://cenalulu.github.io/linux/character-encoding/
  [12]: http://www.ruanyifeng.com/blog/2007/10/ascii_unicode_and_utf-8.html
  [13]: http://www.cnblogs.com/BeginMan/p/3197649.html
  [14]: https://www.restran.net/2015/10/22/how-python-code-run/
  [15]: http://www.cnblogs.com/way_testlife/archive/2011/03/29/1999283.html
  [16]: http://www.tuicool.com/articles/mE3QJ3
  [17]: http://blog.csdn.net/digimon/article/details/7875789
  [18]: http://www.jianshu.com/p/90348ef3f41e
  [19]: http://blog.csdn.net/jiajia4336/article/details/8798421
  [20]: http://blog.163.com/alice_leee/blog/static/167106323201062332816623/
  [21]: ./images/1466861848287.jpg "1466861848287.jpg"
  [22]: ./images/1466861895747.jpg "1466861895747.jpg"
  [23]: http://www.cnblogs.com/nightwatcher/archive/2011/07/03/2096717.html
  [24]: http://blog.sina.com.cn/s/blog_9f488855010198vn.html
  [25]: http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
  [26]: http://www.cnblogs.com/fnng/p/3670789.html
  [27]: http://blog.sina.com.cn/s/blog_9f488855010198vn.html
  [28]: http://www.cnblogs.com/shiyangxt/archive/2008/10/07/1305506.html
  [29]: http://www.blogs8.cn/posts/Wx8G9b8
  [30]: ./images/1466930857819.jpg "1466930857819.jpg"
  [31]: https://www.douban.com/note/13508388/
  [32]: http://diaocow.iteye.com/blog/1922760
  [33]: http://linluxiang.iteye.com/blog/799163
  [34]: http://blog.csdn.net/on_1y/article/details/18803563
  [35]: http://www.letiantian.me/2015-09-10-understand-python-wsgi/
  [36]: https://segmentfault.com/a/1190000003069785
  [37]: ./images/1467896540337.jpg "1467896540337.jpg"
  [38]: http://python.usyiyi.cn/python_278/library/queue.html
  [39]: https://blog.linuxeye.com/334.html
  [40]: http://www.jianshu.com/p/544d406e0875
  [41]: http://www.cnblogs.com/BeginMan/p/3327291.html
  [42]: http://blog.csdn.net/five3/article/details/7762870
