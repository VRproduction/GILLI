# Generated by Django 5.0.2 on 2024-02-07 13:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_generalsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalsettings',
            name='footer_slogan_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=200, null=True)),
                ('is_main', models.BooleanField(default=False)),
                ('setting', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='numbers', to='product.generalsettings')),
            ],
            options={
                'verbose_name': 'Nömrə',
                'verbose_name_plural': 'Nömrələr',
            },
        ),
    ]
