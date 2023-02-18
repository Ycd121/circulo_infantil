# Generated by Django 4.1.7 on 2023-02-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familypickup',
            name='child_family_pickup',
            field=models.ManyToManyField(related_name='child_family_pickup', to='main.child'),
        ),
        migrations.AddField(
            model_name='intolerance',
            name='child_intolerance',
            field=models.ManyToManyField(related_name='child_intolerance', to='main.child'),
        ),
        migrations.AddField(
            model_name='tutor',
            name='child_tutor',
            field=models.ManyToManyField(related_name='child_tutor', to='main.child'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='child_disease',
            field=models.ManyToManyField(blank=True, null=True, related_name='child_disease', to='main.child'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='salary',
            field=models.FloatField(),
        ),
    ]