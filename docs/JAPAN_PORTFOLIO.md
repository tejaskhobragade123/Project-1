# Japan Embedded-Engineering Portfolio Positioning

## Project title
Embedded Engineering AI Agent

## One-line pitch
A Python AI agent that assists embedded engineers with Embedded C review,
FreeRTOS design analysis, ESP32/STM32 serial-log diagnosis and persistent
feedback-driven engineering memory.

## Resume bullets
- Developed a Python-based domain-specific AI agent for ESP32/STM32 firmware analysis.
- Implemented specialist tools for Embedded C static checks, FreeRTOS design review,
  serial-log pattern detection and safe engineering calculations.
- Built persistent SQLite memory and feedback-driven learning to reuse successful
  response strategies across sessions.
- Designed a modular agent architecture separating planning, tools, reasoning,
  memory and user feedback.

## Interview explanation

"I built this project to combine my embedded-systems background with Python and
AI-agent development. The agent is not just a chatbot. It routes engineering
tasks to specialist tools. For example, a serial log is first analyzed for
watchdog, brownout, stack and memory patterns; the structured result is then
given to the language model for diagnosis and verification steps. For FreeRTOS,
the agent checks synchronization, priorities, queues and timing concerns. I also
added SQLite memory so user feedback can improve future response strategy."

## Important technical honesty

Do not claim that the agent independently trains an AI model. Its current learning
mechanism is feedback-driven memory and strategy selection. Model fine-tuning or
vector-based retrieval can be added later.
