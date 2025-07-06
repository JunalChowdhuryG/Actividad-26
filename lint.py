import subprocess
import sys

resultado = subprocess.run(["flake8", "."], capture_output=True)
print(resultado.stdout.decode(), file=sys.stderr)
sys.exit(resultado.returncode)
