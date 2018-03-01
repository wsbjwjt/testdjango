# -*- encoding: UTF-8 -*-

from django.shortcuts import render
from .models import UserMessage

# Create your views here.

def getform(request):
    # 方法一
    # all_message = UserMessage.objects.all()
    # all_message = UserMessage.objects.filter(name="wjt", address=u"北京")
    # for message in all_message:
        # print(message.name)

    # user_message = UserMessage()

    # user_message.name = "wjt"
    # user_message.email = "wsbjwjt@163.com"
    # user_message.address = "北京"
    # user_message.message = "我爱北京天安门"
    #
    # user_message.save()

    # 此处对应html中的method="post"，表示我们只处理post请求
    # if request.method == "POST":
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     message = request.POST.get('message', '')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.message = message
    #     user_message.object_id = 'ijkl'
    #
    #     user_message.save()

    message = None

    all_message = UserMessage.objects.filter(name='wsbjwjt', email='wsbjwjt@foxmail.com')

    if all_message:
        message = all_message[0]

    return render(request, 'message_form.html', {
        "my_message": message
    })