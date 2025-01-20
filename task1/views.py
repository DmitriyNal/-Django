from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from task1.form import UserRegister
from task1.models import Buyer, Auto


def index(request):
    title = 'Главная страница'
    auto = 'Автомобили в наличии'
    offers = 'Специальные предложения'
    context = {'title': title, 'auto': auto, 'offers': offers}

    return render(request, "fourth_task/main.html", context)


def home_page(request):
    title = 'Главная страница'
    shop = 'Магазин'
    credit = 'Кредит'
    choise = 'Выберите раздел'
    context = {'title': title, 'shop': shop, 'credit': credit, 'choise': choise}

    return render(request, "fourth_task/Base.html", context)


class IndexView(TemplateView):
    template_name = 'fourth_task/kredit.html'


def sign_up_by_htm(request):
    info = {}  # Пустой словарь для передачи в context функции render

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        print(f'login: {login} ,password:{password} ,age:{age}')
        # Получение всех записей из таблицы Buyer
        buyers = Buyer.objects.all()
        # Получение всех записей из таблицы Buyer
        for buyer in buyers:
            if buyer.name == login:
                return HttpResponse(f'"Пользователь с таким логином уже существует"')
        # Получение всех записей из таблицы Buyer
        buyer = Buyer(name=login, balance=1000, age=age)
        buyer.save()
        return HttpResponse(f'{buyer.name} успешно зарегистрирован')

    return render(request, 'fifth_tas/egistration_page.html', info)


def get_auto(request):
    cars = Auto.objects.all()
    context = {'cars': cars}
    return render(request, 'fifth_tas/auto.html', context)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(f'login: {login} ,password:{password} ,age:{age}')
            if password == repeat_password and age >= 18 and login not in users:
                return HttpResponse(f'"Приветствуем, {login}"')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_tas/egistration_page.html', info)
