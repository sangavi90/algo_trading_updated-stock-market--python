# Generated by Django 5.0.3 on 2024-04-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_alter_signinuser_user_id_alter_strategy_strategy_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signinuser',
            name='user_id',
            field=models.CharField(default='6646648026847837221178', max_length=100),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='strategy_id',
            field=models.CharField(default='8D80880587592463038785772', max_length=100),
        ),
    ]
