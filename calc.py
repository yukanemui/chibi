class Lambda(Expr):
    __slots__ = ['name', 'body']
    def __init__(self, name, body):
        self.name = name
        self.body = body
    def __repr__(self):
        return f'λ{self.name} . {str(self.body)}'
    def eval(self, env):
        return self
def copy(env): #環境をコピーすることでローカルスコープを作る
    newenv = {}
    for x in env.keys():
        newenv[x] = env[x]
    return env