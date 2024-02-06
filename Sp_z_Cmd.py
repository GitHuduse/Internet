print("Sp_z_Cmd");print("Version:1.0");print("© All right reserved Sp_z")
while True:
    _init_ = input(">>>")
    if _init_ == 'exit':
        exit()
    elif _init_ == '':
        pass
    elif _init_ == 'calc':
        print("Calculator V1.0")
        while True:
            a = input("Number:")
            b = input("Number:")
            c = str(input("mode:(+ - * /):"))
            if a in '0123456789' and b in '0123456789':
                if c == '+':
                    print('As a result, it was:',str(float(a) + float(b)))
                elif c == '-':
                    print('As a result, it was:',str(float(a) - float(b)))
                elif c == '*':
                    print('As a result, it was',str(float(a) * float(b)))
                elif c == '/':
                    print('As a result, it was:',str(float(a) / float(b)))
                elif c == 'exit':
                    break

                else:
                    pass
    else:
        print(f'"{_init_}"is not recognized as an internal or external command.\nPlease try ')