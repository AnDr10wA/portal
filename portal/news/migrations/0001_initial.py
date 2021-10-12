# Generated by Django 3.2.8 on 2021-10-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('slug', models.SlugField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('head', models.TextField(blank=True, db_index=True)),
                ('image', models.ImageField(upload_to='media/news/')),
                ('body', models.TextField(blank=True, db_index=True)),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, related_name='news', to='news.Tag')),
            ],
            options={
                'ordering': ('-title',),
            },
        ),
    ]
