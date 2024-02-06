class Osvetlenie:
    def zapni(self):
        print("Osvetlenie zapnuté")

    def vypni(self):
        print("Osvetlenie vypnuté")

class Klimatizacia:
    def zapni(self):
        print("Klimatizácia zapnutá")

    def vypni(self):
        print("Klimatizácia vypnutá")

class AudioSystem:
    def zapni(self):
        print("Audio systém zapnutý")

    def vypni(self):
        print("Audio systém vypnutý")

class DomacAutomatizaciaFacade:
    def __init__(self):
        self.osvetlenie = Osvetlenie()
        self.klimatizacia = Klimatizacia()
        self.audio_system = AudioSystem()

    def vedomRezim(self):
        self.osvetlenie.zapni()
        self.klimatizacia.vypni()
        self.audio_system.zapni()

    def odchodZDomu(self):
        self.osvetlenie.vypni()
        self.klimatizacia.vypni()
        self.audio_system.vypni()

# Usage
dom_automatizacia = DomacAutomatizaciaFacade()
dom_automatizacia.vedomRezim()
dom_automatizacia.odchodZDomu()
