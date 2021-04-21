from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import Message, Post


def home(request):
    if request.user.is_authenticated:
        return render(request, "CMarket/home.html", {"acc_disp": f"Log out ({request.user.username})"})
    else:
        return render(request, "CMarket/home.html", {"log_disp": "Log in or create account"})


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    elif not request.POST:
        return render(request, "CMarket/login.html", {"log_disp": "Log in or create account"})
    else:
        mode = request.POST["mode"]
        if mode == "login":
            username = request.POST["username"]
            password = request.POST["password"]
            temp = auth.authenticate(username=username, password=password)
            if not temp:
                return render(request, "CMarket/login.html", {"disp": "This username and password does not exist.",
                                                              "log_disp": "Log in or create account"})
            else:
                auth.login(request, temp)
                return redirect("/")
        elif mode == "signup":
            username = request.POST["username"]
            password = request.POST["password"]
            if User.objects.filter(username=username).exists():
                return render(request, "CMarket/login.html", {"disp": "This username is already in use.",
                                                              "log_disp": "Log in or create account"})
            temp = User.objects.create_user(username=username, password=password)
            auth.login(request, temp)
            return redirect("/")
        else:
            return render(request, "CMarket/login.html", {"disp": "An unexpected error has occurred...",
                                                          "log_disp": "Log in or create account"})


def post(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    elif not request.POST:
        return render(request, "CMarket/post.html", {"acc_disp": f"Log out ({request.user.username})"})
    else:
        origin = request.user
        target = request.POST["target"]
        content = request.POST["message"]
        if target == "":
            if len(content) > 4000:
                return render(request, "CMarket/post.html", {"status": "Your message was too long!",
                                                             "acc_disp": f"Log out ({request.user.username})"})
            try:
                Post.objects.create(content=content, origin=origin)
                return render(request, "CMarket/post.html", {"status": "Post success!",
                                                             "acc_disp": f"Log out ({request.user.username})"})
            except:
                return render(request, "CMarket/post.html", {"status": "An expected error has occurred.",
                                                             "acc_disp": f"Log out ({request.user.username})"})
        else:
            if len(content) > 4000:
                return render(request, "CMarket/post.html", {"status": "Your message was too long!",
                                                             "acc_disp": f"Log out ({request.user.username})"})
            try:
                Message.objects.create(target=target, content=content, origin=origin)
                return render(request, "CMarket/post.html", {"status": "Message successfully sent!",
                                                             "acc_disp": f"Log out ({request.user.username})"})
            except:
                return render(request, "CMarket/post.html", {"status": "An expected error has occurred.",
                                                             "acc_disp": f"Log out ({request.user.username})"})


def public(request):
    posts = Post.objects.all()
    if request.user.is_authenticated:
        return render(request, "CMarket/public.html", {"posts": posts,
                                                       "acc_disp": f"Log out ({request.user.username})"})
    else:
        return render(request, "CMarket/public.html", {"posts": posts,
                                                       "log_disp": "Log in or create account"})


def private(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    temp = Message.objects.all()
    messages = [i for i in temp if i.target == request.user.username]
    return render(request, "CMarket/private.html", {"messages": messages,
                                                    "acc_disp": f"Log out ({request.user.username})"})


def logout(request):
    auth.logout(request)
    return redirect("/")


def delete_posts(request):
    if request.user.is_authenticated and request.user.username == "admin":
        Post.objects.all().delete()
    return redirect("/")


def delete_messages(request):
    if request.user.is_authenticated:
        for message in Message.objects.all():
            if message.target == request.user.username:
                message.delete()
    return redirect("/")
