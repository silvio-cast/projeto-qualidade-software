def calcular_total_pedido(itens, valor_minimo):
    if not itens:
        raise ValueError("O pedido não pode estar vazio")
    total = sum(item["preco"] for item in itens)
    if total < valor_minimo:
        raise ValueError(
            f"Valor mínimo de R${valor_minimo:.2f} não atingido. Total: R${total:.2f}"
        )
    return total