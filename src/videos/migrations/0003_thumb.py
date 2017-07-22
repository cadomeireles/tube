from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thumb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_positive', models.BooleanField(verbose_name='is positive')),
                ('time', models.DateTimeField(verbose_name='time')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thumbs_set', related_query_name='thumbs', to='videos.Video', verbose_name='video')),
            ],
            options={
                'verbose_name': 'thumb',
                'verbose_name_plural': 'thumbs',
                'ordering': ['-time'],
            },
        ),
    ]
