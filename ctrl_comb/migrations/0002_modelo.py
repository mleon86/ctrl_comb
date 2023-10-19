# Generated by Django 4.2.1 on 2023-10-19 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ctrl_comb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descript', models.CharField(db_comment='Descripcion del Modelo de Vehículo', max_length=50)),
                ('mark', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ctrl_comb.mark')),
            ],
            options={
                'verbose_name': 'Modelo',
                'verbose_name_plural': 'Modelos de Vehiculos',
            },
        ),
    ]
