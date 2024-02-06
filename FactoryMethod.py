class Document:
  def create(self):
      raise NotImplementedError("Metoda create() musi byt prepisana")

class PDFDocument(Document):
    def create(self):
        return "Vytvaram PDF dokument"

class WordDocument(Document):
    def create(self):
        return "Vytvaram Word dokument"

class Factory():
    def create_document(self, type):
        if type == "pdf":
           return PDFDocument()
        elif type == "word":
            return WordDocument()
        else:
            raise ValueError("Neznamy typ dokumentu")

factory = Factory()
pdf = factory.create_document("pdf")
print(pdf.create())

word = factory.create_document("word")
print(word.create())

txt = factory.create_document("txt")
print(txt.create())

