pylogicator

Uma biblioteca Python profissional para automação de fluxos lógicos, operações booleanas e construção de tabelas verdade.  
Ideal para projetos científicos, educacionais, industriais e empresariais que demandam precisão e flexibilidade.

 Principais Funcionalidades

- Avaliação de Expressões Lógicas
- Avalie expressões com variáveis dinâmicas.
- Fluxo Lógico Automatizado
- Execute sequências condicionais para automação de decisões.
- Geração de Tabela Verdade
- Crie tabelas verdade a partir de qualquer expressão lógica.

 Instalação

Após publicar no PyPI:
```bash
pip install pylogicator
```
Ou, clone o repositório:
```bash
git clone https://github.com/Mateusdang/pylogicator.git
cd pylogicator
pip install .
```

 Uso Rápido

```python
from pylogicator import evaluate_expression, logic_flow, truth_table

# Avaliando uma expressão lógica
expr = "(A and B) or not C"
variables = {"A": True, "B": False, "C": False}
resultado = evaluate_expression(expr, variables)
print(resultado)  # True

# Criando um fluxo de lógica automatizado
steps = [
    {"condition": "A and B", "action": lambda ctx: ctx.update({"result": 1})},
    {"condition": "not A", "action": lambda ctx: ctx.update({"result": 0})}
]
context = {"A": True, "B": False}
final = logic_flow(steps, context)
print(final)  # {'A': True, 'B': False, 'result': 0}

# Gerando tabela verdade
tabela = truth_table("A and not B", ["A", "B"])
for linha in tabela:
    print(linha)
```

 Exemplos de Aplicação

- Automação de testes lógicos em software.
- Simulação de circuitos digitais e eletrônicos.
- Ensino de lógica computacional.
- Construção de sistemas de decisão inteligente.

 Documentação das Funções

- `evaluate_expression(expr: str, variables: dict)`: avalia expressões lógicas.
- `logic_flow(steps: list, context: dict)`: executa sequência condicional de ações.
- `truth_table(expr: str, variables: list)`: gera tabela verdade.

 Licença

MIT License.  
Veja o arquivo [LICENSE](LICENSE) para detalhes.

 Autor

Desenvolvido por Mateus Dang  
GitHub: [@Mateusdang](https://github.com/Mateusdang)