import operator

import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno_selezionato = None
        self.brand_selezionato = None
        self.retailer_selezionato = None

    def leggi_anno(self, e):
        self.anno_selezionato = self._view.dd_anno.value
        #.value serve per leggere la key dal dropdown

    def leggi_brand(self, e):
        self.brand_selezionato = self._view.dd_brand.value

    def leggi_retailer(self, e):
        self.retailer_selezionato = self._view.dd_retailer.value

    def popola_dd_anno(self):
        anni = self._model.get_anno()
        for anno in anni:
            self._view.dd_anno.options.append(ft.dropdown.Option(anno))
        self._view.update_page()

    def popola_dd_brand(self):
        brands = self._model.get_brand()
        for brand in brands:
            self._view.dd_brand.options.append(ft.dropdown.Option(brand[0]))
        self._view.update_page()

    def popola_dd_retailer(self):
        retailers = self._model.get_retailer()
        for retailer in retailers:
            self._view.dd_retailer.options.append(ft.dropdown.Option(key=retailer.retailer_code, text=retailer.retailer_name,
                                                                     data = retailer))
        self._view.update_page()


    def get_top_vendite(self, e):
        vendite = self._model.get_top_vendite(self.anno_selezionato, self.brand_selezionato, self.retailer_selezionato)
        # serve per ordinare le vendite in senso decrescente di ricavo
        vendite.sort(key=operator.attrgetter("ricavo"), reverse = True)
        self._view.txt_result.controls.clear()
        if len(vendite) <= 5:
            for vendita in vendite:
                self._view.txt_result.controls.append(ft.Text(vendita.__str__()))
        elif len(vendite) == 0:
            self._view.txt_result.controls.append(ft.Text("Nessuna vendita"))
        else:
            for i in range(0,5):
                for vendita in vendite:
                    self._view.txt_result.controls.append(ft.Text(vendita.__str__()))
        self._view.update_page()







    def get_analizza_vendite(self, e):
        pass

