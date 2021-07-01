# Generated by Django 3.2.4 on 2021-06-30 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=1, verbose_name='возраст'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Мужской'), ('W', 'Женский')], max_length=1, verbose_name='пол'),
        ),
    ]