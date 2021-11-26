from fractions import Fraction

#edge cases:
# n == 2
# n <= 1

'''construct a matrix for system of equations of type fraction,
find iverse, and solve for radii'''

#make a list of lists containing the rows of the matrix (type 0 = identity, type 1 = coeff)
def buildA(pegs, identity):
    n = len(pegs) - 1
    base = []
    for r in range(n):
        new_row = []
        for c in range(n):
            if r == 0 and c == 0 and not identity:
                new_row.append(Fraction(2, 1))
                new_row.append(Fraction(1, 1))
            elif r == n - 1 and c == 0 and not identity:
                new_row.append(Fraction(1, 1))
            elif r == c:
                new_row.append(Fraction(1, 1))
            else:
                new_row.append(Fraction(1, 1)) if r == c - 1 and r != 0 and not identity else new_row.append(Fraction(0, 1))
        if r == 0 and not identity: new_row.remove(Fraction(0, 1)) #remove extra zero
        base.append(new_row)
    return base


def checkRes(res):
    for rad in res:
        if rad < 1:
            return False
    return True


def invert(sys, identity):
    n = len(sys)
    for r in range(n):
        #step 1: multiply by 1 / diagonal
        diag = sys[r][r]
        const = Fraction(diag.denominator, diag.numerator)
        for c in range(n):
            sys[r][c] *= const
            identity[r][c] *= const
        #step 2: subtract rows
        for i in range(n):
            coeff = sys[i][r]
            for j in range(n):
                if i != r:
                    sys[i][j] -= sys[r][j] * coeff
                    identity[i][j] -= identity[r][j] * coeff
    return identity


def matrixMult(matrix, vector):
    result = []
    for r in range(len(matrix)):
        dot_product = 0
        for c in range(len(matrix)):
            dot_product += matrix[r][c] * vector[c]
        result.append(dot_product)
    return result


def solution(pegs):
    # edge cases
    if len(pegs) <= 1:
        return [-1, -1]
    if len(pegs) == 2:
        dif = Fraction(pegs[1] - pegs[0], 1)
        res = dif / 3
        if res >= 1: return [res.numerator * 2, res.denominator]
        else: return [-1, -1]
    # construct matrix and inverse
    sys = buildA(pegs, False)
    identity = buildA(pegs, True)
    inverse = invert(sys, identity)
    # construct peg difference matrix
    b = []
    for i in range(len(pegs) - 1):
        dif = pegs[i+1] - pegs[i]
        b.append(Fraction(dif, 1))
    #solve
    res = matrixMult(inverse, b)
    if not checkRes(res): return [-1, -1]
    return [res[0].numerator * 2, res[0].denominator]


def main():
    print(solution([4, 30, 50]))


if __name__ == "__main__":
    main()

