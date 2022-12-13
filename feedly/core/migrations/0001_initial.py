# Generated by Django 4.1.4 on 2022-12-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('condition', models.TextField()),
                ('icon', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('published_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SiteUserAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('got_at', models.DateTimeField(auto_now_add=True)),
                ('achievement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.achievement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.siteuser')),
            ],
            options={
                'unique_together': {('user', 'achievement')},
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='core.siteuser')),
            ],
        ),
        migrations.AddField(
            model_name='achievement',
            name='users',
            field=models.ManyToManyField(through='core.SiteUserAchievement', to='core.siteuser'),
        ),
    ]
