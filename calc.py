X = [0] * 5
Y = [0] * 5
coeffs = [0] * 3
for i in range(0, 4 +1, 1):
    print("X[" + str(i) + "] ni kiriting:")
    X[i] = float(input())
    print("Y[" + str(i) + "] ni kiriting:")
    Y[i] = float(input())
print("Interpolatsiya uchun x qiymatini kiriting:")
xval = float(input())
for i in range(0, 3 +1, 1):
    if X[i] < xval and xval < X[i + 1]:
        index = i
        i = 10
print(index)
a = (Y[index + 1] - Y[index]) / (X[index + 1] - X[index])
b = Y[index] - a * X[index]
ylineer = a * xval + b
print("Funksiya: y=" + str(a) + "x+(" + str(b) + ")")
print("Chiziqli interpolyatsiyada: y(" + str(xval) + ")=" + str(ylineer))
if index + 2 > 4:
    index1 = index - 1
    index2 = index
    index3 = index + 1
else:
    index1 = index
    index2 = index + 1
    index3 = index + 2
coeffs[0] = (Y[index1] * (X[index2] - X[index3]) + Y[index2] * (X[index3] - X[index1]) + Y[index3] * (X[index1] - X[index2])) / ((X[index1] - X[index2]) * (X[index1] - X[index3]) * (X[index2] - X[index3]))
coeffs[1] = (Y[index2] - Y[index1]) / (X[index2] - X[index1]) - coeffs[0] * (X[index1] + X[index2])
coeffs[2] = Y[index1] - coeffs[0] * X[index1] * X[index1] - coeffs[1] * X[index1]
ykvadratik = coeffs[0] * xval * xval + coeffs[1] * xval + coeffs[2]
print("Kvadratik interpolatsiya: y = " + str(coeffs[0]) + "x^2 + " + str(coeffs[1]) + "x + " + str(coeffs[2]))
print("Kvadratik interpolatsiya: y(" + str(xval) + ") = " + str(ykvadratik))
