import openai
from django.conf import settings
import requests
import openai
import json


class OpenAIService:
    def analizar_perfil_con_chatgpt_facebook(perfil_facebook):
        perfil_texto = perfil_facebook.generar_texto()
        chatgpt_prompt = f"""
        Dado el siguiente perfil de Facebook:
        {perfil_texto}
        
        Tareas:
        1. Evalúa la estabilidad financiera del usuario basada en su red de contactos, grupos a los que pertenece y ubicación.
        2. Predice su nivel socioeconómico en función de su actividad en Facebook.
        3. Genera un puntaje de confianza financiera de 0 a 1000 basado en estos factores.
        4. Proporciona recomendaciones para mejorar su perfil financiero.
        
        Devuelve la respuesta en JSON **válido y bien formateado** sin texto adicional. **No incluyas explicaciones, solo JSON.**
        
        Formato de salida esperado:
        ```json
        {{
            "message": "Evaluacion basada en actividad digital completada exitosamente.",
            "resultado": {{
                "nombre": "Adele Hudson",
                "puntaje_financiero": 730.0,
                "nivel_socioeconomico": "Medio-Alto",
                "indicadores_clave": {{
                    "red_contactos": "Moderada",
                    "movilidad": "Alta",
                    "ubicacion_actual": "Home, Marquardttown",
                    "historial_de_movimiento": ["Place 1", "Place 2", "Place 3"],
                    "actividad_financiera": "Moderada",
                    "transacciones_digitales": 2,
                    "gasto_promedio": 43.15,
                    "uso_de_tarjetas": "Frecuente",
                    "busquedas_financieras": "Bajas",
                    "interes_en_inversiones": "Desconocido",
                    "consumo_de_contenido_financiero": "Desconocido",
                    "estilo_de_vida": "Movilidad alta, compras moderadas",
                    "riesgo_crediticio": "Medio-Bajo"
                }},
                "recomendaciones": "Fortalecer la educacion financiera, explorar opciones de inversion, mejorar la diversificacion de ingresos y optimizar el uso de tarjetas de credito."
            }}
        }}
        ```
        """

                # Instanciar el cliente de OpenAI
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)  # Usa variables de entorno en producción
        
        chat_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Responde solo en JSON válido."},
                      {"role": "user", "content": chatgpt_prompt}],
            temperature=0  # Reducir creatividad para mejorar formato JSON
        )

        # Extraer la respuesta de OpenAI
        resultado_texto = chat_response.choices[0].message.content
        resultado_json = json.loads(resultado_texto)
        print("Respuesta OpenAI:", resultado_texto)  # Depuración

        
        return resultado_json
    
    def analizar_perfil_con_chatgpt_linkedin(perfil_usuario):
        perfil_texto = perfil_usuario.generar_texto()
        chatgpt_prompt = f"""
        Dado el siguiente perfil de Facebook:
        {perfil_texto}
        
        Tareas:
        1. Evalúa la estabilidad financiera del usuario basada en su red de contactos, grupos a los que pertenece y ubicación.
        2. Predice su nivel socioeconómico en función de su actividad en Facebook.
        3. Genera un puntaje de confianza financiera de 0 a 1000 basado en estos factores.
        4. Proporciona recomendaciones para mejorar su perfil financiero.
        
        Devuelve la respuesta en JSON **válido y bien formateado** sin texto adicional. **No incluyas explicaciones, solo JSON.**
        
        Formato de salida esperado:
        ```json
        {{
            "message": "Evaluacion basada en actividad digital completada exitosamente.",
            "resultado": {{
                "nombre": "Adele Hudson",
                "puntaje_financiero": 730.0,
                "nivel_socioeconomico": "Medio-Alto",
                "indicadores_clave": {{
                    "red_contactos": "Moderada",
                    "movilidad": "Alta",
                    "ubicacion_actual": "Home, Marquardttown",
                    "historial_de_movimiento": ["Place 1", "Place 2", "Place 3"],
                    "actividad_financiera": "Moderada",
                    "transacciones_digitales": 2,
                    "gasto_promedio": 43.15,
                    "uso_de_tarjetas": "Frecuente",
                    "busquedas_financieras": "Bajas",
                    "interes_en_inversiones": "Desconocido",
                    "consumo_de_contenido_financiero": "Desconocido",
                    "estilo_de_vida": "Movilidad alta, compras moderadas",
                    "riesgo_crediticio": "Medio-Bajo"
                }},
                "recomendaciones": "Fortalecer la educacion financiera, explorar opciones de inversion, mejorar la diversificacion de ingresos y optimizar el uso de tarjetas de credito."
            }}
        }}
        ```
        """
                # Instanciar el cliente de OpenAI
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)  # Usa variables de entorno en producción
        
        chat_response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "Responde solo en JSON válido."},
                      {"role": "user", "content": chatgpt_prompt}],
            temperature=0  # Reducir creatividad para mejorar formato JSON
        )

        # Extraer la respuesta de OpenAI
        resultado_texto = chat_response.choices[0].message.content
        resultado_json = json.loads(resultado_texto)
        print("Respuesta OpenAI:", resultado_texto)  # Depuración

        
        return resultado_json
