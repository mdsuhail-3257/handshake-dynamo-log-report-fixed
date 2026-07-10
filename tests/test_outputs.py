import json
from pathlib import Path

REPORT = Path("/app/report.json")


def test_report_saved_as_json():
    """instruction.md: 'write a JSON summary to /app/report.json'
    The report must exist and parse as valid JSON."""
    assert REPORT.exists(), "no report.json found"
    json.loads(REPORT.read_text())


def test_total_requests():
    """instruction.md: 'total_requests: the total number of requests
    (log lines) in access.log'"""
    report = json.loads(REPORT.read_text())
    assert report["total_requests"] == 6, report


def test_unique_ips():
    """instruction.md: 'unique_ips: the number of distinct client IPs
    that made requests'"""
    report = json.loads(REPORT.read_text())
    assert report["unique_ips"] == 3, report


def test_top_path():
    """instruction.md: 'top_path: the single most-requested request path'"""
    report = json.loads(REPORT.read_text())
    assert report["top_path"] == "/index.html", report
