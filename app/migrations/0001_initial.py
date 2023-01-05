# Generated by Django 3.2.15 on 2023-01-05 18:28

import app.models
from django.db import migrations, models


def create(apps, schema_editor):
    Form = apps.get_model('app', 'Form')
    Form(
        name='MyForm',
        email='asd@asd.asd',
        phone='+71111111111',
        date='2023-01-05',
        text='Bla bla',
    ).save()
    Form(
        name='MyForm10',
        email='asd1@asd.asd',
        phone='+72222222222',
        date='2023-01-06',
        text='Bla bla alsldlasd',
    ).save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.CharField(default=app.models.generate_random_id, editable=False, max_length=64,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=64)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('date', models.DateField(auto_now_add=True, unique=True)),
                ('text', models.TextField(max_length=1024)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.RunPython(create),
    ]