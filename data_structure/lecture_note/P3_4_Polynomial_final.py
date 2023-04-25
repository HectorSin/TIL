# 클래스로 구현.
class Polynomial :
    def __init__( self ):
        self.coef= []

    def degree(self) :
        return len(self.coef) - 1

    def display(self, msg="f(x) = "):
        print("  ", msg, end='')
        deg = self.degree()

        for n in range(deg, 0, -1) :
            print("%5.1f x^%d + " % (self.coef[n], n), end='')
        print("%4.1f"%self.coef[0])

    def add(self, b):
        p = Polynomial()
        if self.degree() > b.degree() :
            p.coef = list(self.coef)
            for i in range(b.degree()+1) :
                p.coef[i] += b.coef[i]
        else :
            p.coef = list(b.coef)
            for i in range(self.degree()+1) :
                p.coef[i] += self.coef[i]
        return p

    def evalualte(self, x):
        result = 0.0
        for i in range(self.degree()+1) :
            result += self.coef[i] * (x**i)
        return result
   
    def mult(self, b):
        result = Polynomial()
        result.coef = [0.0]*(self.degree()+b.degree()+1)

        for i in range(len(self.coef)):
            for j in range(len(b.coef)):
                result.coef[i+j] += self.coef[i]*b.coef[j]  
        return result

    # 단항 연산자 중복 함수: -p
    def __neg__(self):
        p = Polynomial()
        for c in self.coef :
            p.coef.append(-c)
        return p

    def sub(self, b):   # p.sub(q) === p-q
        return self.add(-b)

    # 이항 연산자 중복 함수: p-q
    def __sub__(self, b):
        return self.add(-b)

    # read를 멤버 함수로 구현한 경우
    def read(self):
        deg = int(input("다항식의 최고 차수를 입력하시오: "))
        for n in range(deg+1) :
            coef = float(input(  "\tx^%d의 계수 : " % (deg-n)))
            self.coef.append(coef)
        self.coef.reverse()

    # read2 --> 편리한 입력 --> 문자열의 split() 기능 사용
    def read2(self):
        strlist = input("최고차항부터 차수를 순서대로 입력하시오: ").split()
        for coef in strlist :
            self.coef.append(float(coef))   # 최고차항부터 저장
        self.coef.reverse()                 # 최저차항부터 저장


if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()
    a.read2()
    b.read2()
    c = a.add(b)
    d = a.sub(b)
    e = a.mult(b)
    f = a-b
    a.display("A(x) = ")
    b.display("B(x) = ")
    c.display("A+B  = ")
    d.display("A-B  = ")
    e.display("A*B  = ")
    f.display("A-B  = ")
    print("   B(2) =  ", b.evaluate(2))
