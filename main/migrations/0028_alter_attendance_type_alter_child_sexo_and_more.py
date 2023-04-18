# Generated by Django 4.1.7 on 2023-04-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_attendance_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='type',
            field=models.CharField(choices=[('presente', 'presente'), ('ausencia', 'ausencia'), ('certificado', 'certificado'), ('vacaciones', 'vacaciones')], default='presente', max_length=255, verbose_name='Típo'),
        ),
        migrations.AlterField(
            model_name='child',
            name='sexo',
            field=models.CharField(choices=[('Femenino', 'Femenino'), ('Masculino', 'Masculino')], default='female', max_length=10, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='code_disease',
            field=models.CharField(max_length=8, unique=True, verbose_name='Código de Enfermedades'),
        ),
        migrations.AlterField(
            model_name='intolerance',
            name='code_into',
            field=models.CharField(max_length=8, unique=True, verbose_name='Código de Intolerancia'),
        ),
    ]
