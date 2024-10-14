import flet as ft
from flet import VerticalAlignment, MainAxisAlignment, Page
from flet import AppBar, IconButton, ButtonStyle, Text, colors, theme, TextButton

def main(page: Page):
    page.title = "Flet counter example"
    page.theme_mode = "dark"
    
    page.vertical_alignment = VerticalAlignment.START
    txt_function = ft.TextField(value="", text_align=ft.TextAlign.RIGHT, width=100, border_color=colors.WHITE)
    
#region
    def change_theme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()
        
        toggle_theme_button.selected = not toggle_theme_button.selected
        txt_function.border_color = colors.WHITE if page.theme_mode == "dark" else colors.BLACK
        page.update()
    toggle_theme_button = IconButton(icon="dark_mode", on_click=change_theme
                                     ,selected_icon="light_mode"
                                     ,style=ButtonStyle(
                                         color={"":colors.WHITE, "selected":colors.BLACK}))
    
    app_bar = AppBar(title=Text("Newton Raposao", size=30),
                     bgcolor="", leading=IconButton(icon=ft.icons.CALCULATE_ROUNDED), actions=[toggle_theme_button],
                     )
#endregion
    

  

    def plus_click(e):
        txt_function.value = str(int(txt_function.value) + 1)
        page.update()
        
    page.appbar = app_bar
    page.add(
        ft.Row(
            [
                
                txt_function,
                
            ],
            alignment=MainAxisAlignment.CENTER,
        )
    )
    page.add(
        ft.Row(
            [TextButton(text="=", on_click=plus_click),],
            alignment=MainAxisAlignment.CENTER
            ))

def create_buttons():
    a = ""

ft.app(main)


