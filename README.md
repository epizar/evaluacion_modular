1. Introducción
Este informe documenta el desarrollo y despliegue de una API Flask que utiliza un modelo de clasificación para predecir el diagnóstico de cáncer de mama utilizando el dataset Breast Cancer Wisconsin disponible en scikit-learn. El proyecto fue construido como parte de la evaluación modular del módulo de Machine Learning.
2. Estructura del Proyecto
El proyecto se estructura de la siguiente manera:
├── app.py # Código principal de la API Flask ├── Dockerfile # Configuración para contenedor Docker ├── modelo_cancer.pkl # Modelo entrenado y serializado ├── requirements.txt # Dependencias exactas del proyecto ├── test_api.py # Script para realizar pruebas locales a la API ├── .github/workflows # Configuración de CI/CD con GitHub Actions └── train_model.py # Script para entrenar el modelo (no utilizado en producción)
3. CI/CD con GitHub y Render
Se configuró integración continua (CI/CD) mediante GitHub Actions. Cada vez que se hace push al repositorio, Render reconstruye y despliega automáticamente la API. Se fijaron versiones específicas de las librerías para evitar incompatibilidades al cargar el modelo.
4. Pruebas de Predicción
Se realizaron pruebas exitosas mediante curl. Ejemplos:
• Predicción Benigna (0):
curl -X POST https://evaluacion-modular-flask-cancer-api3.onrender.com/predict -H "Content-Type: application/json" -d "{"features": [20.29, 14.34, 135.1, 1297.0, 0.1003, 0.1328, 0.198, 0.1043, 0.1809, 0.0588, 0.7572, 0.7813, 5.438, 94.44, 0.01149, 0.02461, 0.05688, 0.01885, 0.01756, 0.005115, 22.54, 16.67, 152.2, 1575.0, 0.1374, 0.205, 0.4, 0.1625, 0.2364, 0.07678]}"
• Predicción Maligna (1):
curl -X POST https://evaluacion-modular-flask-cancer-api3.onrender.com/predict -H "Content-Type: application/json" -d "{"features": [13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766, 0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023, 15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259]}"
5. Conclusión
El proyecto fue desplegado exitosamente en Render.com con una API funcional y estable, utilizando CI/CD y versionado controlado. Se demostró su funcionalidad mediante pruebas directas desde la línea de comandos.
6. Justificación del Entorno de Despliegue y Monitoreo
Aunque la consigna sugería el uso de plataformas como AWS, Azure o Google Cloud Platform, se optó por Render.com debido a su simplicidad, integración nativa con GitHub, y facilidad para desplegar APIs Flask sin necesidad de configurar máquinas virtuales, buckets o entornos complejos. Esto permitió un desarrollo ágil, centrado en el modelo y la API, sin desviar esfuerzos al mantenimiento de infraestructura compleja.
Render permite visualizar logs del contenedor en tiempo real desde el dashboard, facilitando el monitoreo básico de eventos, errores y peticiones. Aunque no ofrece herramientas de monitoreo avanzadas como CloudWatch o Azure Insights, es suficiente para proyectos de desarrollo, pruebas o formación.
Además, Render simplifica enormemente el proceso de despliegue de APIs mediante Docker y GitHub Actions sin requerir configuraciones de red, permisos ni billing complejo. Esto lo hace especialmente adecuado para entornos académicos, prototipos o proyectos individuales. A diferencia de AWS, GCP o Azure, no requiere configurar buckets, firewalls o roles IAM, lo que agiliza la curva de aprendizaje.
7. Monitoreo Básico del Endpoint
El monitoreo se realizó desde el dashboard de Render.com. El panel de la aplicación muestra:
• • Logs del contenedor en tiempo real
• • Estado de despliegue actual (éxito/error)
• • Historial de despliegues
Además, se realizaron pruebas manuales usando curl para verificar la latencia y estabilidad del endpoint. Para una solución de producción, se sugiere implementar Prometheus + Grafana o integrar servicios externos como UptimeRobot.
8. Métricas de Uso y Desempeño (Bonus)
Como parte del monitoreo básico, se establecieron las siguientes métricas para evaluar el desempeño de la API:
• Latencia:
Se midió usando Measure-Command en PowerShell con resultados entre 0.3 y 0.8 segundos por solicitud. El comando utilizado fue:
Measure-Command { Invoke-WebRequest -Uri "https://evaluacion-modular-flask-cancer-api3.onrender.com/predict" -Method POST -Body '{"features": [14.2, 20.0, 92.0, 640.0, 0.1, 0.15, 0.2, 0.08, 0.2, 0.06, 0.6, 1.0, 4.5, 50.0, 0.007, 0.025, 0.03, 0.01, 0.02, 0.004, 16.0, 27.0, 115.0, 800.0, 0.14, 0.3, 0.35, 0.12, 0.25, 0.08]}' -ContentType "application/json" }
• Frecuencia de uso:
Durante la fase de validación, se realizaron más de 10 solicitudes al endpoint `/predict`. La frecuencia de uso puede ampliarse en producción mediante la integración de herramientas como UptimeRobot, Google Analytics API Gateway, o servicios como Postman Monitor.
En un entorno productivo, se recomienda almacenar logs de acceso con timestamps para construir dashboards que permitan visualizar uso horario, IPs, status codes y latencia individual.


9. Capturas de pantalla clave
🖼🖼􀀀 1. Estructura del Proyecto
🖼🖼􀀀 2. Repositorio en GitHub
🖼🖼􀀀 3. Deploy en Render
• Captura 1: Configuración del servicio (nombre, build command, start command).

• Captura 2: Logs en Render mostrando despliegue exitoso (Deploy succeeded).
• Captura 3: URL activa de la API y prueba en navegador o Postman.
🖼🖼􀀀 4. Pruebas de API
• Captura 1: curl desde CMD o PowerShell con respuesta {"prediction": 0} o 1.
• Captura 2 (bonus): Ejecución de test_api.py mostrando el resultado de predicción.
🖼🖼􀀀 5. Monitoreo y Métricas
• Captura: Logs en Render mostrando varias peticiones a /predict.
• Debe mostrar: Frecuencia de uso y tiempos de respuesta (latencia observada).
• Consola con Measure-Command o similar para medir latencia.
🖼🖼􀀀 6. Error Handling (opcional)
• Captura: Error controlado si se manda un payload incorrecto, mostrando un 400 o 415.
10. Mejoras Futuras o Escalabilidad
🚀🚀 Escalabilidad y Uso de Kubernetes (opcional)
Aunque el despliegue actual se realiza mediante Render.com, una plataforma sencilla y eficaz para proyectos pequeños o académicos, en un entorno de producción real sería recomendable migrar la API a un orquestador como Kubernetes.
Kubernetes permitiría:
• Escalar horizontalmente el servicio basado en demanda (Auto-scaling).
• Realizar despliegues canarios o blue-green para actualizaciones sin downtime.
• Gestionar múltiples réplicas con balanceadores de carga.
• Integrar herramientas de monitoreo como Prometheus + Grafana para observar latencia, uso y errores.
Este tipo de despliegue se puede realizar en proveedores como Google Kubernetes Engine (GKE), Azure Kubernetes Service (AKS) o Amazon EKS, y es especialmente útil si se espera una alta carga de tráfico o múltiples servicios relacionados con el modelo.
