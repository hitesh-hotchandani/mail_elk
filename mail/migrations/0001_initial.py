# Generated by Django 2.2.3 on 2019-07-09 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, max_length=8000)),
                ('attachment', models.TextField(blank=True, max_length=8000)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('to', models.EmailField(max_length=254)),
                ('cc', models.EmailField(blank=True, max_length=254)),
                ('bcc', models.EmailField(blank=True, max_length=254)),
                ('subject', models.CharField(blank=True, max_length=100)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mail.Content')),
            ],
        ),
    ]
