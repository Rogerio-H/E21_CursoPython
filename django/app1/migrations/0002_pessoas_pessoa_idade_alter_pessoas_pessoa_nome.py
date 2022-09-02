# Generated by Django 4.1 on 2022-08-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoas',
            name='pessoa_idade',
            field=models.IntegerField(default=0, verbose_name='Idade'),
        ),
        migrations.AlterField(
            model_name='pessoas',
            name='pessoa_nome',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
    ]