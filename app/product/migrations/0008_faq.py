# Generated by Django 5.0.2 on 2024-02-07 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_whychooseus_whychooseuspunkt'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Sual',
                'verbose_name_plural': 'Suallar',
            },
        ),
    ]