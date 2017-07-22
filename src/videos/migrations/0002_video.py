from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=160, verbose_name='title')),
                ('url', models.URLField(verbose_name='video URL')),
                ('date_uploaded', models.DateField(verbose_name='uploaded at')),
                ('views', models.PositiveIntegerField(verbose_name='views quantity')),
                ('themes', models.ManyToManyField(related_name='videos', to='videos.Theme', verbose_name='themes')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
                'ordering': ['title'],
            },
        ),
    ]
