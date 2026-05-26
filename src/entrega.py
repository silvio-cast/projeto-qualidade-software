def calcular_taxa_entrega(distancia_km):
    TAXA_FIXA = 5.00
    TAXA_POR_KM_EXTRA = 2.00
    LIMITE_TAXA_FIXA = 3.0

    if distancia_km < 0:
        raise ValueError("Distância não pode ser negativa")
    if distancia_km == 0:
        raise ValueError("Distância deve ser maior que zero")

    if distancia_km <= LIMITE_TAXA_FIXA:
        return TAXA_FIXA

    km_extra = distancia_km - LIMITE_TAXA_FIXA
    return round(TAXA_FIXA + (km_extra * TAXA_POR_KM_EXTRA), 2)