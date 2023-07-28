def tipo_de_pago(cuenta):
    if cuenta < 150000:
        return "Pago en efectivo"
    elif 150000 <= cuenta <= 300000:
        return "Pago con el celular (dinero electrónico)"
    elif 300000 < cuenta <= 600000:
        return "Pago con tarjeta de débito"
    else:
        return "Pago con tarjeta de crédito"

try:
    cuenta = float(input("Ingresa el monto de la cuenta: "))

    tipo_pago = tipo_de_pago(cuenta)
    print("Tipo de pago recomendado:", tipo_pago)
except ValueError:
    print("Error: Por favor, ingresa un valor numérico válido para la cuenta.")
