# Generated by Django 4.0.4 on 2022-05-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_turno', models.CharField(max_length=100)),
            ],
        ),
    ]
