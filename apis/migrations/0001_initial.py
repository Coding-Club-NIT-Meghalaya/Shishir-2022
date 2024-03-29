# Generated by Django 4.0.3 on 2022-03-16 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('type', models.CharField(choices=[('Main', 'Main'), ('Departmental CSE', 'Departmental CSE'), ('Departmental ECE', 'Departmental ECE'), ('Departmental EE', 'Departmental EE'), ('Departmental ME', 'Departmental ME'), ('Departmental CE', 'Departmental CE'), ('Gaming', 'Gaming'), ('Other', 'Other')], default='Coding', max_length=200)),
                ('duration', models.CharField(max_length=100)),
                ('total_prize', models.CharField(max_length=100)),
                ('registration_link', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('image', models.CharField(max_length=200)),
                ('live_link', models.CharField(max_length=100)),
                ('doc_link', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=30)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('festival_name', models.CharField(max_length=50)),
                ('year', models.IntegerField(primary_key=True, serialize=False)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Head', 'Head'), ('Coordinator', 'Coordinator'), ('Co-Coordinator', 'Co-Coordinator'), ('General Secretary', 'General Secretary'), ('Publicity and Core Team Head', 'Publicity and Core Team Head'), ('Publicity and Core Team Coordinator', 'Publicity and Core Team Coordinator'), ('Publicity and Core Team Co-Coordinator', 'Publicity and Core Team Co-Coordinator'), ('Designing Team Head', 'Designing Team Head'), ('Designing Team Coordinator', 'Designing Team Coordinator'), ('Designing Team Co-Coordinator', 'Designing Team Co-Coordinator'), ('Sponsor and Marketing Team Head', 'Sponsor and Marketing Team Head'), ('Sponsor and Marketing Team Coordinator', 'Sponsor and Marketing Team Coordinator'), ('Sponsor and Marketing Team Co-Coordinator', 'Sponsor and Marketing Team Co-Coordinator'), ('Web Development Team Head', 'Web Development Team Head'), ('Web Development Team Co-Coordinator', 'Web Development Team Co-Coordinator'), ('App Development Team Head', 'App Development Team Head'), ('App Development Team Coordinator', 'App Development Team Coordinator'), ('App Development Team Co-Coordinator', 'Web Development Team Co-Coordinator')], default='Coordinator', max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=50)),
                ('event_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team_members', to='apis.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='event_year', to='apis.year'),
        ),
    ]
