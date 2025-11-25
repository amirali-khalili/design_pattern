from abc import ABC, abstractmethod


class InterFaceMeno(ABC):
    @abstractmethod
    def generate_meno(self):
        pass


class WindoMeno(InterFaceMeno):
    def generate_meno(self):
        return "windodws meno....."


class MacMeno(InterFaceMeno):
    def generate_meno(self):
        return "Mac meno....."


class InterFacebuutem(ABC):
    @abstractmethod
    def generate_buutem(self):
        pass


class Windobuutem(InterFacebuutem):
    def generate_buutem(self):
        return "windodws buutem....."


class Macbuutem(InterFacebuutem):
    def generate_buutem(self):
        return "Mac buutem....."


class FactoryOs(ABC):
    def create_meno(self):
        pass

    def crate_buutem(self):
        pass


class WindowsFactory(FactoryOs):
    def create_meno(self):
        return WindoMeno()

    def crate_buutem(self):
        return Windobuutem()


class MacFactory(FactoryOs):
    def create_meno(self):
        return MacMeno()

    def crate_buutem(self):
        return Macbuutem()


def abstrac_factory(os):
    oss = {"win": WindowsFactory(), "mac": MacFactory()}
    a = oss[os]
    b1 = a.create_meno()
    b2 = a.crate_buutem()
    print(b1.generate_meno())
    print(b2.generate_buutem())


os = input("os :")
abstrac_factory(os)
