# Generated by Django 3.0.7 on 2020-06-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0018_delete_jobdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobtype', name='name', field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='referencedatasignatures',
            name='job_type_name',
            field=models.CharField(db_index=True, max_length=140),
        ),
    ]
