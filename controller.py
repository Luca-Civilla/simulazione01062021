import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._gene = None

    def handleCreaGrafo(self, e):
        self._model.build_graph()
        nodi,archi = self._model.graphDetails()
        self._view._txt_result.controls.append(ft.Text(f"Nodi: {nodi}\nArchi: {archi}"))


        #CREO DROPDOWN
        for node in self._model._grafo.nodes():
            self._view._ddGeni.options.append(ft.dropdown.Option(data=node, text=node.GeneID, on_click=self.readDDgeni))

        self._view._btnAdiacenti.disabled = False
        self._view.update_page()

    def readDDgeni(self,e):
        if e.control.data is None:
            self._gene = None
        else:
            self._gene = e.control.data
        print(f"readDDgeni called -- {self._gene}")

    def handleDettagli(self, e):
        if self._gene is None:
            self._view._txt_result.controls.append(ft.Text(f"Attenzione selezionare un gene"))
            return
        archi = self._model._vicini(self._gene)
        self._view._txt_result.controls.append(ft.Text("-------------------------------------------------------"))
        self._view._txt_result.controls.append(ft.Text(f"Gene selezionato: {self._gene}"))
        for n in archi:
            self._view._txt_result.controls.append(ft.Text(f"{n[0]} con peso {n[1]}"))
        self._view._txt_result.controls.append(ft.Text("-------------------------------------------------------"))
        self._view.update_page()

    def handlePercorso(self, e):
        pass