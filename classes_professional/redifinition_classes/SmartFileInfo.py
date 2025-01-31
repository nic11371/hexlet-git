from classes_professional.redifinition_classes.FileInfo import FileInfo


# BEGIN (write your solution here)
class SmartFileInfo(FileInfo):
    def __init__(self, path):
        super().__init__(path)

    def meas(self):

        return {
            'b': super().get_size(),
            'kb': super().get_size() / 1024
        }

    def get_size(self, unit='b'):
        measures = self.meas()
        if unit in measures:
            return measures.get(unit)
        raise ValueError


# END

file_stat = SmartFileInfo('Makefile')
file_stat.get_size()  # 67
file_stat.get_size('b')  # 67
file_stat.get_size('kb')  # 0.0654296875
file_stat.get_size('udav')  # ValueError
