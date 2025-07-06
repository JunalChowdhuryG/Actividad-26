import sys
import os

response = input("Confirmas despligue? s/n: ","n")
if response.lower() != "s":
    print("despliegue cancelado", file=sys.stderr)
    sys.exit(1)
print("despligue manual version x.x.x")
