import os
from dotenv import load_dotenv
from app.agent import Agent

def read_multiline():
    print("Paste content. Type END on a new line when finished.")
    rows = []
    while True:
        line = input()
        if line == "END":
            break
        rows.append(line)
    return "\n".join(rows)

def main():
    load_dotenv()
    key = os.getenv("OPENAI_API_KEY")
    if not key:
        raise SystemExit("Missing OPENAI_API_KEY. Create .env from .env.example.")
    agent = Agent(key, os.getenv("OPENAI_MODEL", "gpt-4.1-mini"))

    print("\n=== Embedded Engineering AI Agent ===")
    print("Commands: review_c, analyze_log, rtos, explain, calc, memory, help, exit")

    while True:
        cmd = input("\n> ").strip()
        if cmd == "exit":
            break
        if cmd == "help":
            print("review_c: review Embedded C\nanalyze_log: analyze ESP32/STM32 logs")
            print("rtos: review FreeRTOS design\nexplain: ask an embedded question")
            print("calc: safe arithmetic\nmemory: show learned memory")
            continue
        if cmd == "review_c":
            answer = agent.review_c(read_multiline())
        elif cmd == "analyze_log":
            answer = agent.analyze_log(read_multiline())
        elif cmd == "rtos":
            answer = agent.review_rtos(read_multiline())
        elif cmd == "explain":
            answer = agent.explain(input("Question: "))
        elif cmd == "calc":
            answer = agent.calculate(input("Expression: "))
        elif cmd == "memory":
            rows = agent.memory.recent(12)
            answer = "\n".join(f"[{k} / {s}] {c[:180]}" for k,c,s in rows) or "Memory is empty."
        else:
            print("Unknown command. Type help.")
            continue

        print("\n" + answer)
        if cmd not in {"calc", "memory"}:
            useful = input("\nWas this useful? [y/n]: ").strip().lower() == "y"
            agent.learning.feedback(cmd, answer, useful)
            print("Feedback stored for future responses.")

if __name__ == "__main__":
    main()
