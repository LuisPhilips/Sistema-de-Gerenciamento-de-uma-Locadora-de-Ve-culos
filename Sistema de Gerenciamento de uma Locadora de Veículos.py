class Condutor:
    def __init__(self, nome, numero_cnh, categoria_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh
        self.categoria_cnh = categoria_cnh

    def exibir_dados(self):
        print(f"Condutor: {self.nome}")
        print(f"CNH: {self.numero_cnh}")
        print(f"Categoria: {self.categoria_cnh}")


class ContratoLocacao:
    def __init__(self, data_inicio, data_termino, valor_total, status,
                 nome_condutor, numero_cnh, categoria_cnh):

        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = status

        # Composição:
        # o Contrato cria e possui o seu Condutor
        self.condutor = Condutor(
            nome_condutor,
            numero_cnh,
            categoria_cnh
        )

    def finalizar_contrato(self):
        self.status = "finalizado"

    def cancelar_contrato(self):
        self.status = "cancelado"

    def exibir_contrato(self):
        print("=== CONTRATO ===")
        print(f"Início: {self.data_inicio}")
        print(f"Término: {self.data_termino}")
        print(f"Valor: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status}")

        print("\n=== CONDUTOR ===")
        self.condutor.exibir_dados()


# Criando um contrato
contrato = ContratoLocacao(
    "05/10/2026",
    "10/10/2026",
    1500.00,
    "ativo",
    "João Silva",
    "123456789",
    "AB"
)

contrato.exibir_contrato()

# Finalizando o contrato
contrato.finalizar_contrato()

print("\nStatus após finalizar:")
print(contrato.status)
