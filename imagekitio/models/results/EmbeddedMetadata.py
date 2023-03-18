from typing import List, TypeVar
class EmbeddedMetadata:
    def __init__(self, container: dict):
        if bool(container):
            keys = list(container.keys())
            print("container:====>")
            print(container)
            print(container[keys[0]])
            print("=======")
            for k in container:
                self.items = container[keys[k]]

