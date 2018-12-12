def ValueisError():
    pass


class yesno:
    def __init__(self):
        self.strlsit = []
        self.intlist = []

    def getnum(self):
        while 1:
            num = yield self.intlist,self.strlsit

            try:
                if type(num) is int :
                    self.intlist.append(num)
                elif type(num) is str:
                    self.strlsit.append(num)
                else:
                    raise Exception
            except StopIteration:
                raise StopIteration

            # print(self.intlist,self.strlsit)

    def start(self,numlist):
        gg=self.getnum()
        next(gg)
        try:
            for i in numlist:
                # print(i)
                gg.send(i)
        except Exception:
            print(self.intlist,self.strlsit)

if __name__=="__main__":
    numlsit = [123,"zxc",456,"asd",[123,"asd"]]
    ss = yesno()
    ss.start(numlsit)



