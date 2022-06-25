# Generated by Django 3.2.5 on 2021-07-05 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PitchDeck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('presentation_file', models.FileField(upload_to='decks/')),
            ],
        ),
        migrations.CreateModel(
            name='DeckImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.TextField()),
                ('slide', models.ImageField(upload_to='images/')),
                ('pitch_deck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pitch_decks.pitchdeck')),
            ],
        ),
    ]
