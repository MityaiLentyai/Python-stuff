import abc


class DataProcessor(ABC):

    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass



class NumericProcessor(DataProcessor):
    @abstractmethod
    def validate(self, data: any) -> bool:
        pass
    
    @abstractmethod
    def ingest(self, data: int) -> None:
        pass
class TextProcessor(DataProcessor):
    @abstractmethod
    def validate(self, data: any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: str) -> None:
        pass
class LogProcessor(DataProcessor):
    @abstractmethod
    def validate(self, data: string) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: any) -> None:
        pass

