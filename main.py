# --> trabajo en un entorno virtual
# --> tema: una app de notas que permite:
#  insertar titulo, insertar texto en el cuerpo y borrar la nota
# septiembre: 2024
# 💜 Realizado por Deborah Ajalla 💜

#---------------------------------------------------------------------
import flet as ft  # --> se descargó flet en la consola para empezar a trabajar

#---------------------------------------------------------------------
# ---- FUNCIÓN PRINCIPAL ----
def main (page: ft.Page):      # -> el parámetro es la página que sirve d ventana
    page.title = "MIS NOTAS"   # -> título de la ventana
    page.padding = 30          # -> separación de los márgenes en x e y
    #page.theme_mode = ft.ThemeMode.DARK # -> pongo en modo oscuro
    page.bgcolor = ft.colors.PINK  # -> ❌verificar porqué no funciona el color que elijo ❌
    # note = ft.TextField (value = "Mi Primer Nota", multiline = True )  # --> inserta la nota en la ventana
    # page.add(note)

# ---- FUNCIÓN CREA NOTA en contenedor ----
    # def create_note (text):
    #     return ft.Container (  # --> creo contenedor para fijar formato de los elementos 
    #         content = ft.TextField (value = text, multiline = True),
    #         width = 200,
    #         height = 200,
    #         bgcolor = ft.colors.YELLOW_100,
    #         border_radius = 8,
    #         padding = 10,  # --> separa el interior del cuadro de la nota 
    #         margin = 15    # --> separa entre notas
    #    )

    # ---- FUNCIÓN AÑADE NOTA ----
    def add_note (e):
        new_note = create_note ("Nueva Nota")
        grid.controls.append(new_note)
        page.update()

    # ---- FUNCIÓN BORRA NOTA ----
    def delete_note (note):
        grid.controls.remove (note)
        page.update()

    # ---- FUNCIÓN CREA NOTA en grid ----
    def create_note (text):
        note_contenido = ft.TextField (value = text, multiline = True, bgcolor = ft.colors.YELLOW_100)    

        note = ft.Container (
            content = ft.Column ([note_contenido, ft.IconButton (icon = ft.icons.DELETE,
                                                                 on_click = lambda _: delete_note (note))]),
                     width = 200,
                     height = 200,
                     bgcolor = ft.colors.YELLOW_100,
                     border_radius = 8,
                     padding = 10,  # --> separa el interior del cuadro de la nota 
                     margin = 15    # --> separa entre notas
        )
        return note



    # -- CREA GRILLA DE NOTAS --
    grid = ft.GridView (
        expand = True,
        max_extent = 300,
        child_aspect_ratio = 1,  # --> para que tenga la misma longitud 220 en ambos lados
        spacing = 20,  # separación entre filas



        # horizontal = True  --> si quiero hacer la ubicacion vertical
    )
    
    # -- CREA FILA DE NOTAS --
    # notes = [
    #     create_note ("Reunión"),
    #     create_note ("Entregar tp"),
    #     create_note ("leer pdf")
    # ]

    notes = [
        "Reunión",
        "Entregar tp",
        "Leer pdf"
    ]

    # -- CREA FILA DE NOTAS con for --
    for note in notes:
        create_note(notes)
        grid.controls.append(create_note(note))


    page.add (ft.Row (controls= 
                      [
                        ft.Text (value = "Mis Notitas", size = 24, weight = "bold", color = ft.colors.WHITE),    # -> titulo
                        ft.IconButton (icon = ft.icons.ADD, on_click = add_note, icon_color = ft.colors.WHITE)    # -> icono "+"
                      ],
                      alignment = ft.MainAxisAlignment.SPACE_BETWEEN), grid
             )
                
               
    
    # -- CREA NOTAS --
    # note = create_note("Nota Mejorada")
    # page.add (note)
    # note_2 = create_note ("otra nota")  # --> pruebo crear otra nota
    # page.add (note_2)



# ---- PARA VER LA VENTANA GRÁFICA ----
ft.app (target = main) # --> llama a la función main para que se visualice la ventana