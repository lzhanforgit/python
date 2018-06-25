# 函数

1. 定义一个函数

    你可以定义一个由自己想要功能的函数，以下是简单的规则：

    * 函数代码块以 def 关键词开头，后接函数标识符名称和圆括号()。
    * 任何传入参数和自变量必须放在圆括号中间。圆括号之间可以用于定义参数。
    * 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
    * 函数内容以冒号起始，并且缩进。
    * return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
2. 可更改(mutable)与不可更改(immutable)对象


    在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    
    1. 不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。    
    3. 可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。
    
    python 函数的参数传递：
    
    1. 不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。  
    3. 可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
    
    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。
    
3. 参数
    
   以下是调用函数时可使用的正式参数类型：
   
    *    必备参数
    *    关键字参数
    *    默认参数
    *    不定长参数

    ```
    def show(name,age=12):
    print('name is:',name,'and age is',age)
    return

    # show()   #error
    
    show('tom',22)
    
    show(name='jack',age=32)
    show(name='rose')
    show(age=32,name='nick')
    ```

    **不定长参数**
    
    ```
    def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print "输出: "
   print arg1
   for var in vartuple:
      print var
   return;
 
    # 调用printinfo 函数
    printinfo( 10 );
    printinfo( 70, 60, 50 );
    ```
1. 匿名参数

    python 使用 lambda 来创建匿名函数。

    lambda只是一个表达式，函数体比def简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
    
    ```
    nation='china'
show=lambda name,age=12: print('name is:',name,'and age is',age,nation)
    ```
2. 变量作用域
    一个程序的所有的变量并不是在哪个位置都可以访问的。访问权限决定于这个变量是在哪里赋值的。
    
    变量的作用域决定了在哪一部分程序你可以访问哪个特定的变量名称。两种最基本的变量作用域如下：
    2. 全局变量
    3. 局部变量
    全局变量和局部变量
    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
    
    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。
    
3. 全局变量想作用于函数内，需加 global

    ```
    nation='china'
def show(name,age=12):
        global nation
        nation='usa'
        print('name is:',name,'and age is',age,'and nation is',nation)
        return

    # show()
    
    show('tom',22)
    
    
    print(nation)
    ```

    ```
    def add_b():
        global  b
        b = 42
        def do_global():
            global  b
            b = b + 10
            print(b)
        do_global()
        print(b)
    add_b()
    print(b)
    ```
    
    ```
    def add_b():
        #global  b
        b = 42
        def do_global():
            global  b
            b =  10
            print(b)
        do_global()
        print(b)
    add_b()
    print(" b = %s " % b)
    ```
7. 内置作用域（LEBG）
    
    ```
        import builtins
        print(dir(builtins  ))
    ```
    >内置文件中前一部分是内置异常，后一部分是内置函数。
8. lambda

    ```
        arr=[1,2,3,4,5,6]

        lam=lambda array:[i for i in array if i%2==0]
        
        arr2=lam(arr)
        
        print(arr2)
    ```
    
    函数嵌套
    
    ```
    def func():
        x=4
        action = (lambda n: x**n)      # Pass x in lIlanllally return action
        return action
    
    
    def makeAction():
        acts=[]
        for i in range(5):
            acts.append((lambda x:i**x))
        return acts
    
    atcs=makeAction()
    
    print(atcs[1](3))
    print(atcs[3](3))
    
    
    def makeActionB():
        acts=[]
        for i in range(5):
            acts.append((lambda x,i=i:i**x))  # i=i
        return acts
    
    atcsb=makeActionB()
    
    print(atcsb[1](3))
    print(atcsb[3](3))
    
    ```
9. nonlocal

    nonlocal关键字用来在函数或其他作用域中使用外层(非全局)变量。
    
    ```
    def outer():
        x=100
        def inner():
            nonlocal x
            x=x+1000
            print(x)
    
        return inner
    
    inner=outer()
    
    inner()
    ```

