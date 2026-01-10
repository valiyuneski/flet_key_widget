import flet as ft

class Body(ft.Container):
    def __init__(self):
        super().__init__()
        self.content = ft.Text("Flet app is running!")
        self.bgcolor = "yellow"
        self.content.color = "blue"
        self.padding = 10
        self.border_radius = 5

def main(page: ft.Page):
    page.title = "Flet Key Widget"
    page.window_width = 240
    page.window_height = 100
    page.window_resizable = False
    page.padding = 0
    page.bgcolor = ft.Colors.TRANSPARENT
    page.window.bgcolor = ft.Colors.TRANSPARENT
    page.window.title_bar_hidden = True
    page.window.title_bar_buttons_hidden = True
    page.window.frameless = True
    page.window.always_on_top = True
    
    # For macOS, we need to set the window to be transparent
    if page.platform == "macos":
        page.window_transparent = True
        page.window_skip_task_bar = True
        page.window_focused = True
    
    # Add a simple text control to verify the app is working
    page.add(
        Body()
    )

if __name__ == "__main__":
    ft.run(main)