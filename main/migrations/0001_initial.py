# Generated by Django 5.1.7 on 2025-03-16 06:13

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ism', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('profession', models.CharField(max_length=255)),
                ('KPI', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guruh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('nom', models.CharField(max_length=255)),
                ('vaqt', models.TimeField(blank=True, null=True)),
                ('finshed_at', models.DateField(blank=True, null=True)),
                ('mentor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.mentor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ism', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=15)),
                ('phone_number', models.CharField(max_length=15)),
                ('age', models.PositiveSmallIntegerField()),
                ('guruh', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.guruh')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tolov',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('izoh', models.TextField(blank=True, null=True)),
                ('miqdor', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.student')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
