from julkaisu import Julkaisu
class Kirja(Julkaisu):
    def __init__(self, name, page_count, author):
        self.page_count = page_count
        self.author = author
        super().__init__(name)

    def print_info(self):
        print(f"{self.name} (kirjailija {self.author}, {self.page_count} sivua).")
