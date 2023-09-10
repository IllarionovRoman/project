# Generated by Django 4.1.7 on 2023-05-30 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_event_students_event_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.PositiveIntegerField()),
                ('date', models.DateTimeField()),
                ('sections', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.sections')),
            ],
        ),
    ]
