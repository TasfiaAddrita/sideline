# Generated by Django 3.0.3 on 2020-02-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0005_auto_20200224_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attend',
            name='choice',
            field=models.CharField(default='Attending', max_length=200),
        ),
    ]
