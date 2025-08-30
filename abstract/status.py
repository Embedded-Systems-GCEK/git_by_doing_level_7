from abc import ABC, abstractmethod
class AbstractStatus(ABC):
    @abstractmethod
    def completed(self) -> bool:
        pass
    @abstractmethod
    def already_played(self) -> bool:
        pass
    @abstractmethod
    def remaining(self):
        pass
    @abstractmethod
    def progress(self):
        pass
