class Giris:
    def __init__(self,kullaniciadi,parola):
        self.kullaniciadi = kullaniciadi
        self.parola = parola

class Like(Giris):
    def __init__(self,kullaniciadi,parola, id):
        Giris.__init__(self,kullaniciadi,parola)
        self.id = id
    def begen(self):
        print(f"Girmiş olduğunuz {self.kullaniciadi} adlı hesaptan {self.id} numaralı gönderi beğenilmiştir.")

like1 = Like("_furkan.gul", "the.lord", "515364")
like1.begen()
