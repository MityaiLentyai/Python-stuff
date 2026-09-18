from abc import abstractmethod, ABC


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        pass


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass
