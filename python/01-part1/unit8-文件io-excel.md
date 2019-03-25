# 文件I/O-excel

## 读写数据

1. 安装 openpyxl

    ```
        pip install openpyxl
    ```
2. 打开文件

    ```
        from openpyxl import load_workbook

        from openpyxl.writer.excel import ExcelWriter

        try:
            workbook_ = load_workbook(u"data.xlsx")
            # 获得表单名字
            sheetnames = workbook_.get_sheet_names()

            sheet = workbook_.get_sheet_by_name(sheetnames[0])
        except Exception as ex:
            print(ex)

    ```
3. 获取单元格

    ```
        # 获取某个单元格的值，观察excel发现也是先字母再数字的顺序，即先列再行
        b4 = sheet['A4']  #A行4列

        # 除了用下标的方式获得，还可以用cell函数, 换成数字，这个表示B4
        b4_too = sheet.cell(row=4, column=2)
        print(b4_too.value)


        for i in range(2):
            for j in range(5):
                print(sheet.cell(row=i+1, column=j+1).value,end=' ')
            print()
    ```
4. 获得最大行和最大列

    ```
        # 获得最大列和最大行
        print(sheet.max_row)
        print(sheet.max_column)


    ```
5. 获取行和列

    ```
        sheet.rows为生成器, 里面是每一行的数据，每一行又由一个tuple包裹。
        sheet.columns类似，不过里面是每个tuple是每一列的单元格。
    ```

    ```
        # 因为按行，所以返回A1, B1, C1这样的顺序
        for row in sheet.rows:
            for cell in row:
                print(cell.value)

        # A1, A2, A3这样的顺序
        for column in sheet.columns:
            for cell in column:
                print(cell.value)
    ```

    >上面的代码就可以获得所有单元格的数据。如果要获得某行的数据呢？给其一个索引就行了，因为sheet.rows是生成器类型，不能使用索引，转换成list之后再使用索引，list(sheet.rows)[2]这样就获取到第三行的tuple对象。

    ```
        for cell in list(sheet.rows)[2]:
            print(cell.value)
    ```

6. 切片获取

    还可以像使用切片那样使用。sheet['A1':'B3']返回一个tuple，该元组内部还是元组，由每行的单元格构成一个元组。

    ```
        for row_cell in sheet['A1':'B3']:
            for cell in row_cell:
                print(cell)
    ```

## 写入数据

1. 完整案例

    ```
        from openpyxl import Workbook

        from openpyxl import load_workbook

        from openpyxl.writer.excel import ExcelWriter

        try:

            #     新建工作表
            wb=Workbook()
            # 新建一个工作表，可以指定索引，适当安排其在工作簿中的位置
            sheet=wb.create_sheet('Data', index=1)  # 被安排到第二个工作表，index=0就是第一个位置

            # 删除某个工作表
            # wb.remove(wb)
            # del wb[sheet]
            # row = [1, 2, 3, 4, 5]
            # sheet.append(row)
            rows = [
                ['Number', 'data1', 'data2'],
                [2, 40],
                [3, 40, 25],
                [4, 50, 30],
                [5, 30, 10],
                [6, 25, 5],
                [7, 50, 10111],
            ]
            for row in rows:
                sheet.append(row)
            wb.save(r'新歌检索失败1477881109469.xlsx')
        except Exception as ex:
            print(ex)
    ```