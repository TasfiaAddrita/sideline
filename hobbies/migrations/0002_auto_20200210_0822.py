# Generated by Django 3.0.3 on 2020-02-10 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobbies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hobbies',
            old_name='title',
            new_name='name',
        ),
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('hobby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hobbies.Hobbies')),
            ],
        ),
    ]