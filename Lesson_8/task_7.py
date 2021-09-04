class Complex:
    def __init__(self, k):
        self.n = k
        self.meaning = []
        a = self.n.find('-')
        if a < 0:
            self.nu = self.n.split('+')
        else:
            n2 = self.n.replace('-', '+-')
            self.nu = n2.split('+')
        for i in self.nu:
            try:
                b = int(i)
                self.meaning.append(b)
            except:
                b = i
                self.meaning.append(b)
        self.mean = self.meaning

    def __add__(self, other):
        nlist = []
        self.num = self.mean
        other.num = other.mean
        for i in self.num:
            if type(i) is int:
                nlist.append(i)
                self.num.remove(i)
            else:
                pass
        for i in other.num:
            if type(i) is int:
                nlist.append(i)
                other.num.remove(i)
            else:
                pass
        a = sum(nlist)
        if a == 0:
            a = ''
        else:
            pass
        s1 = self.num[0]
        s2 = other.num[0]
        if s1[-1] == s2[-1]:
            if len(s1) == 1:
                b = (f'1{s1}')
            elif len(s1) == 2 and s1[0] == '-':
                b = (f'-1{s1}')
            else:
                b = s1
            if len(s2) == 1:
                c = (f'1{s2}')
            elif len(s2) == 2 and s1[0] == '-':
                c = (f'-1{s2}')
            else:
                c = s2
            x1 = b[-1]
            x2 = int(b[:-1])
            x3 = int(c[:-1])
            b = (f'{x2 + x3}{x1}')
            result = (f'{a}+{b}')
        else:
            b = s1
            c = s2
            result = (f'{a}+{b}+{c}')
        a = result.find('-')
        if a <= 0:
            print(result)
        else:
            print(result.replace('+-', '-'))

    def __mul__(self, other):
        a1 = [self.meaning[0], other.meaning[0]]
        b1 = [self.meaning[0], other.meaning[1]]
        c1 = [self.meaning[1], other.meaning[0]]
        d1 = [self.meaning[1], other.meaning[1]]
        if type(a1[0]) is int and type(a1[1]) is int:
            a = (a1[0] * a1[1])
        elif type(a1[0]) is int:
            s1 = a1[0]
            s3 = a1[1][-1]
            if len(a1[1]) == 1:
                s2 = 1
            elif len(a1[1]) == 2 and a1[0] == '-':
                s2 = -1
            else:
                s2 = int(a1[1][:-1])
            a = f'{s1 * s2}{s3}'
        elif type(a1[1]) is int:
            s1 = a1[1]
            s3 = a1[0][-1]
            if len(a1[0]) == 1:
                s2 = 1
            elif len(a1[0]) == 2 and a1[0] == '-':
                s2 = -1
            else:
                s2 = int(a1[0][:-1])
            a = f'{s1 * s2}{s3}'
        elif a1[0][-1] == a1[1][-1]:
            s1 = a1[0]
            s2 = a1[1]
            if len(s1) == 1:
                a3 = (f'1{s1}')
            elif len(s1) == 2 and s1[0] == '-':
                a3 = (f'-1{s1}')
            else:
                a3 = s1
            if len(s2) == 1:
                a4 = (f'1{s2}')
            elif len(s2) == 2 and s1[0] == '-':
                a4 = (f'-1{s2}')
            else:
                a4 = s2
            x1 = a3[-1]
            x2 = int(a3[:-1])
            x3 = int(a4[:-1])
            a = (f'{x2 * x3}{x1}**2')
        else:
            if len(a1[0]) == 1:
                s1 = 1
            elif len(a1[0]) == 2 and a1[0][0] == '-':
                s1 = -1
            else:
                s1 = int(a1[0][:-1])
            if len(a1[1]) == 1:
                s2 = 1
            elif len(a1[1]) == 2 and a1[1][0] == '-':
                s2 = -1
            else:
                s2 = int(a1[1][:-1])
            s3 = a1[0][-1]
            s4 = a1[1][-1]
            a = f'{s1 * s2}{s3}{s4}'
        if type(b1[0]) is int and type(b1[1]) is int:
            b = (b1[0] * b1[1])
        elif type(b1[0]) is int:
            s1 = b1[0]
            s3 = b1[1][-1]
            if len(b1[1]) == 1:
                s2 = 1
            elif len(b1[1]) == 2 and b1[0] == '-':
                s2 = -1
            else:
                s2 = int(b1[1][:-1])
            b = f'{s1 * s2}{s3}'
        elif type(b1[1]) is int:
            s1 = b1[1]
            s3 = b1[0][-1]
            if len(b1[0]) == 1:
                s2 = 1
            elif len(b1[0]) == 2 and b1[0] == '-':
                s2 = -1
            else:
                s2 = int(b1[0][:-1])
            b = f'{s1 * s2}{s3}'
        elif b1[0][-1] == b1[1][-1]:
            s1 = b1[0]
            s2 = b1[1]
            if len(s1) == 1:
                b3 = (f'1{s1}')
            elif len(s1) == 2 and s1[0] == '-':
                b3 = (f'-1{s1}')
            else:
                b3 = s1
            if len(s2) == 1:
                b4 = (f'1{s2}')
            elif len(s2) == 2 and s1[0] == '-':
                b4 = (f'-1{s2}')
            else:
                b4 = s2
            x1 = b3[-1]
            x2 = int(b3[:-1])
            x3 = int(b4[:-1])
            b = (f'{x2 * x3}{x1}**2')
        else:
            if len(b1[0]) == 1:
                s1 = 1
            elif len(b1[0]) == 2 and b1[0][0] == '-':
                s1 = -1
            else:
                s1 = int(b1[0][:-1])
            if len(b1[1]) == 1:
                s2 = 1
            elif len(b1[1]) == 2 and b1[1][0] == '-':
                s2 = -1
            else:
                s2 = int(b1[1][:-1])
            s3 = b1[0][-1]
            s4 = b1[1][-1]
            b = f'{s1 * s2}{s3}{s4}'
        if type(c1[0]) is int and type(c1[1]) is int:
            c = (c1[0] * c1[1])
        elif type(c1[0]) is int:
            s1 = c1[0]
            s3 = c1[1][-1]
            if len(c1[1]) == 1:
                s2 = 1
            elif len(c1[1]) == 2 and c1[0] == '-':
                s2 = -1
            else:
                s2 = int(c1[1][:-1])
            c = f'{s1 * s2}{s3}'
        elif type(c1[1]) is int:
            s1 = c1[1]
            s3 = c1[0][-1]
            if len(c1[0]) == 1:
                s2 = 1
            elif len(c1[0]) == 2 and c1[0] == '-':
                s2 = -1
            else:
                s2 = int(c1[0][:-1])
            c = f'{s1 * s2}{s3}'
        elif c1[0][-1] == c1[1][-1]:
            s1 = c1[0]
            s2 = c1[1]
            if len(s1) == 1:
                c3 = (f'1{s1}')
            elif len(s1) == 2 and s1[0] == '-':
                c3 = (f'-1{s1}')
            else:
                c3 = s1
            if len(s2) == 1:
                c4 = (f'1{s2}')
            elif len(s2) == 2 and s1[0] == '-':
                c4 = (f'-1{s2}')
            else:
                c4 = s2
            x1 = c3[-1]
            x2 = int(c3[:-1])
            x3 = int(c4[:-1])
            c = (f'{x2 * x3}{x1}**2')
        else:
            if len(c1[0]) == 1:
                s1 = 1
            elif len(c1[0]) == 2 and c1[0][0] == '-':
                s1 = -1
            else:
                s1 = int(c1[0][:-1])
            if len(c1[1]) == 1:
                s2 = 1
            elif len(c1[1]) == 2 and c1[1][0] == '-':
                s2 = -1
            else:
                s2 = int(c1[1][:-1])
            s3 = c1[0][-1]
            s4 = c1[1][-1]
            c = f'{s1 * s2}{s3}{s4}'
        if type(d1[0]) is int and type(d1[1]) is int:
            d = (d1[0] * d1[1])
        elif type(d1[0]) is int:
            s1 = d1[0]
            s3 = d1[1][-1]
            if len(d1[1]) == 1:
                s2 = 1
            elif len(d1[1]) == 2 and d1[0] == '-':
                s2 = -1
            else:
                s2 = int(d1[1][:-1])
            d = f'{s1 * s2}{s3}'
        elif type(d1[1]) is int:
            s1 = d1[1]
            s3 = d1[0][-1]
            if len(d1[0]) == 1:
                s2 = 1
            elif len(d1[0]) == 2 and d1[0] == '-':
                s2 = -1
            else:
                s2 = int(d1[0][:-1])
            d = f'{s1 * s2}{s3}'
        elif d1[0][-1] == d1[1][-1]:
            s1 = d1[0]
            s2 = d1[1]
            if len(s1) == 1:
                d3 = (f'1{s1}')
            elif len(s1) == 2 and s1[0] == '-':
                d3 = (f'-1{s1}')
            else:
                d3 = s1
            if len(s2) == 1:
                d4 = (f'1{s2}')
            elif len(s2) == 2 and s1[0] == '-':
                d4 = (f'-1{s2}')
            else:
                d4 = s2
            x1 = d3[-1]
            x2 = int(d3[:-1])
            x3 = int(d4[:-1])
            d = f'{x2 * x3}{x1}**2'
        else:
            if len(d1[0]) == 1:
                s1 = 1
            elif len(d1[0]) == 2 and d1[0][0] == '-':
                s1 = -1
            else:
                s1 = int(d1[0][:-1])
            if len(d1[1]) == 1:
                s2 = 1
            elif len(d1[1]) == 2 and d1[1][0] == '-':
                s2 = -1
            else:
                s2 = int(d1[1][:-1])
            s3 = d1[0][-1]
            s4 = d1[1][-1]
            d = f'{s1 * s2}{s3}{s4}'
        result = f'{a}+{b}+{c}+{d}'
        i = result.find('-')
        if i <= 0:
            print(result)
        else:
            print(result.replace('+-', '-'))


x = Complex('3+i')
y = Complex('2-3i')
n = Complex('7-3x')
m = Complex('k-7')
t = Complex('6x+1')
v = Complex('8-4y')
p = Complex('4+5n')
s = Complex('5-9m')

x + y
n * m
t + v
p * s
