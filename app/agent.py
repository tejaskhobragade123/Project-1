from openai import OpenAI
from .memory import Memory
from .learning import LearningEngine
from .tools import analyze_serial_log, review_c_code, review_rtos, safe_calculator

class Agent:
    def __init__(self, api_key, model="gpt-4.1-mini"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.memory = Memory()
        self.learning = LearningEngine(self.memory)

    def ask(self, prompt):
        try:
            r = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role":"system","content":
                    "You are an embedded-systems engineering assistant. "
                    "Focus on ESP32, STM32, Embedded C, FreeRTOS, UART, I2C, SPI, "
                    "debugging and practical engineering reasoning. Do not claim "
                    "to have executed code or hardware tests unless actually provided."},
                    {"role":"user","content": prompt}],
                temperature=0.25
            )
            return r.choices[0].message.content
        except Exception as e:
            return f"AI request failed: {e}"

    def embedded_task(self, task, context=""):
        memory = "\n".join(
            f"- {k}: {c}" for k,c,_ in self.memory.recent(6)
        ) or "No previous memory."
        prompt = f"""Analyze this embedded-engineering request.

REQUEST:
{task}

SPECIALIST TOOL OUTPUT:
{context}

LEARNED MEMORY:
{memory}

Return:
1. Diagnosis / explanation
2. Evidence or reasoning
3. Recommended next checks
4. Practical fix or implementation approach
5. Risks / limitations
"""
        return self.ask(prompt)

    def review_c(self, code):
        findings = review_c_code(code)
        context = "Static checks:\n" + ("\n".join("- "+x for x in findings) if findings else "- No basic rule matched.")
        return self.embedded_task("Review this Embedded C code for ESP32/STM32 quality, safety and maintainability. Do not execute it.\n\n"+code, context)

    def analyze_log(self, log):
        result = analyze_serial_log(log)
        context = str(result)
        return self.embedded_task("Analyze this ESP32/STM32 serial log and prioritize likely causes.", context)

    def review_rtos(self, design):
        findings = review_rtos(design)
        context = "RTOS checks:\n" + ("\n".join("- "+x for x in findings) if findings else "- No specific keyword check matched.")
        return self.embedded_task("Review this FreeRTOS design for task priorities, blocking, synchronization, timing and memory concerns.", context+"\n\nDESIGN:\n"+design)

    def explain(self, question):
        return self.embedded_task(question, "No specialist tool required.")

    def calculate(self, expression):
        return safe_calculator(expression)
