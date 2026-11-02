import subprocess
import sys

def test_application_output():
    result = subprocess.run(
        [sys.executable, "app.py"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0
    assert "Jenkins Freestyle Project" in result.stdout
    assert "Application executed successfully!" in result.stdout
    assert "Build Status: SUCCESS" in result.stdout
