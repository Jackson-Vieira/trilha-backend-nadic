# Generated by Django 3.2.16 on 2022-12-04 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_auto_20221204_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registry',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresa.company'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registry',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresa.product'),
            preserve_default=False,
        ),
    ]
