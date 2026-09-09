import json
import os
from openai import OpenAI
from prompt import SYSTEM_PROMPT, build_user_prompt
from voice_simulation_prompt import VOICE_SIMULATION_SYSTEM_PROMPT, INITIAL_GREETING
from matchbook_config import get_use_case_config


def _json(body, status=200):
    return {"statusCode": status, "headers": {"Content-Type": "application/json", "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "Content-Type", "Access-Control-Allow-Methods": "GET,POST,OPTIONS"}, "body": json.dumps(body, ensure_ascii=False)}


def handler(event, context):
    method = event.get("httpMethod", "GET")
    if method == "OPTIONS":
        return _json({})
    path = event.get("path", "")
    if path.endswith("/health"):
        return _json({"status": "ok", "service": "rhapsody-evaluator-agent"})
    if not os.getenv("OPENAI_API_KEY"):
        return _json({"error": "OPENAI_API_KEY is not configured"}, 500)
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    model = os.getenv("OPENAI_MODEL", "gpt-5.6")
    try:
        body = json.loads(event.get("body") or "{}")
        if path.endswith("/simulate/start"):
            return _json({"text": INITIAL_GREETING})
        if path.endswith("/simulate"):
            history = body.get("conversation", [])
            prompt = "\n".join(("CLIENT: " if x.get("role") == "client" else "BROKER: ") + x.get("text", "") for x in history)
            response = client.responses.create(model=model, instructions=VOICE_SIMULATION_SYSTEM_PROMPT, input=prompt + "\n\nResponda agora como Ricardo, mantendo a persona e revelando somente o que for natural neste momento.", temperature=0.7)
            return _json({"text": response.output_text.strip()})
        if path.endswith("/evaluate"):
            use_case = body.get("use_case", "first_visit")
            config = get_use_case_config(use_case)
            # Matchbook and competencies come from the server-side configuration,
            # never from the browser request.
            user_prompt = build_user_prompt(config["matchbook"], body["transcript"], use_case, body.get("broker_profile"), config["competencies"])
            response = client.responses.create(model=model, instructions=SYSTEM_PROMPT, input=user_prompt, temperature=0.1)
            return _json(json.loads(response.output_text))
        return _json({"error": "Not found"}, 404)
    except Exception as exc:
        return _json({"error": str(exc)}, 502)
