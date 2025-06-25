# Dashboard de Vendas com Taipy

## Visão Geral

O Dashboard de Vendas é uma aplicação interativa e multilíngue desenvolvida com Taipy GUI, projetada para oferecer uma visão abrangente do desempenho de vendas. Este dashboard apresenta métricas-chave, gráficos e análises detalhadas que permitem aos usuários acompanhar tendências, identificar produtos de alto desempenho e tomar decisões baseadas em dados.

## Principais Funcionalidades

### Suporte Multilíngue
- Compatível com 6 idiomas: Português (Brasil), Inglês (EUA), Espanhol, Francês, Italiano e Alemão
- Tradução automática de interface, gráficos e formatação de dados específica para cada região

### Análise de Dados Interativa
- **Filtros Dinâmicos**: Filtragem por período de data e categoria
- **Métricas-Chave**: Visualização rápida de receita total, total de pedidos, valor médio por pedido e categoria de maior desempenho
- **Visualizações Gráficas**:
  - Gráfico de linha mostrando a receita ao longo do tempo
  - Gráfico de barras exibindo receita por categoria
  - Ranking dos 10 produtos com melhor desempenho

### Interface Intuitiva
- Design responsivo com cards interativos
- Layout limpo e organizado para facilitar a navegação
- Tabela de dados brutos para análises detalhadas

## Requisitos

- Python 3.8+
- Taipy
- Pandas
- Polars (para geração de dados de exemplo)
- Babel (para formatação de moeda)

## Como Executar

1. Clone o repositório ou baixe os arquivos do projeto
2. Instale as dependências:
   ```
   pip install taipy pandas polars babel
   ```
3. Execute o gerador de dados de teste (opcional, se precisar criar dados sintéticos):
   ```
   python dados_vendas.py
   ```
4. Inicie o dashboard:
   ```
   python dashboard_taipy.py
   ```
5. Acesse a interface através do navegador no endereço indicado pelo terminal (normalmente http://127.0.0.1:5000)

## Estrutura do Projeto

- **dashboard_taipy.py**: Aplicação principal com interface e lógica do dashboard
- **translations.py**: Módulo de internacionalização com suporte a múltiplos idiomas
- **dados_vendas.py**: Gerador de dados sintéticos para demonstração

## Personalização

O dashboard pode ser facilmente personalizado:

- **Dados**: Substitua o arquivo CSV por seus próprios dados de vendas
- **Idiomas**: Adicione novos idiomas estendendo o dicionário de traduções
- **Estilos**: Modifique o CSS na seção `page.css` para alterar a aparência
- **Métricas**: Adapte ou adicione métricas de acordo com suas necessidades específicas

## Detecção Automática de Idioma

O dashboard possui a capacidade de detectar automaticamente o idioma dos dados carregados, tornando-o flexível para trabalhar com diferentes fontes de dados.

---

Desenvolvido com [Taipy](https://www.taipy.io/), uma ferramenta moderna para criação de aplicações web com Python.
