# Generated by Django 4.1.4 on 2022-12-30 21:06

from django.db import migrations, models
import polling_auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('polling_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', polling_auth.models.PollingUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email_address'),
        ),
    ]
