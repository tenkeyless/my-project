from abc import ABC, abstractmethod

class BaseAlgorithm(ABC):
    @abstractmethod
    def run(self, graph, start, goal):
        pass