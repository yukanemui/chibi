class Q(object):
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def __repr__(self):
        return f'{self.a}/{self.b}'


q = Q(1,2)
print(q)
