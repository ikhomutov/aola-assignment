# Generated by Django 4.1.4 on 2022-12-13 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('article', 'article'), ('advertisement', 'advertisement'), ('achievement', 'achievement')], max_length=100)),
                ('title', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('object_id', models.PositiveIntegerField(blank=True, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name_plural': 'FeedEntries',
                'ordering': ('timestamp',),
            },
        ),
    ]