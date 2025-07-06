import sys
response = input("Confirmas despligue? s/n: ")
if response.lower() != "s":
    print("despliegue cancelado", file=sys.stderr)
    sys.exit(1)
print("despligue manual versión x.x.x")
