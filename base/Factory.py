from abc import ABC,abstractmethod


class Factory(ABC):

    @abstractmethod
    def crate_driver(self):
        pass
    @abstractmethod
    def open_browser(self):
        pass



