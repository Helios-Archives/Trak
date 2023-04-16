class Settings:
    def __init__(self):
        self.exclude = []

    def parseLine(self, line):
        if line[0] == 'exclude':
            for key in line[1]:
                self.exclude.append(key)