from django.urls import path

from .views import base


urlpatterns = [
    path('main/', base, {'name': 'Главная'}, name='main'),
    path('сontact_us/', base, {'name': 'Наши Контакты'}, name='contact_us'),
    path('contact_us/public_relations/', base, {'name': 'Связь с Общественностью'}, name='public_relations'),
    path('contact_us/advertising/', base, {'name': 'Реклама'}, name='adverts'),
    path('forum/', base, {'name': 'Форум'}, name='forum'),
    path('howses/', base, {'name': 'Как'}, name='how'),
    path('howses/us_search/', base, {'name': 'Нас найти'}, name='us_search'),
    path('registration/', base, {'name': 'Регистрация или'}, name='registration'),
    path('registration/enter/', base, {'name': 'Вход'}, name='enter'),
    path('registration/change_password/', base, {'name': 'Восстановить пароль'}, name='change_password'),
]

