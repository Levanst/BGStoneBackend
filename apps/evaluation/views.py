from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from apps.utils.openai_service import OpenAIService
from apps.user.models import PerfilLinkedIn, PerfilFacebook
# from core.models import User

# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny, ])
def SocialMediaServiceEvaluation(request):
    try:
        data = request.data.get('value', None)

        perfil_usuario = PerfilFacebook(
            nombre="Giancarlo Carvajal Flor",
            ubicacion="Guayaquil, Ecuador",
            edad="20",
            email="nitroso1814@gmail.com",
            genero="Masculino",
            ciudad_origen="Guayaquil, Ecuador",
            intereses=["Deportes", "Música", "Tecnología"],
            publicaciones=[
                "Portal Rights Manager.",
                "Quieroooo Mayito AZ",
                "Lo admito, yo soy quien manda en la relación 😞"
            ],
            fotos=["Foto de perfil", "Foto de perfil", "Foto de perfil"],
            educacion=["Bachillerato en Liceo Corbi"]
        )
        print(perfil_usuario)
        result_analys = OpenAIService.analizar_perfil_con_chatgpt_facebook(perfil_usuario)

        return Response(result_analys, status=status.HTTP_200_OK)
        
    except Exception as e:
        res = {'msg': 'Something went wrong', 'error': str(e)}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)


# Create your views here.
@api_view(['POST'])
@permission_classes([AllowAny, ])
def ProfessionalProfileServiceEvaluation(request):
    try:
        data = request.data.get('value', None)

        # Crear una instancia de PerfilLinkedIn con datos de ejemplo
        perfil_linkedin = PerfilLinkedIn(
            nombre="Carlos Mendoza",
            ubicacion="Ciudad de México, México",
            experiencia=[
                {
                    "empresa": "Microsoft",
                    "cargo": "Ingeniero de Software",
                    "fecha_inicio": "Enero 2021",
                    "fecha_fin": "Presente",
                    "tecnologias": ["Python", "Django", "Azure", "Inteligencia Artificial"],
                    "nivel_seniority": "Senior"
                },
                {
                    "empresa": "IBM",
                    "cargo": "Desarrollador Backend",
                    "fecha_inicio": "Junio 2018",
                    "fecha_fin": "Diciembre 2020",
                    "tecnologias": ["Java", "Spring Boot", "AWS"],
                    "nivel_seniority": "Intermedio"
                }
            ],
            trabajos_previos=2,
            estado_actual="Empleado",
            cargo_actual="Ingeniero de Software",
            nivel_educacion="Maestría en Ciencias de la Computación",
            habilidades=["Python", "Django", "Machine Learning", "Desarrollo Backend", "Cloud Computing"],
            idiomas=[
                {"idioma": "Español", "nivel": "Nativo"},
                {"idioma": "Inglés", "nivel": "Avanzado"},
                {"idioma": "Francés", "nivel": "Intermedio"}
            ],
            salario_estimado={
                "EE.UU": {"rango": "120,000 - 150,000 USD", "fuente": "Glassdoor"},
                "México": {"rango": "900,000 - 1,200,000 MXN", "fuente": "Indeed"},
                "España": {"rango": "50,000 - 70,000 EUR", "fuente": "LinkedIn Salary"}
            },
            perfil_crediticio={
                "factores": {
                    "estabilidad_laboral": "Alta",
                    "nivel_ingresos": "Alto",
                    "historial_crediticio": "Excelente",
                    "endeudamiento": "Bajo"
                },
                "categoria_probable": "Muy Bueno"
            }
        )


        result_analys = OpenAIService.analizar_perfil_con_chatgpt_linkedin(perfil_linkedin)

        return Response(result_analys, status=status.HTTP_200_OK)
        
    except Exception as e:
        res = {'msg': 'Something went wrong', 'error': str(e)}
        return Response(res, status=status.HTTP_400_BAD_REQUEST)
