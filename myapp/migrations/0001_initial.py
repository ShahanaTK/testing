# Generated by Django 3.2.16 on 2023-04-13 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
            ],
        ),
    ]
