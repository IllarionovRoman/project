# Generated by Django 4.1.7 on 2023-05-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_rename_student_sections_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sections',
            name='trainers',
            field=models.ManyToManyField(blank=True, related_name='trainers', to='base.trainers'),
        ),
    ]
