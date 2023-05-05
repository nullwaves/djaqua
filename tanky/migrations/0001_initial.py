# Generated by Django 4.2.1 on 2023-05-05 18:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inhabitant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('volume', models.IntegerField()),
                ('tank_type', models.CharField(choices=[('FW', 'Freshwater'), ('BW', 'Brackish'), ('SW', 'Saltwater')], default='FW', max_length=2)),
                ('substrate', models.CharField(max_length=255)),
                ('filter_media', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaterTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_tested', models.DateField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ammonia_level', models.DecimalField(decimal_places=4, max_digits=5)),
                ('nitrite_level', models.DecimalField(decimal_places=4, max_digits=5)),
                ('nitrate_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ph_level', models.DecimalField(decimal_places=2, max_digits=5)),
                ('salinity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notes', models.TextField(blank=True, null=True)),
                ('tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tanky.tank')),
            ],
        ),
        migrations.CreateModel(
            name='Spawn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spawn_date', models.DateField()),
                ('hatch_date', models.DateField(blank=True, null=True)),
                ('fry_quantity', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('breeders', models.ManyToManyField(related_name='spawns_produced', to='tanky.inhabitant')),
                ('tank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tanky.tank')),
                ('water_test', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tanky.watertest')),
            ],
        ),
        migrations.AddField(
            model_name='inhabitant',
            name='tank',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tanky.tank'),
        ),
        migrations.CreateModel(
            name='HistoricalTank',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('volume', models.IntegerField()),
                ('tank_type', models.CharField(choices=[('FW', 'Freshwater'), ('BW', 'Brackish'), ('SW', 'Saltwater')], default='FW', max_length=2)),
                ('substrate', models.CharField(max_length=255)),
                ('filter_media', models.CharField(max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical tank',
                'verbose_name_plural': 'historical tanks',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalSpawn',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('spawn_date', models.DateField()),
                ('hatch_date', models.DateField(blank=True, null=True)),
                ('fry_quantity', models.IntegerField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tank', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tanky.tank')),
                ('water_test', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tanky.watertest')),
            ],
            options={
                'verbose_name': 'historical spawn',
                'verbose_name_plural': 'historical spawns',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalInhabitant',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('species', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('tank', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='tanky.tank')),
            ],
            options={
                'verbose_name': 'historical inhabitant',
                'verbose_name_plural': 'historical inhabitants',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
