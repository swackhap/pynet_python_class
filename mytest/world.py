
def func1(var1='VARIABLE1',var2='VARIABLE2',var3='VARIABLE3'):
    print 'this is from func1 inside world.py'

class MyClass(object):

    def __init__(self,var1,var2,var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
        print "inside MyClass.hello, var1== " + self.var1 + ", var2== " + self.var2 + ", var3== " + self.var3

def main():
    func1()

if __name__ == "__main__":
    main()
