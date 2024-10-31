# Se crea una interfaz de login 🆗
#-----------------------------------------------------
import flet as ft

def main (page: ft.Page):
    page.padding = 0
    page.bgcolor = ft.colors.PINK_100
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    encabezado = ft.TextField ("Este es mi LOGIN ", width=300, text_align= "center")

    page.add (encabezado)




#visualizo ventana gráfica
ft.app (target= main)