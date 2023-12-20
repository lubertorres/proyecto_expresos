from django.contrib import admin

from .models import estado
from .models import unidadT
from .models import conductorT
from .models import carreraT
from .models import cursoT
from .models import viajeT

# Register your models here.



admin.site.register(estado)
admin.site.register(unidadT)
admin.site.register(conductorT)
admin.site.register(carreraT)
admin.site.register(cursoT)
admin.site.register(viajeT)


