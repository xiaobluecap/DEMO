class Gun(object):
    def __init__(self,bulletBox):
        self.bulletBox=bulletBox

    def shoot(self):
        if self.bulletBox.bulletCount == 0:
            print("no buttleCount")
        else:
            self.bulletBox.bulletCount -=1
            print("hava %d bulletCount" %(self.bulletBox.bulletCount))