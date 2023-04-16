class Settings:
    def __init__(self, file):
        self.exclude = []

        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line.startswith('#'):
                    line = line.split('=')
                    line[1] = line[1].split(':')
                    self.parseLine(line)


    def parseLine(self, line):
        if line[0] == 'exclude':
            for key in line[1]:
                self.exclude.append(key)