from math_function import add, max, mul, div, mod


def main():

    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
    
    if operator == "*":
        result = mul(data_1, data_2)
    
    if operator == "/":
        result = div(data_1, data_2)
    
    if operator == "lebih":
        result = max(data_1, data_2)

    if operator == "%":
        result = mod(data_1, data_2)
    
    print("{} {} {} = {} ".format(data_1, operator, data_2, result))


if __name__ == "__main__":
    print("Hello Main !")
    main()