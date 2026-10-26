import ollama

def main():
    # 1. Definir o modelo de embeddings e o texto de entrada
    modelo = "nomic-embed-text"
    texto = "Sistemas para Internet no IFRN: processamento de linguagem natural e embeddings."
    
    print("=" * 60)
    print("Conectando ao Ollama e gerando embeddings...")
    print(f"Modelo utilizado: {modelo}")
    print(f"Texto de entrada: '{texto}'")
    print("=" * 60)

    try:
        # 2. Chamada à API local do Ollama
        resposta = ollama.embeddings(
            model=modelo,
            prompt=texto
        )

        vetor = resposta["embedding"]
        dimensao = len(vetor)

        # 3. Exibição dos resultados e do sumário vetorial
        print("\nEmbeddings gerados com sucesso!")
        print(f"Dimensão do vetor (número de dimensões): {dimensao}")
        print("\nPrimeiros 5 valores do vetor:")
        print(vetor[:5])
        print("\nÚltimos 5 valores do vetor:")
        print(vetor[-5:])
        print("=" * 60)

    except Exception as e:
        print(f"Erro ao conectar com o Ollama: {e}")
        print("Certifique-se de que o aplicativo Ollama está em execução no sistema.")

if __name__ == "__main__":
    main()