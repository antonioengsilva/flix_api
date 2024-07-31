# Generated by Django 5.0.7 on 2024-07-24 19:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0, 'Avaliação não pode ser inferior a 0 estrelas.'), django.core.validators.MaxValueValidator(5, 'Avaliação não pode ser superior a 5 estrelas.')]),
        ),
    ]
