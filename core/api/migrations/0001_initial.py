# Generated by Django 4.0.1 on 2022-01-18 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raffle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=257)),
                ('max_number', models.BigIntegerField()),
                ('raffle_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField()),
                ('is_active', models.BooleanField(default=False)),
                ('raffle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raffle_ticket', to='api.raffle')),
            ],
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize_name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('prize_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('raffle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='raffle_prize', to='api.raffle')),
            ],
        ),
    ]
