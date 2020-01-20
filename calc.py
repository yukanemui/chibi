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
class FuncApp(Expr):
    __slots__ = ['func', 'param']
    def __init__(self, func: Lambda, param):
        self.func = func
        self.param = Expr.new(param)
    def __repr__(self):
        return f'({repr(self.func)}) ({repr(self.param)})'
    def eval(self, env):
        f = self.func.eval(env)
        v = self.param.eval(env)  # パラメータを先に評価する
        name = f.name # Lambda の変数名をとる
        env = copy(env)  # 環境をコピーすることでローカルスコープを作る
        env[name] = v   # 環境から引数を渡す
        return f.body.eval(env)