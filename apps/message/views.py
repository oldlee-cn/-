from django.shortcuts import render
#导入models.py中'创建表的类'
from .models import FromTable

# Create your views here.

#调用render函数，返回静态html文件到页面
def getfrom(request):

    #先定义一个变量：👇

    messages = None

    #对指定对数据进行赋值，赋值结果是一个列表
    all_messages = FromTable.objects.filter(username='bobby')
    #对全部数据的结果进行循环遍历，然后就可以像操作类一样操作数据表
    for messages in all_messages:
        #将赋值结果的第一条赋值给上面的变量
        messages = all_messages[0]


    return render(request,'message_from.html',{
        #把变量值传递给my_messages，然后就可以在html中使用my_messages进行取值
        "my_messages":messages
    })
    #首先判断是否是POST提交：
    # if request.method == 'POST':
    #     #其实，html表单提交的数据是个字典，也就是键值对，这样就可以用get()方法来取字典里的值
    #     #把html提交的字典里的username复制给变量username，默认值为空
    #     username = request.POST.get('name','')
    #     email = request.POST.get('email','')
    #     address = request.POST.get('address','')
    #     message = request.POST.get('message','')
    # #然后利用变量值向数据表内插入数据，然后调用save()方法来保存即可
    # fromtable = FromTable()
    # fromtable.username = username
    # fromtable.email = email
    # fromtable.adsress = address
    # fromtable.message = message
    # fromtable.object_id = ''
    # fromtable.save()

