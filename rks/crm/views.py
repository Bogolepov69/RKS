from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Order, main
from django import forms


def order_list(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'order_list.html', context)


def Client(request):
    client = Client.objects.all()
    context = {'client': client}
    return render(request, 'crm/client.html', context)


def main(request):
    title = 'Главная страница'
    context = {'title': title}
    return render(request, 'main.html', context)


class UserRegister(forms.Form):
    username = forms.CharField(label="Введите логин", max_length=30)
    password = forms.CharField(label="Введите пароль", min_length=8, widget=forms.PasswordInput)
    repeat_password = forms.CharField(label="Повторите пароль", min_length=8, widget=forms.PasswordInput)
    age = forms.IntegerField(label="Введите свой возраст", max_value=150, min_value=0)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            buyer_exists = Client().objects.filter(username=username).exists()
            if password == repeat_password and age >= 18 and not buyer_exists:
                Client().objects.create(username=username, password=password, age=age)
                info['message'] = f"Приветствуем, {username}!"
                return redirect('register')
            else:
                if password != repeat_password:
                    info['error'] = 'Пароли не совпадают'
                elif age < 18:
                    info['error'] = 'Вы должны быть старше 18'
                else:
                    info['error'] = 'Пользователь уже существует'
        else:
            info['error'] = 'Некорректные данные в форме'
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'main.html', info)


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    context = {
        'order': order,
    }
    return render(request, 'order_detail.html', context)
