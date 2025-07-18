import operator
import ast

def evaluate_expression(expr: str, variables: dict):
    """
    Avalia uma expressão lógica usando variáveis fornecidas.
    Exemplo:
        expr = "(A and B) or not C"
        variables = {"A": True, "B": False, "C": False}
        >>> evaluate_expression(expr, variables)
        True
    """
    allowed_names = {"and": operator.and_, "or": operator.or_, "not": operator.not_}
    allowed_names.update(variables)
    try:
        node = ast.parse(expr, mode='eval')
        code = compile(node, '<string>', 'eval')
        return eval(code, {"__builtins__": None}, allowed_names)
    except Exception as e:
        raise ValueError(f"Erro ao avaliar expressão: {e}")

def logic_flow(steps: list, context: dict):
    """
    Executa uma sequência de funções lógicas condicionais.
    Cada step é um dict: {"condition": expr, "action": func}
    Exemplo:
        steps = [
            {"condition": "A and B", "action": lambda ctx: ctx.update({"result": 1})},
            {"condition": "not A", "action": lambda ctx: ctx.update({"result": 0})}
        ]
        context = {"A": True, "B": False}
        >>> logic_flow(steps, context)
        {'A': True, 'B': False, 'result': 0}
    """
    for step in steps:
        cond = step.get("condition")
        action = step.get("action")
        if evaluate_expression(cond, context):
            action(context)
    return context

def truth_table(expr: str, variables: list):
    """
    Gera a tabela verdade de uma expressão lógica.
    Exemplo:
        expr = "A and not B"
        variables = ["A", "B"]
        >>> truth_table(expr, variables)
        [
            {"A": False, "B": False, "result": False},
            {"A": False, "B": True,  "result": False},
            {"A": True,  "B": False, "result": True},
            {"A": True,  "B": True,  "result": False}
        ]
    """
    from itertools import product
    table = []
    for values in product([False, True], repeat=len(variables)):
        context = dict(zip(variables, values))
        result = evaluate_expression(expr, context)
        row = context.copy()
        row["result"] = result
        table.append(row)
    return table