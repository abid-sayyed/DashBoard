# Generated by Django 4.2.6 on 2023-10-14 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.CharField(blank=True, max_length=4)),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=100)),
                ('start_year', models.CharField(blank=True, max_length=4)),
                ('impact', models.CharField(blank=True, max_length=100)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(blank=True, max_length=100)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
