# Generated by Django 4.2.1 on 2024-03-17 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_author_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.author'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auhtor_name', models.CharField(max_length=63)),
                ('content', models.TextField()),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]