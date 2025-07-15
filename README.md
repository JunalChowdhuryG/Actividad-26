# **Actividad 26: Implementacion continua con GitHub Actions**


## **¿Que es la implementacion continua?**


### **Ejercicio teorico**
**¿Que es GitHub Actions?**  
es una herramienta de automatizacion  en GitHub que permite crear flujos de trabajo  para automatizar tareas como compilacion y pruebas despliegue se basa en archivos YAML qu estan en el directorio `.github/workflows` donde se especifican eventos desencadenantes (como push o pull_request), jobs y pasos que ejecutan comandos, en mis actividades utilice `workflows` para automatizar pruebas y linters en [JunalChowdhuryG/Actividades-CC3S2/.github/workflows](https://github.com/JunalChowdhuryG/Actividades-CC3S2/tree/main/.github/workflows) para distintas actividades

**Redacta una definicion de "implementacion continua" (~150 palabras), diferenciandola de "entrega continua" y "despliegue continuo".**  
[IBM: Continuous Deployment](https://www.ibm.com/mx-es/think/topics/continuous-deployment)  

es una practica de desartrollo donde cada cambio en el codigo  pasa las pruebas automatizadas se despliega automaticamente a produccion sin intervencion manual se diferencia de la entrega continua (Continuous Delivery) donde los cambios tambien pasan pruebas automatizadas pero el despliegue a produccion requiere una aprobacion manual  
a veces el termino  implemmentacion continua es usado como sinonimo de implementacion continua aunque puede implicar despliegues mas frecuentes o en entornos no prroductivos la implementacion continua asegura releases rapidos y confiables reduciendo riesgos mediante pruebas exhaustivas  un cambio en el codigo podria desencadenar un workflow de GitHub Actions que ejecuta pruebas unitarias verifica el estilo con flake8 y si todo pasa garantizando actualizaciones continuas y estables en produccion, en mis actividades utilice `workflows` para automatizar pruebas y linters en [JunalChowdhuryG/Actividades-CC3S2/.github/workflows](https://github.com/JunalChowdhuryG/Actividades-CC3S2/tree/main/.github/workflows)





