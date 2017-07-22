from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='time'),
        ),
        migrations.AlterField(
            model_name='thumb',
            name='time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='time'),
        ),
    ]
