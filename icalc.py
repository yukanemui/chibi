import pegpy
#from pegpy.tpeg import ParseTree
peg = pegpy.grammar('chibi.tpeg')
parser = pegpy.generate(peg)
'''
tree = parser('1+2*3')
print(repr(tree))
tree = parser('1@2*3')
print(repr(tree))
'''
class Expr(object):
    @classmethod
    def new(cls, v):
        if isinstance(v, Expr):
            return v
        return Val(v)
class Val(Expr):
    __slots__ = ['value']
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f'Val({self.value})'
    def eval(self, env: dict):
        return self.value
e = Val(0)
assert e.eval({}) == 0
class Binary(Expr):
    __slots__ = ['left', 'right']
    def __init__(self, left, right):
        self.left = Expr.new(left)
        self.right = Expr.new(right)
    def __repr__(self):
        classname = self.__class__.__name__
        return f'{classname}({self.left},{self.right})'
class Add(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) + self.right.eval(env)
class Sub(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) - self.right.eval(env)
class Mul(Binary):
    __slots__ = ['left', 'right']
    def eval(self, env: dict):
        return self.left.eval(env) * self.right.eval(env)
    class Div(Binary):
        __slots__ = ['left', 'right']
        def eval(self, env: dict):
            return self.left.eval(env) // self.right.eval(env)
    class Mod(Binary):
        __slots__ = ['left', 'right']
        def eval(self, env: dict):
            return self.left.eval(env) % self.right.eval(env)
    class Eq(Binary): # left == right
        __slots__ = ['left', 'right']
        def eval(self, env: dict):   # cond ? x : y
            return 1 if self.left.eval(env) == self.right.eval(env) else 0
    class Ne(Binary): # left != right
        __slots__ = ['left', 'right']
        def eval(self, env: dict):   # cond ? x : y
            return 1 if self.left.eval(env) != self.right.eval(env) else 0
        class Lt(Binary): # left != right
            __slots__ = ['left', 'right']
            def eval(self, env: dict):   # cond ? x : y
                return 1 if self.left.eval(env) < self.right.eval(env) else 0
        class Lte(Binary): # left != right
            __slots__ = ['left', 'right']
            def eval(self, env: dict):   # cond ? x : y
                return 1 if self.left.eval(env) <= self.right.eval(env) else 0
        class Gt(Binary): # left != right
            __slots__ = ['left', 'right']
            def eval(self, env: dict):   # cond ? x : y
                return 1 if self.left.eval(env) > self.right.eval(env) else 0
        class Gte(Binary): # left != right
            __slots__ = ['left', 'right']
            def eval(self, env: dict):   # cond ? x : y
                return 1 if self.left.eval(env) >= self.right.eval(env) else 0
            class Var(Expr):
                __slots__ = ['name']
                def __init__(self, name):
                    self.name = name
                def __repr__(self):
                    return self.name
                def eval(self, env: dict):
                    if self.name in env:
                        return env[self.name]
                    raise NameError(self.name)     
                class Assign(Expr):
                    __slots__ = ['name', 'e']
                    def __init__(self, name, e):
                        self.name = name
                        self.e = Expr.new(e)
                    def eval(self, env):
                        env[self.name] = self.e.eval(env)
                        return env[self.name]
                class Block(Expr):
                    __slots__ = ['exprs']
                    def __init__(self, *exprs): # 可変長個の引数
                        self.exprs = exprs  # [e, e2, e3, e4, e5] リストになっている
                    def eval(self, env):
                        for e in self.exprs:
                            e.eval(env)   