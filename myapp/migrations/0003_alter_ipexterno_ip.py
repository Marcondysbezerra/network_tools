# Generated by Django 3.2.8 on 2021-12-06 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_ipexterno_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipexterno',
            name='ip',
            field=models.CharField(max_length=255),
        ),
    ]