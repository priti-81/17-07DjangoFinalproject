# Generated by Django 4.2 on 2023-06-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynote', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Technology', models.CharField(max_length=20)),
                ('Explaination', models.TextField()),
                ('Files', models.FileField(upload_to='media')),
            ],
        ),
    ]
