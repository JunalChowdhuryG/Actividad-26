# **Actividad 26: Implementacion continua con GitHub Actions**


## **¿Que es la implementacion continua?**


### **Ejercicio teorico**
**¿Que es GitHub Actions?**  
es una herramienta de automatizacion  en GitHub que permite crear flujos de trabajo  para automatizar tareas como compilacion y pruebas despliegue se basa en archivos YAML qu estan en el directorio `.github/workflows` donde se especifican eventos desencadenantes (como push o pull_request), jobs y pasos que ejecutan comandos, en mis actividades utilice `workflows` para automatizar pruebas y linters en [JunalChowdhuryG/Actividades-CC3S2/.github/workflows](https://github.com/JunalChowdhuryG/Actividades-CC3S2/tree/main/.github/workflows) para distintas actividades

**Redacta una definicion de "implementacion continua" (~150 palabras), diferenciandola de "entrega continua" y "despliegue continuo".**  
[IBM: Continuous Deployment](https://www.ibm.com/mx-es/think/topics/continuous-deployment)  

es una practica de desartrollo donde cada cambio en el codigo  pasa las pruebas automatizadas se despliega automaticamente a produccion sin intervencion manual se diferencia de la entrega continua (Continuous Delivery) donde los cambios tambien pasan pruebas automatizadas pero el despliegue a produccion requiere una aprobacion manual  
a veces el termino  implemmentacion continua es usado como sinonimo de implementacion continua aunque puede implicar despliegues mas frecuentes o en entornos no prroductivos la implementacion continua asegura releases rapidos y confiables reduciendo riesgos mediante pruebas exhaustivas  un cambio en el codigo podria desencadenar un workflow de GitHub Actions que ejecuta pruebas unitarias verifica el estilo con flake8 y si todo pasa garantizando actualizaciones continuas y estables en produccion, en mis actividades utilice `workflows` para automatizar pruebas y linters en [JunalChowdhuryG/Actividades-CC3S2/.github/workflows](https://github.com/JunalChowdhuryG/Actividades-CC3S2/tree/main/.github/workflows)


## **¿Por qué automatizar la implementación?**
### **Tabla que compare 3 ventajas de un deploy automatizado vs 3 riesgos de hacerlo manual, y propone contramedidas**

| **ventajas  deploy automatizado** | **riesgos  deploy manual** | **contramedidas** |
|-------------------------------------|------------------------------|-------------------|
| **es rapido** ya que automatiza tareas repetitivas esto reduce el tiempo de despliegue | **los errores hummanos** introducir comandos incorrectos o si saltamos pasos  | documentar procesos  |
| **es consistente** ya que ejecuta los mismos pasos en cada despliegue| **falta de consistencia** ya que  diferentes personas pueden seguir procesos distintos | Esstandarisar scripts |
| **reduces riesgos** ya que las pruebas automatizadas aseguran q el codigo es estable antes del despliegue | **despliegues fallidos**: errores no detectados pueden llegar a produccio | implementar pruebas manuales exaustivas antes de  desplegar |

## **Introducción a la automatización con GitHub Actions**

### **diferencia entre uses: y run:**
* **uses**: invoca una acción predefinida como `actions/checkout@v4` que encapsula lógica compleja y se puede reusar
* **run**: ejecuta un comando directo en la terminal del runner como python deploy.py


## **Por qué GitHub Actions?**

### **Escribe en Comparativa-CI.md un párrafo donde compares GitHub Actions con Jenkins y GitLab CI, enfocándote en integración con GitHub, facilidad de uso y coste.**

**GitHub actions , Jenkins y GitLab CI son simmilares pero se diferencian:**
- **GitHub Actions** destaca por la integración nativa con GitHub lo que facilita  configuración y gestión  workflows directamente en el repositorio ess ideal para proyectos  en GitHub  la sintaxis YAML es intuitiva   yy su Marketplace ofrece acciones reutilizables aunque puede ser costoso para proyectos grandes debido a los minutos facturables 
- **jenkins** siendo de código abierto es  personalizable pero requiere configurar servidores y plugins lo que lo hace menos accesible para principiantes
- **GitLab CI** integrado en GitLab ofrece  experiencia similar a GitHub Actions pero su dependencia de GitLab limita su uso en otros entornos
