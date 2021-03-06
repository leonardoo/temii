# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-13 16:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CharlaModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('prerequisitos', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('posible', 'Temas Posibles'), ('agendado', 'Temas agendados'), ('finalizado', 'Temas finalizados')], default='posible', max_length=255)),
                ('fecha_taller', models.DateField(blank=True, null=True)),
                ('votos', models.PositiveIntegerField(default=0)),
                ('talleriast_no_usuario', models.TextField(blank=True, null=True)),
                ('categorias', models.ManyToManyField(to='charlas.CategoriaModel')),
                ('tallerista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tallerista', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='propone_charla', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['votos'],
            },
        ),
        migrations.CreateModel(
            name='UsuarioVotoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('charla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charlas.CharlaModel')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='usuariovotomodel',
            unique_together=set([('usuario', 'charla')]),
        ),
    ]
