# Generated by Django 5.1 on 2024-09-06 06:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsymmetricApp', '0003_casestudiesdatas'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorksForUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(max_length=230)),
                ('practice', models.CharField(max_length=66)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=44)),
                ('icon_for_user_account', models.ImageField(upload_to='icons_for_acc/')),
                ('my_comment_on_this_site', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('practice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_practice', to='AsymmetricApp.worksforuser')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_work', to='AsymmetricApp.worksforuser')),
            ],
        ),
    ]