import ast
import operator
import re
from collections import Counter

BINOPS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.Mod: operator.mod
}

def safe_calculator(expression):
    def ev(node):
        if isinstance(node, ast.Expression): return ev(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -ev(node.operand)
        if isinstance(node, ast.BinOp) and type(node.op) in BINOPS:
            return BINOPS[type(node.op)](ev(node.left), ev(node.right))
        raise ValueError("Only basic arithmetic is supported")
    return str(ev(ast.parse(expression, mode="eval")))

def analyze_serial_log(log):
    lines = [x.strip() for x in log.splitlines() if x.strip()]
    patterns = {
        "watchdog": r"(?i)watchdog|wdt|task watchdog",
        "brownout": r"(?i)brownout|brown.?out",
        "stack": r"(?i)stack.*overflow|stack canary",
        "assert": r"(?i)assert|assertion failed",
        "hardfault": r"(?i)hardfault|hard fault",
        "heap": r"(?i)heap|out of memory|malloc failed",
        "uart": r"(?i)uart|serial",
        "i2c": r"(?i)i2c",
        "spi": r"(?i)spi"
    }
    hits = Counter()
    evidence = {}
    for name, pattern in patterns.items():
        matched = [line for line in lines if re.search(pattern, line)]
        if matched:
            hits[name] = len(matched)
            evidence[name] = matched[:5]
    return {"lines": len(lines), "patterns": dict(hits), "evidence": evidence}

def review_c_code(code):
    findings = []
    rules = [
        (r"\bgets\s*\(", "Unsafe gets() usage."),
        (r"\bsprintf\s*\(", "sprintf() can overflow buffers; prefer bounded formatting."),
        (r"\bstrcpy\s*\(", "strcpy() can overflow buffers; validate destination capacity."),
        (r"volatile\s+[^;=]+;", "volatile found; verify that it is used for a genuinely asynchronous/shared register or ISR variable."),
        (r"HAL_Delay\s*\(", "HAL_Delay() blocks execution; consider task scheduling or non-blocking timing where appropriate."),
        (r"xTaskCreate\s*\(", "FreeRTOS task creation detected; verify stack size, priority and lifetime."),
        (r"malloc\s*\(", "Dynamic allocation detected; assess fragmentation and deterministic-memory requirements.")
    ]
    for pattern, message in rules:
        if re.search(pattern, code):
            findings.append(message)
    return findings

def review_rtos(text):
    findings = []
    checks = [
        (r"(?i)priority", "Priority decisions are mentioned; check for starvation and priority inversion."),
        (r"(?i)mutex", "Mutex usage is mentioned; verify ownership and bounded critical sections."),
        (r"(?i)semaphore", "Semaphore usage is mentioned; verify whether a mutex, binary semaphore or counting semaphore is intended."),
        (r"(?i)queue", "Queue usage is mentioned; verify queue length, item size and producer/consumer timing."),
        (r"(?i)delay|vTaskDelay", "Delay behavior is mentioned; check whether periodic timing should use vTaskDelayUntil()."),
        (r"(?i)stack", "Stack sizing is mentioned; check high-water-mark measurements under worst-case load.")
    ]
    for pattern, message in checks:
        if re.search(pattern, text):
            findings.append(message)
    return findings
