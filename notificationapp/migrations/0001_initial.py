# Generated by Django 3.2.4 on 2021-07-01 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0002_article_tags'),
        ('commentapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='содержимое уведомления')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('closed', models.DateTimeField(blank=True, null=True, verbose_name='закрыто')),
                ('is_active', models.BooleanField(db_index=True, default=True, verbose_name='актив')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.article', verbose_name='статья')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commentapp.comment', verbose_name='комментарий')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_user_from', to=settings.AUTH_USER_MODEL, verbose_name='пользователь-создатель')),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='note_user_to', to=settings.AUTH_USER_MODEL, verbose_name='пользователь-получатель')),
            ],
        ),
    ]
