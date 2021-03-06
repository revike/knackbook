# Generated by Django 3.2.4 on 2021-07-01 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_article_tags'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='актив')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_from', to=settings.AUTH_USER_MODEL, verbose_name='пользователь-создатель')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_to', to=settings.AUTH_USER_MODEL, verbose_name='пользователь-получатель')),
            ],
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='актив')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commentapp.comment', verbose_name='комментарий')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='LikeArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='актив')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создан')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.article', verbose_name='статья')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
        ),
    ]
