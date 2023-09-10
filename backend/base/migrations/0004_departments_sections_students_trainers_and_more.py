# Generated by Django 4.1.4 on 2023-01-22 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sections',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.departments')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section', to='base.sections')),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=200, null=True)),
                ('age', models.IntegerField(blank=True, default=0, null=True)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.departments')),
                ('sections', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sections', to='base.sections')),
                ('students', models.ManyToManyField(blank=True, related_name='students', to='base.students')),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to='base.trainers'),
        ),
        migrations.AddField(
            model_name='sections',
            name='student',
            field=models.ManyToManyField(blank=True, related_name='student', to='base.students'),
        ),
        migrations.AddField(
            model_name='sections',
            name='trainers',
            field=models.ManyToManyField(blank=True, related_name='trainers', to='base.students'),
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('count', models.IntegerField(blank=True, default=0, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('type', models.CharField(choices=[('gold', 'gold'), ('silver', 'silver'), ('bronze', 'bronze')], max_length=255)),
                ('_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('students', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.students')),
            ],
        ),
    ]