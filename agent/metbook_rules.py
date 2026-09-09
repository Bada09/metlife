"""Rules distilled from MetBook de Corretoras_2026.pdf.

This file intentionally keeps the source terminology and separates the two
core conversation flows represented in the material: first visit/approach and
closing visit.
"""

FIRST_VISIT_COMPETENCIES = {
    "quebra_gelo": "Criar empatia e um ambiente favorável à apresentação, reduzindo resistências iniciais.",
    "abordagem_inicial": "Apresentar a Corretora, a parceria com a MetLife e o papel da Corretora de forma clara, generalizada e superficial, criando confiança.",
    "despertar_de_necessidades": "Descobrir necessidades e traçar o perfil do potencial cliente usando perguntas abertas e fechadas, começando pelas abertas e depois direcionando com fechadas.",
    "escuta_ativa": "Perguntar e escutar; manter atenção durante a reunião; evitar interrupções; observar atitudes, emoções e contexto; falar com o cliente, e não para o cliente.",
    "adn": "Coletar informações relevantes sobre despesas, receitas, reservas, projetos, sonhos, perfil de saúde, histórico familiar, profissão, esportes e hobbies para compreender a realidade do cliente.",
    "conscientizacao": "Ajudar o cliente a identificar imprevistos e riscos e reconhecer suas principais preocupações, conectando-as ao papel da Corretora como solucionadora.",
    "proximos_passos": "Após a coleta, identificar as preocupações mais relevantes do cliente, confirmar o que mais o preocupa e apresentar a existência de uma solução personalizada como próximo passo.",
    "agendamento": "Agendar a visita de fechamento, preferencialmente em até 3 dias após a primeira visita, e firmar o compromisso com data, hora e local/plataforma.",
    "encerramento": "Agradecer o tempo e a disponibilidade do cliente e encerrar de forma adequada, inclusive quando houver recusa.",
}

CLOSING_VISIT_COMPETENCIES = {
    "conexao_com_necessidades": "Antes de apresentar a solução, revisar e confirmar os interesses e necessidades levantados na visita de abordagem.",
    "apresentacao_da_solucao": "Apresentar uma solução personalizada aos interesses, necessidades e perfil identificados anteriormente.",
    "clareza_da_oferta": "Ofertar produtos e serviços de forma clara e adequada, minimizando a possibilidade de má compreensão e atendendo ao interesse, necessidade e perfil do cliente.",
    "compreensao_de_objecoes": "Ser receptivo, ouvir atentamente, compreender a objeção real e responder de maneira que ajude o cliente a entender a solução.",
    "fechamento": "Auxiliar o cliente a decidir sobre a contratação, eliminando dúvidas e questionamentos não resolvidos.",
    "encerramento": "Agradecer e encerrar adequadamente a reunião.",
}

OBJECTION_RULES = {
    "understand_first": "Antes de contornar a objeção, procurar entender claramente qual é a objeção.",
    "active_listening": "Ouvir até o fim, manter a calma e distinguir claramente o tipo de objeção.",
    "types": "Classificar, quando possível, como objeção em forma de pergunta, explícita ou vaga.",
    "sim_mas": "O material recomenda utilizar a ferramenta 'Sim, mas...' para tratar objeções.",
    "return_to_goal": "Na abordagem telefônica, após tratar a objeção, voltar à pergunta de disponibilidade para marcar a visita.",
    "two_options_one_choice": "O material apresenta 'Two Options, One Choice' como técnica para conduzir o prospect à escolha entre horários.",
    "less_is_more": "No contato telefônico, evitar excesso de informação; detalhes, números e características do produto devem ser tratados pessoalmente.",
}

COMPLIANCE_RULES = {
    "client_interest": "A oferta deve atender ao interesse, à necessidade e ao perfil do cliente.",
    "clear_adequate": "A oferta, promoção e divulgação devem ser claras e adequadas, minimizando a possibilidade de má compreensão.",
    "principles": "Observar ética, responsabilidade, transparência, diligência, lealdade, probidade, honestidade e boa-fé objetiva.",
    "dps": "A DPS deve sempre, sem exceção, ser preenchida pelo próprio cliente.",
    "no_inducing_falsehood": "Não induzir, aconselhar, incentivar ou incitar o cliente a omitir informações ou prestar informações inexatas/incorretas na proposta ou DPS.",
}

USE_CASE_RULES = {
    "first_visit": FIRST_VISIT_COMPETENCIES,
    "closing_visit": CLOSING_VISIT_COMPETENCIES,
}
