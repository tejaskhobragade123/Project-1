# Embedded  AI Agent

A portfolio-grade AI agent designed specifically for **embedded-systems engineering workflows**.

Built to demonstrate Python + AI-agent engineering while connecting directly to embedded skills:
**ESP32, STM32, Embedded C, FreeRTOS, Git and GitHub**.

## What the agent can do

- Analyze ESP32/STM32 serial logs and identify repeated faults
- Review Embedded C for common embedded issues
- Review FreeRTOS task designs
- Explain embedded concepts with practical examples
- Calculate timing/engineering expressions safely
- Maintain persistent SQLite memory
- Learn response preferences from user feedback
- Plan tasks and select specialist tools
- Generate structured engineering reports
- Run from a simple terminal UI

## Agent architecture

```text
                    ┌────────────────────┐
                    │    User Request    │
                    └─────────┬──────────┘
                              ↓
                    ┌────────────────────┐
                    │   Agent Planner    │
                    └─────────┬──────────┘
                              ↓
             ┌────────────────────────────────┐
             │     Embedded Tool Router       │
             ├────────────┬───────────────┬───┤
             ↓            ↓               ↓
       C Code Review   Log Analyzer   RTOS Review
             │            │               │
             └────────────┴───────┬───────┘
                                  ↓
                         ┌────────────────┐
                         │ LLM Reasoning  │
                         └───────┬────────┘
                                 ↓
                    ┌────────────────────┐
                    │ Memory + Learning  │
                    └─────────┬──────────┘
                              ↓
                       Engineering Answer
```

## Why this is useful for an embedded-engineering portfolio

Instead of a generic chatbot, this project demonstrates an AI assistant applied to
real engineering tasks: firmware review, RTOS analysis, serial-debug analysis,
engineering calculations and persistent feedback.

It is especially suitable as a portfolio project alongside ESP32/STM32 and
Embedded C projects.

## Requirements

- Python 3.10+
- OpenAI API key
- Internet connection for LLM requests

## Installation

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

Linux/macOS:
```bash
source .venv/bin/activate
```

Install:
```bash
pip install -r requirements.txt
```

Create `.env`:
```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4.1-mini
```

## Run

```bash
python main.py
```

Try:

```text
> review_c
```

Paste Embedded C code and finish with:
```text
END
```

Or:

```text
> analyze_log
```

Paste a serial log and finish with:
```text
END
```

Other commands:

```text
> rtos
> explain
> calc
> memory
> help
> exit
```

## Example embedded log

See `sample_data/esp32_serial.log`.

The agent can identify patterns such as repeated watchdog resets,
stack-overflow warnings, brownout messages and communication failures.

## Security

- API keys are loaded from `.env`
- `.env` is ignored by Git
- No API key is stored in source code
- Code-review input is analyzed as text and is not executed

## Testing

```bash
pytest
```

## GitHub

Developer profile:
https://github.com/tejaskhobragade123

Suggested repository name:

`embedded-ai-agent`

Suggested description:

`AI agent for embedded firmware review, FreeRTOS analysis, serial-log debugging and engineering memory using Python.`

## Suggested resume entry

**Embedded AI Agent | Python, LLM, SQLite, Embedded C, FreeRTOS**

Built a domain-specific AI agent that analyzes Embedded C, FreeRTOS designs and
ESP32/STM32 serial logs using modular planning and specialist tools. Implemented
persistent SQLite memory and feedback-driven learning, with safe engineering
calculations and structured diagnostic reports.

## Future extensions

- ESP32 serial-port live monitoring with `pyserial`
- STM32CubeIDE project parser
- GitHub repository analysis
- Datasheet/PDF retrieval and RAG
- Vector database memory
- CAN/UART/I2C/SPI diagnostic tools
- FreeRTOS trace analysis
- Web dashboard
- Docker deployment
