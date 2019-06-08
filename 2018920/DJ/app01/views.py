from django.shortcuts import render,HttpResponse
# from templates import
# Create your views here.
def test(request):
    import pymysql

    # 创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='blogyuan')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 执行SQL，并返回收影响行数
    effect_row = cursor.execute("select * from test")

    # 执行SQL，并返回受影响行数
    # effect_row = cursor.execute("update hosts set host = '1.1.1.2' where nid > %s", (1,))

    # 执行SQL，并返回受影响行数
    # effect_row = cursor.executemany("insert into hosts(host,color_id)values(%s,%s)", [("1.1.1.11",1),("1.1.1.11",2)])

    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
    data=cursor.fetchall()
    print(data)


    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return  render(request,'test.html',{'data':data})