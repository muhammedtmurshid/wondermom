# Generated by Django 4.0.3 on 2022-03-25 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_brands_vote_vote_brands_remove_vote_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='vote_brands',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.votebrand'),
        ),
    ]