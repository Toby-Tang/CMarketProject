from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.models import User, auth


from .models import Question, Choice


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


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'CMarket/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'CMarket/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'CMarket/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (Keydisp, Choice.DoesNotExist):
        return render(request, 'CMarket/detail.html', {
            'question': question,
            'disp_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
