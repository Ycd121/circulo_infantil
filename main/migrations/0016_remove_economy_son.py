# Generated by Django 4.1.7 on 2023-03-02 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_room_code_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='economy',
            name='son',
        ),
    ]