from julkaisu import Julkaisu

class Lehti(Julkaisu):
    def __init__(self, name, author):
        self.author = author
        super().__init__(name)

    def print_info(self):
        print(f"{self.name} (päätoimittaja {self.author}).")






