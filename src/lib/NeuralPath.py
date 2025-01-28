class NeuralPath:

    def __init__(self, path="neurons"):
        self.__global_path = f"{str(path)}/"

    def set_path(self, path):
        self.__global_path = path

    def get_path(self):
        return self.__global_path

    def get_wb(self, name, w=False):
        return self.__global_path + name + (".w.npz" if w else ".b.npz")

    def get_hwb(self, name, w=False):
        return self.__global_path + name + (".hw.npz" if w else ".hb.npz")
