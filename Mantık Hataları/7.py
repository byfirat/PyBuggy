class Sınıf():
    sınıf_niteliği = 'sınıf niteliği'

    def örnek_metodu(self):
        print(self.nitelik)

    @classmethod
    def sınıf_metodu(cls):
        print('sınıf metodu')

    @staticmethod
    def statik_metot():
        print('statik metot')