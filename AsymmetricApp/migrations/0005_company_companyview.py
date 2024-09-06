# Generated by Django 5.1 on 2024-09-06 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AsymmetricApp', '0004_worksforuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=99)),
                ('company_image', models.ImageField(upload_to='company_images/')),
                ('company_phone', models.CharField(max_length=33)),
                ('accepts_workers', models.BooleanField(default=False)),
                ('company_builded_at', models.CharField(max_length=255)),
                ('the_company_exists', models.CharField(max_length=300)),
                ('CEO_of_the_company', models.CharField(max_length=66)),
                ('how_many_employees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CompanyView',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_company', models.CharField(max_length=99)),
                ('detail_of_company', models.TextField()),
                ('accepts_workers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepts_workers_views', to='AsymmetricApp.company')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_views', to='AsymmetricApp.company')),
                ('company_builded_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_build_dates_views', to='AsymmetricApp.company')),
                ('company_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_images_views', to='AsymmetricApp.company')),
            ],
        ),
    ]
