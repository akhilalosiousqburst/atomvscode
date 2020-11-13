# Generated by Django 3.1.3 on 2020-11-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phonenumber', models.IntegerField(default='')),
                ('description', models.CharField(default='', max_length=20)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]