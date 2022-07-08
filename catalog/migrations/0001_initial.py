# Generated by Django 4.0.2 on 2022-03-01 18:38

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(blank=True, max_length=64, null=True)),
                ('Pseudonymous', models.CharField(blank=True, max_length=64, null=True)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, null=True)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('mother_tongue', models.CharField(blank=True, choices=[('EN', 'English'), ('FR', 'French'), ('ES', 'Spanish'), ('PT', 'Portuguese'), ('DE', 'German'), ('EL', 'Greek'), ('RU', 'Russian'), ('ZH', 'Chinese')], max_length=2, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('summary', models.TextField(blank=True, null=True)),
                ('isbn', models.CharField(max_length=16, unique=True, verbose_name='ISBN')),
                ('publish_year', models.DateField(blank=True, null=True)),
                ('original_language', models.CharField(choices=[('EN', 'English'), ('FR', 'French'), ('ES', 'Spanish'), ('PT', 'Portuguese'), ('DE', 'German'), ('EL', 'Greek'), ('RU', 'Russian'), ('ZH', 'Chinese')], max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('books', models.ManyToManyField(to='catalog.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('country', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipBookGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.genre')),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipBookAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.author')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('status', models.CharField(choices=[('Available', 'Ava'), ('Borrowed', 'Bor'), ('Reserved', 'Res'), ('LOST', 'Los')], default='Available', max_length=10)),
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole librarium', primary_key=True, serialize=False)),
                ('num_borrowed', models.PositiveIntegerField(blank=True, null=True)),
                ('loan_date', models.DateField()),
                ('return_date', models.DateField(blank=True, null=True)),
                ('prologue', models.TextField(blank=True, null=True)),
                ('edition_year', models.DateField()),
                ('edition_num', models.PositiveIntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='catalog.book')),
                ('prologue_author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.author')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.publisher')),
            ],
            options={
                'ordering': ['return_date'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(through='catalog.RelationshipBookAuthor', to='catalog.Author'),
        ),
        migrations.AddField(
            model_name='book',
            name='genres',
            field=models.ManyToManyField(through='catalog.RelationshipBookGenre', to='catalog.Genre'),
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(through='catalog.RelationshipBookAuthor', to='catalog.Book'),
        ),
    ]
