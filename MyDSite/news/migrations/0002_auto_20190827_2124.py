# Generated by Django 2.2.4 on 2019-08-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('annotation', models.CharField(max_length=256)),
                ('content', models.CharField(max_length=1024)),
                ('link', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=100)),
                ('publish', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
