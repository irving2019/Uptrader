from django.db import migrations

from app.models import TreeMenu, TreeMenuCategory


def create_menu(*args, **kwargs):
    category = TreeMenuCategory.objects.create(name="main", verbose_name="Главная")
    main = TreeMenu.objects.create(name="Главная", category=category, path="main")
    contact_us = TreeMenu.objects.create(name="Контакты", category=category, parent= main, path="contact_us")
    TreeMenu.objects.create(name="Связь с общественностью", category=category, parent=contact_us, path="public_relations")
    TreeMenu.objects.create(name="Реклама", category=category, parent=contact_us, path="adverts")
    TreeMenu.objects.create(name="Форум", category=category, path="forum")
    how = TreeMenu.objects.create(name="Как", category=category, path="how")
    TreeMenu.objects.create(name="Нас найти", category=category, parent=how, path="us_search")
    registration = TreeMenu.objects.create(name="Регистрация или", category=category, path="registration")
    TreeMenu.objects.create(name="Вход", category=category, parent=registration, path="enter")
    TreeMenu.objects.create(name="Восстановить пароль", category=category, parent=registration, path="change_password")


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_menu, migrations.RunPython.noop)
    ]
