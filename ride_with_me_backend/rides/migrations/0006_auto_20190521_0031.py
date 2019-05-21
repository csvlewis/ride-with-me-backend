# Generated by Django 2.2.1 on 2019-05-21 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0005_auto_20190521_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.TextField(blank=True, null=True)),
                ('state', models.TextField(blank=True, null=True)),
                ('lat', models.TextField(blank=True, null=True)),
                ('long', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rides_city',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='ride',
            name='end_city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='end_city', to='rides.City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='start_city',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='start_city', to='rides.City'),
            preserve_default=False,
        ),
    ]
