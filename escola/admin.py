from django.contrib import admin
from escola.models import Aluno, Curso, Matricula
# Register your models here.


@admin.register(Aluno)
class Alunos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('id', 'nome')
    serach_fields = ('nome',)
    list_per_page = 20


@admin.register(Curso)
class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    serach_fields = ('codigo_curso',)


@admin.register(Matricula)
class Matriculas(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)
