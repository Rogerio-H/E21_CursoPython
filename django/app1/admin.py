from django.contrib import admin

# Register your models here.

from .models import Pessoas
from .models import Alunos
from .models import Turmas


admin.site.register(Pessoas)
admin.site.register(Alunos)
admin.site.register(Turmas)