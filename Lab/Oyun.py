class Karakter:
    def __init__(self,id,isim,seviye,can,guc):
        self.id = id
        self.isim = isim
        self.seviye = seviye
        self.can = can
        self.guc = guc

class Sovalye(Karakter):
    def __init__(self,id,isim,seviye,can,guc,zirh):
        self.zirh = zirh
        super().__init__(id,isim,seviye,can,guc)
    def bilgigoser(self):
        print("-----------------------------")
        print(f"Kullanıcı ID: {self.id}")
        print(f"İsim: {self.isim}")
        print(f"Seviye: {self.seviye}")
        print(f"Can: {self.can}")
        print(f"Güç: {self.guc}")
        print(f"Mana: {self.zirh}")
class Buyucu(Karakter):
    def __init__(self,id,isim,seviye,can,guc,mana):
        self.mana = mana
        super().__init__(id,isim,seviye,can,guc)

    def bilgigoser(self):
        print("-----------------------------")
        print(f"Kullanıcı ID: {self.id}")
        print(f"İsim: {self.isim}")
        print(f"Seviye: {self.seviye}")
        print(f"Can: {self.can}")
        print(f"Güç: {self.guc}")
        print(f"Mana: {self.mana}")


def main():
    karakter = []
    s1 = Sovalye(1, "Arthas", 10, 100, 20, "Ağır Zırh")
    s2 = Sovalye(2, "Lancelot", 8, 90, 18, "Orta Zırh")
    b1 = Buyucu(3, "Merlin", 12, 70, 25, 150)
    b2 = Buyucu(4, "Gandalf", 15, 65, 30, 200)

    karakter.append(s1)
    karakter.append(s2)
    karakter.append(b1)
    karakter.append(b2)

    for k in karakter:
        k.bilgigoser()
        print("------------")


if __name__ == "__main__":
    main()
