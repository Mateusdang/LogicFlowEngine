# logicflowengine

**Uma biblioteca Python profissional para automação de fluxos lógicos, operações booleanas e construção de tabelas verdade.**

Ideal para projetos científicos, educacionais, industriais e empresariais que demandam precisão e flexibilidade.

---

## Principais Funcionalidades

- **Avaliação de Expressões Lógicas:** Avalie expressões com variáveis dinâmicas.
- **Fluxo Lógico Automatizado:** Execute sequências condicionais para automação de decisões.
- **Geração de Tabela Verdade:** Crie tabelas verdade a partir de qualquer expressão lógica.

---

## Instalação

**Via PyPI:**
```bash
pip install logicflowengine==0.1.1
```

**Via GitHub (repositório):**
```bash
git clone https://github.com/Mateusdang/logicflowengine.git
cd logicflowengine
pip install .
```

---

## Uso Rápido

```python
from logicflowengine import evaluate_expression, logic_flow, truth_table

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
# Saída:
# {'A': False, 'B': False, 'result': False}
# {'A': False, 'B': True, 'result': False}
# {'A': True, 'B': False, 'result': True}
# {'A': True, 'B': True, 'result': False}
```

---

## Exemplos Avançados

### 1. Avaliação de Expressões Complexas

```python
from logicflowengine import evaluate_expression

expr = "((A or B) and (not C or D)) and (E == False)"
variables = {"A": True, "B": False, "C": True, "D": True, "E": False}
print(evaluate_expression(expr, variables))  # True
```

### 2. Fluxo Lógico com Funções Customizadas

```python
from logicflowengine import logic_flow

def acao_personalizada(ctx):
    ctx['resultado'] = ctx.get('valor', 0) * 2

steps = [
    {"condition": "A and (valor > 5)", "action": acao_personalizada},
    {"condition": "not A", "action": lambda ctx: ctx.update({"resultado": -1})}
]
context = {"A": True, "valor": 10}
final = logic_flow(steps, context)
print(final)  # {'A': True, 'valor': 10, 'resultado': 20}
```

### 3. Geração de Tabela Verdade com Análise

```python
from logicflowengine import truth_table
import pandas as pd  # Exemplo de integração

expr = "(A or B) and not (C and D)"
variables = ["A", "B", "C", "D"]
tabela = truth_table(expr, variables)
df = pd.DataFrame(tabela)
print(df)
# Filtrar apenas casos onde resultado é True
print(df[df['result'] == True])
```

### 4. Uso em Sistemas de Decisão Inteligente

```python
from logicflowengine import evaluate_expression

def tomar_decisao(entrada):
    expr = "(temperatura > 30 and umidade < 50) or alerta"
    return evaluate_expression(expr, entrada)

sensor = {"temperatura": 32, "umidade": 45, "alerta": False}
print(tomar_decisao(sensor))  # True
```

### 5. Simulação de Circuito Digital

```python
from logicflowengine import evaluate_expression, truth_table

# Porta lógica XOR
expr = "A != B"
print(evaluate_expression(expr, {"A": True, "B": False}))  # True

# Gerar tabela verdade para XOR
print(truth_table(expr, ["A", "B"]))
```

---

## Exemplos de Aplicação

- Automação de testes lógicos em software.
- Simulação de circuitos digitais e eletrônicos.
- Ensino de lógica computacional.
- Construção de sistemas de decisão inteligente.

---

## Documentação das Funções

### `evaluate_expression(expr: str, variables: dict) -> bool`
Avalia uma expressão lógica booleana utilizando variáveis dinâmicas.

**Parâmetros:**
- `expr`: Expressão lógica (ex: `"A and not B"`).
- `variables`: Dicionário com variáveis booleanas (ex: `{"A": True, "B": False}`).

**Retorno:**  
- Resultado booleano da expressão.

---

### `logic_flow(steps: list, context: dict) -> dict`
Executa uma sequência condicional de ações baseada em fluxo lógico.

**Parâmetros:**
- `steps`: Lista de dicionários contendo `"condition"` (expressão lógica) e `"action"` (função a ser executada).
- `context`: Dicionário de contexto (variáveis de entrada).

**Retorno:**  
- Contexto atualizado após execução dos passos.

---

### `truth_table(expr: str, variables: list) -> list`
Gera a tabela verdade para uma expressão lógica.

**Parâmetros:**
- `expr`: Expressão lógica (ex: `"A and not B"`).
- `variables`: Lista de variáveis presentes na expressão (ex: `["A", "B"]`).

**Retorno:**  
- Lista de dicionários, cada linha representa uma combinação de valores das variáveis e o resultado da expressão.

---

## Licença


Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](https://github.com/Mateusdang/logicflowengine/blob/main/LICENSE.md) para mais detalhes.

---

## Autor

Desenvolvido por **Mateus Dang**  
[GitHub: @Mateusdang](https://github.com/Mateusdang)

---


## Referências

- [Documentação Python](https://docs.python.org/pt-br/3/)
- [PyPI](https://pypi.org/project/logicflowengine/0.1.1/)