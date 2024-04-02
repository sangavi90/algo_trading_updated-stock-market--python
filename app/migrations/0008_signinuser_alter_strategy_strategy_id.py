# Generated by Django 5.0.3 on 2024-03-27 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_strategy_status_alter_strategy_strategy_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignInUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
        migrations.AlterField(
            model_name='strategy',
            name='strategy_id',
            field=models.CharField(default='A91915079341676010', max_length=100),
        ),
    ]
