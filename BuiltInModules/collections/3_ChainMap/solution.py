from collections import OrderedDict
from collections import ChainMap

class DeepChainMap(ChainMap):
    def __setitem__(self, key, value):
        for mapping in self.maps:
            if key in mapping:
                mapping[key] = value
                return
        self.maps[0][key] = value

    def __delitem__(self, key):
        for mapping in self.maps:
            if key in mapping:
                del mapping[key]
                return
        raise KeyError(key)

default = eval(input())
user = eval(input())
workspace = eval(input())
settings = DeepChainMap(workspace, user, default)
i = input()
del settings[i]
print(settings[i])
i = input()
del settings[i]
print(settings[i])