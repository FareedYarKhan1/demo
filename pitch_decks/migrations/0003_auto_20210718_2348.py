# Generated by Django 3.2.5 on 2021-07-18 23:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pitch_decks', '0002_rename_title1_deckimage_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckimage',
            name='pitch_deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deck_images', to='pitch_decks.pitchdeck'),
        ),
        migrations.AlterField(
            model_name='deckimage',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='pitchdeck',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]
