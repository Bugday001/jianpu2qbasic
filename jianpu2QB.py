class converter:
    def __init__(self) -> None:
        self.basicLen = 4
        self.underLine = 0
        self.lowOct = 0
        self.highOct = 0
        self.pound = 0
        self.map = {'1':'C', '2':'D', '3':'E', '4':'F', '5':'G', '6':'A', '7':'B'}

    def init(self):
        self.underLine = 0
        self.lowOct = 0
        self.highOct = 0

    def clearMark(self):
        self.lowOct = 0
        self.highOct = 0
        self.pound = 0

    def markAdd(self, c):
        if c == ',':
            self.lowOct += 1
        elif c == '\'':
            self.highOct += 1
        elif c == '(':
            self.underLine += 1
        elif c == ')':
            self.underLine -= 1
        elif c == '#':
            self.pound += 1

    def convert(self, data):
        ans = ""
        for each in data:
            if each == '-' or each == '0':
                ans += 'P4'
            elif each.isdigit():
                tone = 4 + self.highOct - self.lowOct
                if tone != 4:
                    ans += "O" + str(tone)
                ans += self.map[each]
                if self.pound:
                    ans += '#'
                if self.underLine != 0:
                    num = 4
                    for i in range(self.underLine):
                        num *= 2
                    ans += str(num)
                if tone != 4:
                    ans += "O4"

                self.clearMark()
            elif each == '|':
                ans += ' '
            else:
                self.markAdd(each)
        return ans



if __name__ == "__main__":
    worker = converter()
    while True:
        data = input()
        worker.init()
        qbCode = worker.convert(data)
        print(qbCode)