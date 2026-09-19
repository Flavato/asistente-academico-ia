from datetime import date, datetime

from django.shortcuts import render

from .models import TareaAcademica

from .servicios_clima import consultar_clima


def inicio(request):
    contexto = {
        "titulo": "Asistente Académico IA",
        "descripcion": (
            "Ingresá una actividad académica y recibí "
            "una recomendación para organizarte."
        ),
    }

    if request.method == "POST":
        materia = request.POST.get("materia", "").strip()
        tarea = request.POST.get("tarea", "").strip()
        fecha_entrega = request.POST.get("fecha_entrega", "")
        dificultad = request.POST.get("dificultad", "")

        contexto["materia"] = materia
        contexto["tarea"] = tarea
        contexto["fecha_entrega"] = fecha_entrega
        contexto["dificultad"] = dificultad

        if materia and tarea and fecha_entrega and dificultad:
            fecha_seleccionada = datetime.strptime(
                fecha_entrega,
                "%Y-%m-%d"
            ).date()

            dias_restantes = (fecha_seleccionada - date.today()).days

            if dias_restantes < 0:
                recomendacion = (
                    "La fecha de entrega ya pasó. "
                    "Consultá con el docente si todavía podés "
                    "presentar la actividad."
                )
                prioridad = "Fecha vencida"

            elif dias_restantes == 0:
                recomendacion = (
                    "La entrega es hoy. Concentrate primero en "
                    "los puntos obligatorios y revisá el trabajo "
                    "antes de enviarlo."
                )
                prioridad = "Urgente"

            elif dias_restantes <= 2:
                recomendacion = (
                    "Queda muy poco tiempo. Dividí la tarea en "
                    "partes pequeñas y comenzá hoy con la sección "
                    "más importante."
                )
                prioridad = "Alta"

            elif dificultad == "alta":
                recomendacion = (
                    "La actividad tiene dificultad alta. Aunque "
                    "todavía hay tiempo, conviene comenzar ahora, "
                    "buscar el material necesario y consultar "
                    "las dudas con anticipación."
                )
                prioridad = "Alta"

            elif dias_restantes <= 7:
                recomendacion = (
                    "Tenés varios días disponibles. Organizá la "
                    "actividad en etapas: investigación, desarrollo, "
                    "revisión y entrega."
                )
                prioridad = "Media"

            else:
                recomendacion = (
                    "La fecha todavía está alejada. Podés planificar "
                    "sesiones cortas de trabajo y revisar el avance "
                    "cada semana."
                )
                prioridad = "Normal"

            TareaAcademica.objects.create(
                materia=materia,
                descripcion=tarea,
                fecha_entrega=fecha_seleccionada,
                dificultad=dificultad,
                prioridad=prioridad,
                recomendacion=recomendacion,
            )

            contexto["resultado"] = {
                "materia": materia,
                "tarea": tarea,
                "dias_restantes": dias_restantes,
                "prioridad": prioridad,
                "recomendacion": recomendacion,
            }

            contexto["guardado"] = (
                "La actividad se guardó correctamente en SQLite."
            )

        else:
            contexto["error"] = (
                "Completá todos los campos antes de solicitar "
                "la recomendación."
            )

    contexto["historial"] = TareaAcademica.objects.order_by(
        "-creada_en"
    )[:10]

    contexto["clima"] = consultar_clima()

    return render(request, "asistente/inicio.html", contexto)