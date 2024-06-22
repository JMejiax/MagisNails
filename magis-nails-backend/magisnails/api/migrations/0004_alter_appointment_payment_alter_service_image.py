# Generated by Django 5.0.6 on 2024-06-12 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_appointment_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='payment',
            field=models.FileField(default='null', upload_to='appointment_payments/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='', upload_to='service_images/'),
            preserve_default=False,
        ),
    ]
