# Generated by Django 3.0.6 on 2020-05-12 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='subject',
        ),
    ]