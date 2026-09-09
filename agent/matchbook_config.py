"""MetBook configuration used by the evaluator.

Keep official Matchbook content here (or replace this module with a secure
backend data source). The evaluator must never accept Matchbook criteria from
an untrusted browser client.
"""

FIRST_VISIT_COMPETENCIES = [
    "quebra_gelo",
    "abordagem_inicial",
    "despertar_de_necessidades",
    "escuta_ativa",
    "ADN",
    "proximos_passos",
    "agendamento",
    "encerramento",
    "tratamento_de_objecoes",
]

# Initial production-safe placeholder. Replace the values with the exact
# approved text from the official MetBook before a MetLife pilot goes live.
FIRST_VISIT_MATCHBOOK = """
Use o conteúdo oficial do MetBook de Corretoras 2026 para Primeira Visita / Abordagem.
Objetivo: descobrir necessidades e traçar o perfil do potencial cliente antes de desenhar uma solução.
Priorize perguntas abertas antes das fechadas, escuta ativa, aprofundamento de necessidades,
ADN e definição de próximos passos. Para objeções, compreender a objeção, ouvir até o fim,
retomar o objetivo do cliente e conduzir a conversa de forma consultiva.

IMPORTANTE: esta configuração é deliberadamente conservadora. Não invente critérios que
não estejam no documento oficial. Substitua este texto pelo Matchbook oficial aprovado
antes do uso em produção.
""".strip()

USE_CASES = {
    "first_visit": {
        "name": "Primeira Visita / Abordagem",
        "matchbook": FIRST_VISIT_MATCHBOOK,
        "competencies": FIRST_VISIT_COMPETENCIES,
    }
}


def get_use_case_config(use_case: str):
    return USE_CASES.get(use_case, USE_CASES["first_visit"])
