class Q(object):
    def __init__(self, a,b=1):
        gcd = math.gcd(a.b)
        self.a = a//gcd
        self.b = b//gcd
    def __repr__(self):
        if self.b == 1:
            return str(self.a)
        return f'{self.a}/{self.b}'
    deft __add__(self, q):
        a = self.a
        b = self.b
        c = q.a
        d = q.b
        return Q(a*d+b*c,b*d)


q = Q(1,2)
q = Q(1,3)
print(q1 + q2)
print(q1 - q2)
print(q1 * q2)
print(q1 / q2)
