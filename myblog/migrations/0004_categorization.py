# Generated by Django 2.0.7 on 2018-10-06 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20181005_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Category')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myblog.Post')),
            ],
        ),
    ]
