# Actividad 3 - DevOps y DevSecOps
## Parte Teórica
### 1. Introducción a DevOps: ¿Qué es y qué no es?
- DevOps es un conjunto de prácticas para que el desarrollo de software sea de una manera rápida desde el código hasta la producción, su nombre viene de desarrollo(Dev) y operaciones(Ops).
- A diferencia de waterfall, que trabaja con otro tipo de métodos, DevOps es iterativo e incremental, por lo cual es más rápida y eficiente.
- El lema "You build, yo run it" significa que los desarrolladores también son responsable de ejecutar y mantener la aplicación. Por ejemplo en el laboratorio nosotros configuramos app.py(Flask).
- Qué no es? DevOps no es solo una herramienta como Docker u otras. Uno de los mitos sobre DevOps es que elimina Ops, pero no esa así ya que lo integra en un flujo compartido.
### 2. Marco CALMS en acción
- C(culture): Colaboración entre Dev y Ops
- A(Automation): Automatizar despliegues y pruebas.
- L(Lean): Minimizar desperdicio y fallos con ciclos cortos.
- M(Measurement): Medición con métricas y logs.
- S(Sharing): Compartir aprendizajes y errores
- Extensión Sharing, subir un report.md al repositorio cuando falle el tls para que el equipo de desarrollo también lo solucione.
### 3. Visión Cultural de DevOps y paso a DevSecOps
- DevOps fomenta la colaboración transversal(desarrollo y operaciones), evita que cada equipo trabaje de manera aisalada.
- DevSecOps extiende DevOps integrando seguridad desde el inicio, en lugar de añadirla al final.
- En el laboratorio se uso systemd con configuraciones mínimas para uso en Flask.
### Métodología 12-FactorApp
Son principios para construir app modernas, portables y escalables