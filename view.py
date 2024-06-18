import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "TdP Baseball Manager 2024"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        self._page.bgcolor = "#ebf4f4"
        self._page.window_height = 800
        page.window_center()
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self._txt_name = None
        self._txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Simulazione 01/06/2021", color="blue", size=24)
        self._page.controls.append(self._title)

        self._btnCreaGrafo = ft.ElevatedButton(text="Crea Grafo", on_click=self._controller.handleCreaGrafo)
        row1 = ft.Row([ft.Container(self._btnCreaGrafo, width=500)], alignment=ft.MainAxisAlignment.CENTER)

        self._ddGeni = ft.Dropdown(label="Gene")
        self._btnAdiacenti = ft.ElevatedButton(text="Geni adiacenti", on_click=self._controller.handleDettagli, disabled=True)

        row2 = ft.Row([self._ddGeni, self._btnAdiacenti], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.END)

        self._btnCammino = ft.ElevatedButton(text="Ricerca Cammino", on_click=self._controller.handlePercorso,
                                               disabled=True)
        row3 = ft.Row([self._btnCammino], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.END)

        self._page.controls.append(row1)
        self._page.controls.append(row2)
        self._page.controls.append(row3)
        self._txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(ft.Container(self._txt_result, bgcolor="#deeded", height=350))
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def update_page(self):
        self._page.update()
