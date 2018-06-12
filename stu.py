class stu:
    name = ""
    id = ""
    course = ""
    def __init__(self, n, i, c):
        self.name = n
        self.id = i
        self.course = c
    def __str__(self):
        return str(self.name)+","+ str(self.id)+","+ str(self.course)
class stuls:
    ls = []
    def __init__(self, fn=-1):
        if fn == -1:
            return
        f = open(fn, 'r')
        for l in f:
            self.ls.append(stu(l.split(",")[0],l.split(",")[1],l.split(",")[2]))
        f.close
    def w(self,fn):
        f = open(fn, 'w')
        for s in self.ls:
            f.write(str(s))
        f.close
    def sn(self):
        for i in range(0,len(self.ls)):
            s = i
            for j in range(i,len(self.ls)):
                if self.ls[j].name < self.ls[s].name:
                    s = j
            t = self.ls[i]
            self.ls[i] = self.ls[s]
            self.ls[s] = t
    def f(self,n):
        s = 0
        p = len(self.ls)/2
        e = len(self.ls)
        while True:
            if n == self.ls[p].name:
                return p
            if n < self.ls[p].name:
                e = p
            else:
                s = p + 1
            if s >= e:
                return -1
            p = (s + e) / 2
    def r(self,f,l):
        s = self.f(f)
        e = self.f(l)
        if s == -1:
            s = 0
        if e == -1:
            e = len(self.ls)
        n = stuls()
        n.ls = self.ls[s:e]
        return n
    def sc(self):
        for i in range(0,len(self.ls)):
            p = 0
            for j in range(i,-1,-1):
                if self.ls[j].course < self.ls[i].course:
                    p = j + 1
                    break
            t = self.ls.pop(i)
            self.ls.insert(p,t)
