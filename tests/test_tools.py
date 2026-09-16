from app.tools import analyze_serial_log, review_c_code, review_rtos, safe_calculator

def test_calculator():
    assert safe_calculator("25*48") == "1200"

def test_log_analysis():
    r = analyze_serial_log("E task watchdog triggered\nBrownout detector was triggered")
    assert r["patterns"]["watchdog"] == 1
    assert r["patterns"]["brownout"] == 1

def test_c_review():
    findings = review_c_code("char x[8]; sprintf(x, \"%s\", input);")
    assert any("sprintf" in x for x in findings)

def test_rtos_review():
    findings = review_rtos("Task priority 5 uses mutex and vTaskDelay.")
    assert len(findings) >= 3
