# Generated by Django 4.0.2 on 2022-03-08 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secopy_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=320)),
                ('password', models.CharField(max_length=50)),
                ('organisation', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
