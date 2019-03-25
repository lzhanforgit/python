# Xpath 
**作者：詹亮**


 1. 节点类型
 1. 选取节点


    | 表达式 | 描述 |
    | --- | --- |
    | nodename | 选取此节点的所有子节点。 |
    | / |  从根节点选取|
    |//| <span style='color:red'>从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。</span> |
    | . | 选取当前节点。 |
    | .. | 选取当前节点的父节点。 |
    | @ | 选取属性。 |

3. 带谓词的选取

    | 路径表达式 |	结果 |
    | --- | --- |
    |/bookstore/book[1]	|选取属于 bookstore 子元素的第一个 book 元素。|
    |/bookstore/book[last()]	|选取属于 bookstore 子元素的最后一个 book 元素。|
    |/bookstore/book[last()-1]	|选取属于 bookstore 子元素的倒数第二个 book 元素。|
    |/bookstore/book[position()<3]	|选取最前面的两个属于 bookstore 元素的子元素的 book 元素。|
    |//title[@lang]	|选取所有拥有名为 lang 的属性的 title 元素。|
    |//title[@lang='eng']	|选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。|
    |/bookstore/book[price>35.00]	|选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。|
    |/bookstore/book[price>35.00]/title	|选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。|

    **选取未知节点**
    
    |路径表达式|	结果|
    | --- | --- |
    |/bookstore/*	|选取 bookstore 元素的所有子元素。|
    |//*	|选取文档中的所有元素。|
    |//title[@*]	|选取所有带有属性的 title 元素。|
    
    **选取若干路径**
    
    |路径表达式|	结果|
    | --- | --- |
    |//book/title \| //book/price	|选取 book 元素的所有 title 和 price 元素。
    |//title \| //price	|选取文档中的所有 title 和 price 元素。
    |/bookstore/book/title \| //price	|选取属于 bookstore 元素的 book 元素的所有 title 元素，以及文档中所有的 price 元素。|


