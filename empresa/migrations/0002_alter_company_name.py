# Generated by Django 3.2.16 on 2022-12-03 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='name'),
        ),
    ]