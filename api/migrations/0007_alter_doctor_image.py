# Generated by Django 5.0.6 on 2024-08-14 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, default='doctor/default.jpeg', upload_to='doctor'),
        ),
    ]
