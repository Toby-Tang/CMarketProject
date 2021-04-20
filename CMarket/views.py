from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User, auth
from .models import Message, Post


def home(request):
    return render(request, "CMarket/home.html")


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif not request.POST:
        return render(request, "CMarket/login.html")
    else:
        mode = request.POST["mode"]
        if mode == "login":
            username = request.POST["username"]
            password = request.POST["password"]
            temp = auth.authenticate(username=username, password=password)
            if not temp:
                return render(request, "CMarket/login.html", {"disp": "This username and password does not exist."})
            else:
                auth.login(request, temp)
                return redirect("/")
        elif mode == "signup":
            username = request.POST["username"]
            password = request.POST["password"]
            if User.objects.filter(username=username).exists():
                return render(request, "CMarket/login.html", {"disp": "This username is already in use."})
            temp = User.objects.create_user(username=username, password=password)
            auth.login(request, temp)
            return redirect("/")
        else:
            return render(request, "CMarket/login.html", {"disp": "An unexpected error has occurred..."})


def post(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    elif not request.POST:
        return render(request, "CMarket/post.html")
    else:
        origin = request.user
        target = request.POST["target"]
        content = request.POST["message"]
        if target == "":
            try:
                Post.objects.create(content=content, origin=origin)
                return render(request, "CMarket/post.html", {"status": "Post success!"})
            except:
                return render(request, "CMarket/post.html", {"status": "An expected error has occurred."})
        else:
            try:
                Message.objects.create(target=target, content=content, origin=origin)
                return render(request, "CMarket/post.html", {"status": "Message successfully sent!"})
            except:
                return render(request, "CMarket/post.html", {"status": "An expected error has occurred."})


def public(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "CMarket/public.html", context)


def private(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    temp = Message.objects.all()
    messages = [i for i in temp if i.target == request.user.username]
    context = {"messages": messages}
    return render(request, "CMarket/private.html", context)
