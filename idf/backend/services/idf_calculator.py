class IDFCalculator:
    @staticmethod
    def calculate_idf(avaliacoes, temas):
        """
        Calcula o IDF baseado nas avaliações e pesos dos temas
        
        Args:
            avaliacoes (list): Lista de avaliações
            temas (list): Lista de temas com seus respectivos pesos
            
        Returns:
            float: Valor do IDF calculado
        """
        total_peso = sum(tema.peso for tema in temas)
        if total_peso == 0:
            return 0
            
        soma_ponderada = sum(
            avaliacao.nota * avaliacao.tema.peso 
            for avaliacao in avaliacoes
        )
        
        return soma_ponderada / total_peso
