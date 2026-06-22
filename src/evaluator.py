from openai import OpenAI
from config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)


class Evaluator:

    def evaluate(self, transcript):

        prompt = f"""
You are a senior healthcare QA engineer.

Review the following call transcript between a patient and a healthcare voice agent.

Analyze:

1. Scheduling mistakes
2. Medication/refill mistakes
3. Incorrect information
4. Safety concerns
5. Hallucinations
6. Poor conversational quality
7. Missed opportunities
8. Repetitive responses
9. Failure to understand intent
10. Policy violations

For each issue provide:
- severity (LOW, MEDIUM, HIGH, CRITICAL)
- category
- description
- recommendation

Return ONLY valid JSON.

Required format:

{{
  "overall_score": 0-100,
  "call_successful": true,
  "summary": "short summary",
  "issues": [
    {{
      "severity": "HIGH",
      "category": "Scheduling",
      "description": "...",
      "recommendation": "..."
    }}
  ]
}}

Transcript:

{transcript}
"""

        response = client.responses.create(
            model="gpt-5",
            input=prompt
        )

        try:
            return json.loads(response.output_text)
        except Exception:
            return {
                "overall_score": 0,
                "call_successful": False,
                "summary": "Failed to parse evaluator output",
                "issues": [
                    {
                        "severity": "HIGH",
                        "category": "System",
                        "description": response.output_text,
                        "recommendation": "Review evaluator output manually"
                    }
                ]
            }