from library import *

def main ():
    SAL_MIN = 1000000
    SUB_ALI = 120000
    SUB_TRANS = 80000
    BONO = 50000
    nombre = input("digite su nombre ==> ")
    salario = int(input("digite su salario ==> "))
    diastrabajo = int(input("digite los dias de trabajo ==> "))
    saldo_pago = calcular_sueldo (nombre, salario, diastrabajo)
    if saldo_pago < (SAL_MIN * 2):
        saldo_pago = saldo_pago+SUB_ALI+SUB_TRANS
    else:
        saldo_pago = saldo_pago+BONO

    print(f"su sueldo total es: {saldo_pago:.0f}")

if __name__ == "__main__":  
    main()