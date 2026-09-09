# Rhapsody Evaluation Agent

Agente HTTP para avaliar uma conversa de vendas comparando a transcrição com o Matchbook e devolver scoring + evidências + gaps + coaching.

## Entradas

`POST /evaluate`

```json
{
  "use_case": "Discovery",
  "broker_profile": "Experiência: 5 anos; Hub: SP",
  "matchbook": "...comportamentos esperados...",
  "transcript": "...transcrição...",
  "competencies": ["discovery", "assertiveness", "objection_handling"]
}
```

## Saída

```json
{
  "overall_score": 3.67,
  "top_strength": "...",
  "top_development_area": "...",
  "next_action": "...",
  "competencies": [
    {
      "competency": "assertiveness",
      "score": 3,
      "status": "PARTIALLY_DEMONSTRATED",
      "confidence": "HIGH",
      "evidence": "...",
      "expected": "...",
      "gap": "...",
      "feedback": "..."
    }
  ]
}
```

## Rodando localmente

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="..."
export OPENAI_MODEL="gpt-5.6"
uvicorn main:app --host 0.0.0.0 --port 8000
```

Health check: `GET /health`

Avaliação: `POST /evaluate`

## Segurança

Nunca coloque `OPENAI_API_KEY` no GitHub. Use variável de ambiente ou secret do ambiente de deploy.

## Próxima etapa

Conectar o endpoint ao backend da Rhapsody/dashboard e substituir o conjunto inicial de competências pelas definições oficiais do Matchbook de cada Use Case.
