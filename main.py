class Avtobus:
    def __init__(self, limit):
        self.limit = limit
        self.yolovchilar = 0

    def chiqish(self):
        if self.yolovchilar < self.limit:
            self.yolovchilar += 1
            print("🧍 Yo‘lovchi chiqdi")
        else:
            print("❌ Avtobus to‘la")

    def tushish(self):
        if self.yolovchilar > 0:
            self.yolovchilar -= 1
            print("⬇️ Yo‘lovchi tushdi")
        else:
            print("Avtobus bo‘sh")

    def holat(self):
        print(f"🚍 Ichida: {self.yolovchilar}/{self.limit}")


avtobus1 = Avtobus(5)

avtobus1.chiqish()
avtobus1.chiqish()
avtobus1.chiqish()
avtobus1.holat()

avtobus1.tushish()
avtobus1.holat()
