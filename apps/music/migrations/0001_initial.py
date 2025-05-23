# Generated by Django 5.2.1 on 2025-05-24 05:10

import apps.music.utils.uploads
import core.models
import core.utils.utils
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, verbose_name='Título Slug')),
                ('initial', models.CharField(blank=True, editable=False, max_length=1, verbose_name='Inicial')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Fecha Lanzamiento')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Álbum',
                'verbose_name_plural': 'Álbumes',
                'ordering': ['artist', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=150, verbose_name='Nombre Slug')),
                ('initial', models.CharField(blank=True, editable=False, max_length=1, verbose_name='Inicial')),
                ('biography', models.TextField(blank=True, verbose_name='Biografía')),
                ('start_year', core.models.YearField(blank=True, null=True, validators=[core.utils.utils.validate_year], verbose_name='Año inicio')),
                ('year_end', core.models.YearField(blank=True, null=True, validators=[core.utils.utils.validate_year], verbose_name='Año término')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
                'ordering': ['-created_at', 'initial', 'name'],
            },
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.music.utils.uploads.album_image_path, verbose_name='Imagen Álbum')),
                ('image_url', models.URLField(blank=True, max_length=2000, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('album', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='albums_as_images', to='music.album', verbose_name='Álbum')),
                ('size_image', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='albums_images_as_sizes', to='common.imagesize', verbose_name='Tamaño')),
            ],
            options={
                'verbose_name': 'Imagen Álbum',
                'verbose_name_plural': 'Imágenes Álbumes',
                'ordering': ['album', 'size_image'],
            },
        ),
        migrations.CreateModel(
            name='AlbumImageExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.music.utils.uploads.album_image_extra_path, verbose_name='Imagen Extra Álbum')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('album', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='albums_as_images_extra', to='music.album', verbose_name='Álbum')),
            ],
            options={
                'verbose_name': 'Imagen Extra Álbum',
                'verbose_name_plural': 'Imágenes Extra Álbumes',
                'ordering': ['album'],
            },
        ),
        migrations.CreateModel(
            name='AlbumType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('name_esp', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Nombre Español')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True, verbose_name='Nombre Slug')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Tipo Álbum',
                'verbose_name_plural': 'Tipos Álbumes',
                'ordering': ['-created_at', 'name'],
                'unique_together': {('name', 'name_esp')},
            },
        ),
        migrations.AddField(
            model_name='album',
            name='album_type',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='albums_as_types', to='music.albumtype', verbose_name='Tipo'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='albums_as_artists', to='music.artist', verbose_name='Artista'),
        ),
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.music.utils.uploads.artist_image_path, verbose_name='Imagen Artista')),
                ('image_url', models.URLField(blank=True, max_length=2000, null=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('artist', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='artists_as_images', to='music.artist', verbose_name='Artista')),
                ('size_image', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='artists_images_as_sizes', to='common.imagesize', verbose_name='Tamaño')),
            ],
            options={
                'verbose_name': 'Imagen Artista',
                'verbose_name_plural': 'Imágenes Artistas',
                'ordering': ['artist', 'size_image'],
            },
        ),
        migrations.CreateModel(
            name='ArtistImageExtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=apps.music.utils.uploads.artist_image_extra_path, verbose_name='Imagen Extra Artista')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('artist', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='artists_as_images_extra', to='music.artist', verbose_name='Artista')),
            ],
            options={
                'verbose_name': 'Imagen Extra Artista',
                'verbose_name_plural': 'Imágenes Extra Artista',
                'ordering': ['artist'],
            },
        ),
        migrations.CreateModel(
            name='ArtistType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('name_esp', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Nombre Español')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True, verbose_name='Nombre Slug')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Tipo Artista',
                'verbose_name_plural': 'Tipos Artistas',
                'ordering': ['-created_at', 'name'],
                'unique_together': {('name', 'name_esp')},
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='artist_type',
            field=models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='artits_as_types', to='music.artisttype', verbose_name='Tipo Artista'),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='Nombre')),
                ('name_esp', models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='Nombre Español')),
                ('initial', models.CharField(blank=True, editable=False, max_length=1, verbose_name='Inicial')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=40, unique=True, verbose_name='Nombre Slug')),
                ('description', models.TextField(blank=True, verbose_name='Descripción')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('parent', models.ForeignKey(blank=True, limit_choices_to={'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='music.genre', verbose_name='Padre')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
                'ordering': ['-created_at', 'name'],
                'unique_together': {('name', 'name_esp')},
            },
        ),
        migrations.AddField(
            model_name='artist',
            name='genre',
            field=models.ManyToManyField(blank=True, limit_choices_to={'is_active': True}, related_name='artists_as_genres', to='music.genre', verbose_name='Géneros'),
        ),
        migrations.CreateModel(
            name='MusicLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='fecha Añadido')),
                ('process', models.TextField(default='', verbose_name='Proceso')),
                ('level', models.CharField(default='INFO', max_length=10, verbose_name='Nivel')),
                ('message', models.TextField(verbose_name='Mensaje')),
            ],
            options={
                'verbose_name': 'Log Música',
                'verbose_name_plural': 'Logs Música',
                'db_table': 'log_Music',
                'ordering': ['-timestamp'],
                'unique_together': {('level', 'process', 'timestamp')},
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Nombre')),
                ('name_esp', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='Nombre Español')),
                ('initial', models.CharField(blank=True, editable=False, max_length=1, verbose_name='Inicial')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=30, unique=True, verbose_name='Nombre Slug')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name': 'Rol',
                'verbose_name_plural': 'Roles',
                'ordering': ['-created_at', 'name'],
                'unique_together': {('name', 'name_esp')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='album',
            unique_together={('artist', 'album_type', 'title')},
        ),
        migrations.AlterUniqueTogether(
            name='artist',
            unique_together={('initial', 'name')},
        ),
        migrations.CreateModel(
            name='ArtistMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('join_date', models.DateField(blank=True, null=True, verbose_name='Fecha Ingreso')),
                ('leave_date', models.DateField(blank=True, null=True, verbose_name='Fecha Salida')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('artist', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='artist_memberships', to='music.artist', verbose_name='Artista')),
                ('person', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='persons_role_memberships', to='common.person', verbose_name='Persona')),
                ('role', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.CASCADE, related_name='roles_persons_memberships', to='music.role', verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Miembro de Artista',
                'verbose_name_plural': 'Miembros de Artistas',
                'ordering': ['artist', 'person', 'role'],
                'unique_together': {('artist', 'person', 'role')},
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, verbose_name='Título Slug')),
                ('initial', models.CharField(blank=True, editable=False, max_length=1, verbose_name='Inicial')),
                ('lyrics', models.TextField(blank=True, verbose_name='Letra')),
                ('album_song_id', models.PositiveIntegerField(blank=True, default=0, verbose_name='ID Canción Álbum')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Fecha Lanzamiento')),
                ('audio_file', models.FileField(blank=True, null=True, upload_to=apps.music.utils.uploads.song_path, verbose_name='Archivo Audio')),
                ('is_active', models.BooleanField(default=True, verbose_name='Activo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('album', models.ForeignKey(limit_choices_to={'is_active': True}, on_delete=django.db.models.deletion.PROTECT, related_name='songs_as_albums', to='music.album', verbose_name='Álbum')),
            ],
            options={
                'verbose_name': 'Canción',
                'verbose_name_plural': 'Canciones',
                'ordering': ['album_song_id', 'album'],
                'unique_together': {('album_song_id', 'title', 'album')},
            },
        ),
    ]
