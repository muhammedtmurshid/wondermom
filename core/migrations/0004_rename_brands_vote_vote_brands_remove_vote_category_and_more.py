# Generated by Django 4.0.3 on 2022-03-25 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_about_contact_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='brands',
            new_name='vote_brands',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='category',
        ),
        migrations.AddField(
            model_name='vote',
            name='brand',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='core.registrationbrandcategory'),
            preserve_default=False,
        ),
    ]
