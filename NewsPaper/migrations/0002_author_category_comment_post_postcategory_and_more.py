# Generated by Django 4.2.1 on 2023-05-30 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NewsPaper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ratingAuthor', models.SmallIntegerField(default=0)),
                ('authorUser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('datetime_comment', models.DateTimeField(auto_now_add=True)),
                ('rating', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryType', models.CharField(choices=[('NW', 'Новость'), ('AR', 'Ствтья')], default='AR', max_length=2)),
                ('dateCreation', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=128)),
                ('text', models.TextField()),
                ('rating', models.SmallIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.category')),
                ('postThrough', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post')),
            ],
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='order',
        ),
        migrations.RemoveField(
            model_name='productorder',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductOrder',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.AddField(
            model_name='post',
            name='postCategory',
            field=models.ManyToManyField(through='NewsPaper.PostCategory', to='NewsPaper.category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentPost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NewsPaper.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='commentUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
