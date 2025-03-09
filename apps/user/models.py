from django.db import models
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

class PerfilFacebook:
    def __init__(self, nombre, ubicacion, edad, email, genero, ciudad_origen, intereses, publicaciones, fotos, educacion):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.edad = edad
        self.email = email
        self.genero = genero
        self.ciudad_origen = ciudad_origen
        self.intereses = intereses  # Lista de intereses
        self.publicaciones = publicaciones  # Lista de publicaciones recientes
        self.fotos = fotos  # Lista de fotos publicadas
        self.educacion = educacion  # Nivel educativo

    def generar_texto(self):
        return f"""
        Nombre: {self.nombre}
        Ubicación: {self.ubicacion}
        Edad: {self.edad}
        Email: {self.email}
        Género: {self.genero}
        Ciudad de Origen: {self.ciudad_origen}
        Intereses: {', '.join(self.intereses)}
        Publicaciones recientes: {', '.join(self.publicaciones)}
        Fotos subidas: {len(self.fotos)}
        Nivel de educación: {', '.join(self.educacion)}
        """

class PerfilLinkedIn():
    def __init__(self, nombre, ubicacion, experiencia, trabajos_previos, estado_actual, cargo_actual, nivel_educacion, habilidades, idiomas, salario_estimado, perfil_crediticio):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.experiencia = experiencia  # Lista de experiencias profesionales
        self.trabajos_previos = trabajos_previos  # Cantidad de trabajos previos
        self.estado_actual = estado_actual  # Estado laboral actual
        self.cargo_actual = cargo_actual  # Cargo en la empresa actual
        self.nivel_educacion = nivel_educacion  # Nivel educativo alcanzado
        self.habilidades = habilidades  # Lista de habilidades
        self.idiomas = idiomas  # Lista de idiomas y nivel
        self.salario_estimado = salario_estimado  # Salario estimado por país
        self.perfil_crediticio = perfil_crediticio  # Estimación del perfil crediticio

    def generar_texto(self):
        return f"""
        nombre:{self.nombre}
        Experiencia profesional: {len(self.experiencia)} años
        Trabajos previos: {self.trabajos_previos}
        Estado actual: {self.estado_actual}
        Cargo actual: {self.cargo_actual}
        Nivel de educación: {self.nivel_educacion}
        Habilidades: {', '.join(self.habilidades)}
        Idiomas: {', '.join([f"{idioma['idioma']} ({idioma['nivel']})" for idioma in self.idiomas])}
        Salario estimado: {self.salario_estimado}
        Perfil crediticio: {self.perfil_crediticio}
        """