from math_function import add, mul, div, exp, max_number, root

def main():
    
    data_1 = int(input("masukkan input 1 :"))
    data_2 = int(input("masukkan input 2 :"))
    operator = input("masukkan operator :")

    if operator == "+":
        result = add(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
    
    if operator == "*":
        result = mul(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))

    if operator == "/":
        result = div(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))
    
    if operator == "**":
        result = exp(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))

    if operator == "max":
        result = max_number(data_1, data_2)
        print("max number is", result)

    if operator == "root":
        result = root(data_1, data_2)
        print("{} {} {} = {} ".format(data_1, operator, data_2, result))

if __name__ == "__main__":
    print("Hello Main !")
    main()