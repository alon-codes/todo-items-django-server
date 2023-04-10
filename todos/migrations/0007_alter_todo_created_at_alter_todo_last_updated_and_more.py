# Generated by Django 4.2 on 2023-04-09 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0006_alter_todo_id_alter_todo_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="todo",
            name="order",
            field=models.IntegerField(editable=False),
        ),
    ]