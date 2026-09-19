from django.db import models


class TareaAcademica(models.Model):
    NIVELES_DIFICULTAD = [
        ("baja", "Baja"),
        ("media", "Media"),
        ("alta", "Alta"),
    ]

    materia = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_entrega = models.DateField()
    dificultad = models.CharField(
        max_length=10,
        choices=NIVELES_DIFICULTAD,
    )
    prioridad = models.CharField(max_length=30)
    recomendacion = models.TextField()
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.materia}: {self.descripcion}"