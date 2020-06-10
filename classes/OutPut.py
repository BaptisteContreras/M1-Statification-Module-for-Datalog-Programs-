class OutPut:

    def __init__(self):
        self.output = ""

    def setData(self, data):
        self.output = ""

        if len(data):
            lastKey = sorted(data.keys())[-1];

            for key in sorted(data.keys()):
                self.output += "P" + str(key) + " = {"

                for i in range(len(data[key])):
                    rule = data[key][i]
                    self.output += " " + rule.__str__()
                    if i + 1 != len(data[key]):
                        self.output += "\n"

                self.output += "}"
                if key != lastKey:
                    self.output += '\n'

    def print(self):
        print(self.output)
