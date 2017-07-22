from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_thumb'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_positive', models.BooleanField(verbose_name='is positive')),
                ('time', models.DateTimeField(verbose_name='time')),
                ('message', models.TextField(blank=True, null=True, verbose_name='message')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_set', related_query_name='comments', to='videos.Video', verbose_name='video')),
            ],
            options={
                'verbose_name': 'comment',
                'verbose_name_plural': 'comments',
                'ordering': ['-time'],
            },
        ),
    ]
