# Generated by Django 3.2.8 on 2023-06-13 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_portfolio_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
