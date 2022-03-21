# Generated by Django 4.0.3 on 2022-03-21 17:10

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='rules',
            field=froala_editor.fields.FroalaField(default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='total_prize',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.CharField(choices=[('Main', 'Main'), ('Departmental', 'Departmental'), ('Gaming', 'Gaming'), ('Other', 'Other')], default='Coding', max_length=200),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='type',
            field=models.CharField(choices=[('Head', 'Head'), ('Coordinator', 'Coordinator'), ('Co-Coordinator', 'Co-Coordinator'), ('General Secretary', 'General Secretary'), ('Publicity and Core Team Head', 'Publicity and Core Team Head'), ('Publicity and Core Team Coordinator', 'Publicity and Core Team Coordinator'), ('Publicity and Core Team Co-Coordinator', 'Publicity and Core Team Co-Coordinator'), ('Designing Team Head', 'Designing Team Head'), ('Designing Team Coordinator', 'Designing Team Coordinator'), ('Designing Team Co-Coordinator', 'Designing Team Co-Coordinator'), ('Sponsor and Marketing Team Head', 'Sponsor and Marketing Team Head'), ('Sponsor and Marketing Team Coordinator', 'Sponsor and Marketing Team Coordinator'), ('Sponsor and Marketing Team Co-Coordinator', 'Sponsor and Marketing Team Co-Coordinator'), ('Web Development Team Head', 'Web Development Team Head'), ('Web Development Team Coordinator', 'Web Development Team Coordinator'), ('Web Development Team Co-Coordinator', 'Web Development Team Co-Coordinator'), ('App Development Team Head', 'App Development Team Head'), ('App Development Team Coordinator', 'App Development Team Coordinator'), ('App Development Team Co-Coordinator', 'App Development Team Co-Coordinator')], default='Coordinator', max_length=100),
        ),
    ]
