import classes as c

def main():
    # instancia objeto da classe Conta
    cc = c.ContaCorrente(
        titular="João Silva", 
        cpf="123.456.789-00", 
        agencia="0001", 
        conta="12345-6", 
        saldo=1000.0
    )

    print(f"Saldo: R$ {cc.saldo}")

if __name__ == "__main__":
    main()