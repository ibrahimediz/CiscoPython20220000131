# Generated by Django 4.0.4 on 2022-04-11 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('icerik', models.TextField()),
                ('kayitzamani', models.DateTimeField(default=django.utils.timezone.now)),
                ('yayimzamani', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
