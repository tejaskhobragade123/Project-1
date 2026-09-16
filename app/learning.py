class LearningEngine:
    def __init__(self, memory):
        self.memory = memory

    def feedback(self, task, answer, useful):
        score = 1.0 if useful else -1.0
        self.memory.add("feedback", f"Task: {task}\nAnswer: {answer}", score)
        rule = (
            "Prefer structured engineering answers with evidence, practical checks and concrete fixes."
            if useful else
            "Improve precision: separate evidence from assumptions and give actionable verification steps."
        )
        self.memory.add("strategy", rule, score)
