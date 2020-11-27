# Generated by Django 3.1.3 on 2020-11-26 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0003_auto_20201125_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='PicWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('work', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.work')),
            ],
        ),
    ]