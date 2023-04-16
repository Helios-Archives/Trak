class Sites:
    def __init__(self, file):
        self.sites = []

        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if not line.startswith('#'):
                    line = line.split(' | ')
                    line[1] = line[1].split(',')
                    self.sites.append(line)
