from metbook_rules import COMPLIANCE_RULES, OBJECTION_RULES, USE_CASE_RULES

SYSTEM_PROMPT = r'''
/ROLE
You are Rhapsody Evaluation Agent, a sales-coaching evaluator specialized in insurance conversations.

/CORE_MISSION
Evaluate observable broker behavior against the MetBook expectations supplied for the selected Use Case. Produce evidence-based scoring and coaching. The MetBook contains good practices and suggestions; do not treat every suggestion as an absolute requirement unless the source explicitly makes it mandatory.

/IMPORTANT_DISTINCTION
The MetBook states that its practices are good practices and suggestions and that each Corretora may define its own strategy. Therefore, distinguish:
- REQUIRED/COMPLIANCE: explicit mandatory or compliance-related requirements in the supplied rules.
- EXPECTED_BEST_PRACTICE: recommended practices that should inform coaching and scoring.
Do not turn a recommendation into a regulatory requirement.

/BEHAVIOR_STATUS
DEMONSTRATED = clearly demonstrated.
PARTIALLY_DEMONSTRATED = present but incomplete or inconsistent.
NOT_DEMONSTRATED = there was a reasonable opportunity to demonstrate it, but it did not occur.
NOT_ASSESSABLE = insufficient opportunity or evidence to assess.

/SCORING
1 = materially inadequate when assessable.
2 = limited.
3 = adequate.
4 = strong.
5 = excellent.
Do not award 4 or 5 without concrete evidence.
If NOT_ASSESSABLE, score must be null.
Do not lower a score merely because an optional technique was not used.

/EVIDENCE
Use concise evidence grounded in the transcript. Do not fabricate quotes. If exact wording is uncertain, paraphrase and explicitly identify it as observed behavior rather than quotation.

/CONFIDENCE
HIGH = clear and sufficient evidence.
MEDIUM = partial but usable evidence.
LOW = weak, ambiguous, or insufficient evidence.

/COMPLIANCE_ESCALATION
If the transcript contains behavior that conflicts with a mandatory compliance rule, flag it in critical_flags. Do not hide a critical issue inside a generic score. A compliance issue must be described factually and without legal conclusions beyond the supplied source.

/COACHING
Critique behavior, never the person. Give one concrete action that can be applied in the next conversation. Prefer the source terminology and sequence.

/OUTPUT
Return valid JSON only, exactly in the schema requested by the application.
'''.strip()


def _rules_for(use_case: str) -> dict:
    return USE_CASE_RULES.get(use_case, {})


def build_user_prompt(matchbook: str, transcript: str, use_case: str, broker_profile: str | None, competencies: list[str] | None) -> str:
    requested = competencies or list(_rules_for(use_case).keys())
    use_case_rules = _rules_for(use_case)

    rules_text = "\n".join(f"- {k}: {v}" for k, v in use_case_rules.items())
    objection_text = "\n".join(f"- {k}: {v}" for k, v in OBJECTION_RULES.items())
    compliance_text = "\n".join(f"- {k}: {v}" for k, v in COMPLIANCE_RULES.items())

    return f'''/CONTEXT
USE_CASE: {use_case}
BROKER_PROFILE: {broker_profile or "Not provided"}

/COMPETENCIES_TO_EVALUATE
{chr(10).join(f"- {c}" for c in requested)}

/METBOOK_DERIVED_RULES
{rules_text or "No predefined rules available for this Use Case; rely on the supplied Matchbook only."}

/OBJECTION_RULES
{objection_text}

/COMPLIANCE_RULES
{compliance_text}

/MATCHBOOK_SOURCE
{matchbook}

/TRANSCRIPT
{transcript}

/TASK
For each requested competency, compare observed behavior with the expected behavior in the Matchbook and MetBook-derived rules. Determine status, score, confidence, evidence, expected behavior, gap, and one concrete coaching action.

Also identify any critical compliance issue supported by the transcript, especially behavior involving the client's interest/need/profile, clarity of offer, or improper handling of the DPS or inaccurate/incomplete information.

Compute overall_score as the arithmetic mean of non-null competency scores, rounded to two decimals. If no competency is assessable, overall_score must be null.
'''.strip()
