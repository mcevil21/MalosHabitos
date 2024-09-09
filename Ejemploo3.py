def rectangulo(dimension1, dimension2):
    AreaRectangulo = dimension1 * dimension2
    return AreaRectangulo
def triangulo(base, altura):
    AreaTriangulo = 0.5 * base * altura
    return AreaTriangulo
if __name__ == "__main__":
    def main():
        dimension1 = float(input("Dimension1 :"))
        dimension2 = float(input("Dimension2 :"))
        rect_area = rectangulo(dimension1, dimension2)
        print("Área del rectángulo:", rect_area)
        base = float(input("Base :"))
        altura = float(input("Altura :"))
        tri_area = triangulo(base, altura)
        print("Área del triángulo:", tri_area)
    main()