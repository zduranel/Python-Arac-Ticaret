# Generated by Django 3.0.4 on 2020-03-31 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='setting',
            name='smptemail',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smptpassword',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpserver',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
