# Generated by Django 4.2.2 on 2023-06-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('admin', 'Администратор'), ('user', 'Пользователь')], default='user', help_text='Роль пользователя', max_length=20),
        ),
    ]
