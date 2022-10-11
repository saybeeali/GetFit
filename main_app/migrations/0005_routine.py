# Generated by Django 4.1.2 on 2022-10-11 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_exercise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('exercises', models.ManyToManyField(to='main_app.exercise')),
            ],
        ),
    ]
