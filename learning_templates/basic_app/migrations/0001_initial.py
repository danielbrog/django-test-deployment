# Generated by Django 2.2.1 on 2019-08-28 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('gamepk', models.PositiveIntegerField()),
                ('hometeamid', models.PositiveSmallIntegerField()),
                ('hometeamname', models.CharField(max_length=256)),
                ('awayteamid', models.PositiveSmallIntegerField()),
                ('awayteamname', models.CharField(max_length=256)),
                ('parkid', models.PositiveSmallIntegerField()),
                ('park', models.CharField(max_length=256)),
                ('batterid', models.PositiveIntegerField()),
                ('battername', models.CharField(max_length=256)),
                ('batside', models.CharField(max_length=1)),
                ('batterteamid', models.PositiveIntegerField()),
                ('pitcherid', models.PositiveIntegerField()),
                ('pitchername', models.CharField(max_length=256)),
                ('pitcherteamid', models.PositiveIntegerField()),
                ('pitchside', models.CharField(max_length=1)),
                ('balls', models.PositiveSmallIntegerField()),
                ('strikes', models.PositiveSmallIntegerField()),
                ('result_type', models.CharField(max_length=256)),
                ('pitch_type', models.CharField(max_length=2)),
                ('pitch_speed', models.FloatField()),
                ('zone_location_x', models.FloatField()),
                ('zone_location_z', models.FloatField()),
                ('launch_speed', models.FloatField()),
                ('launch_vert_ang', models.FloatField()),
                ('launch_horiz_ang', models.FloatField()),
                ('landing_location_x', models.FloatField()),
                ('landing_location_y', models.FloatField()),
                ('hang_time', models.FloatField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
