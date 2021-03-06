# Generated by Django 2.2.1 on 2020-08-15 06:57

from django.db import migrations, models
import utils.upload
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=utils.upload.article_pic_path, validators=[utils.validators.validate_file_size]),
        ),
    ]
