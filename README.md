🧠 Flask API – Predicción de Cáncer de Mama
1. 🚀 Introducción

Este proyecto implementa una API Flask que utiliza un modelo de clasificación para predecir el diagnóstico de cáncer de mama a partir del dataset Breast Cancer Wisconsin disponible en scikit-learn.

El sistema fue desarrollado como parte de la evaluación modular del Módulo de Machine Learning, enfocándose en el despliegue de modelos y buenas prácticas de CI/CD.

2. 🧩 Estructura del Proyecto
├── app.py                # Código principal de la API Flask
├── Dockerfile            # Configuración para contenedor Docker
├── modelo_cancer.pkl     # Modelo entrenado y serializado
├── requirements.txt      # Dependencias exactas del proyecto
├── test_api.py           # Script para pruebas locales
├── .github/workflows     # Configuración CI/CD (GitHub Actions)
└── train_model.py        # Entrenamiento del modelo (no producción)

3. ⚙️ CI/CD con GitHub y Render

El proyecto utiliza GitHub Actions para integración continua (CI/CD).
Cada push al repositorio desencadena un deploy automático en Render, reconstruyendo la imagen Docker y desplegando la API.

🔒 Se fijaron versiones específicas de librerías para evitar incompatibilidades al cargar el modelo.

4. 🧪 Pruebas de Predicción
✅ Predicción Benigna (0)
curl -X POST https://evaluacion-modular-flask-cancer-api3.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"features": [20.29, 14.34, 135.1, 1297.0, 0.1003, 0.1328, 0.198, 0.1043, 0.1809, 0.0588, 0.7572, 0.7813, 5.438, 94.44, 0.01149, 0.02461, 0.05688, 0.01885, 0.01756, 0.005115, 22.54, 16.67, 152.2, 1575.0, 0.1374, 0.205, 0.4, 0.1625, 0.2364, 0.07678]}'

⚠️ Predicción Maligna (1)
curl -X POST https://evaluacion-modular-flask-cancer-api3.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"features": [13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766, 0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023, 15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259]}'

5. 🧾 Conclusión

El proyecto fue desplegado exitosamente en Render.com, con una API funcional, estable y versionada.
Se demostró su correcto funcionamiento mediante pruebas directas desde línea de comandos (curl y test_api.py).

6. ☁️ Justificación del Entorno de Despliegue y Monitoreo

Aunque la consigna sugería AWS, Azure o GCP, se eligió Render.com por su:

Simplicidad e integración nativa con GitHub.

Despliegue ágil de APIs Flask sin necesidad de VMs ni buckets.

Monitoreo básico de logs desde el dashboard.

🧭 Ideal para entornos académicos o prototipos donde la agilidad prima sobre la infraestructura compleja.

7. 📊 Monitoreo Básico del Endpoint

Desde el dashboard de Render.com se visualizan:

Logs del contenedor en tiempo real.

Estado del despliegue (éxito/error).

Historial de deploys.

Se realizaron pruebas manuales para medir latencia y estabilidad.
Para producción se recomienda integrar herramientas como Prometheus + Grafana o UptimeRobot.

8. 📈 Métricas de Uso y Desempeño (Bonus)
⏱ Latencia

Medida con PowerShell:

Measure-Command {
  Invoke-WebRequest -Uri "https://evaluacion-modular-flask-cancer-api3.onrender.com/predict" `
  -Method POST `
  -Body '{"features": [14.2, 20.0, 92.0, 640.0, 0.1, 0.15, 0.2, 0.08, 0.2, 0.06, 0.6, 1.0, 4.5, 50.0, 0.007, 0.025, 0.03, 0.01, 0.02, 0.004, 16.0, 27.0, 115.0, 800.0, 0.14, 0.3, 0.35, 0.12, 0.25, 0.08]}' `
  -ContentType "application/json"
}


Resultados: entre 0.3 y 0.8 segundos por solicitud.

🔁 Frecuencia de uso

Durante la validación se realizaron más de 10 peticiones al endpoint /predict.
Se sugiere integrar herramientas como Postman Monitor, Google Analytics API Gateway o UptimeRobot para seguimiento continuo.

9. 🖼 Capturas Clave
Sección	Descripción
📁 Estructura del Proyecto	Vista general de archivos y carpetas
🧷 Repositorio GitHub	Código fuente con CI/CD
🚀 Deploy en Render	Logs y estado de despliegue
🧪 Pruebas API	Curl o test_api.py mostrando {"prediction": 0} o 1
📊 Monitoreo y Métricas	Logs y latencias observadas
⚠️ Error Handling (opcional)	Captura de error controlado 400/415
10. 🔮 Mejoras Futuras y Escalabilidad

Aunque Render cumple perfectamente para este proyecto, una futura migración a Kubernetes permitiría:

🔁 Auto-scaling según demanda.

🧬 Despliegues canary o blue-green.

⚖️ Balanceo de carga entre réplicas.

📡 Monitoreo avanzado con Prometheus + Grafana.


🧠 Flask API – Predicción de Cáncer de Mama
1. 🚀 Introducción

Este proyecto implementa una API Flask que utiliza un modelo de clasificación para predecir el diagnóstico de cáncer de mama a partir del dataset Breast Cancer Wisconsin disponible en scikit-learn.

El sistema fue desarrollado como parte de la evaluación modular del Módulo de Machine Learning, enfocándose en el despliegue de modelos y buenas prácticas de CI/CD.

2. 🧩 Estructura del Proyecto
├── app.py                # Código principal de la API Flask
├── Dockerfile            # Configuración para contenedor Docker
├── modelo_cancer.pkl     # Modelo entrenado y serializado
├── requirements.txt      # Dependencias exactas del proyecto
├── test_api.py           # Script para pruebas locales
├── .github/workflows     # Configuración CI/CD (GitHub Actions)
└── train_model.py        # Entrenamiento del modelo (no producción)

3. ⚙️ CI/CD con GitHub y Render

El proyecto utiliza GitHub Actions para integración continua (CI/CD).
Cada push al repositorio desencadena un deploy automático en Render, reconstruyendo la imagen Docker y desplegando la API.

🔒 Se fijaron versiones específicas de librerías para evitar incompatibilidades al cargar el modelo.

4. 🧪 Pruebas de Predicción
✅ Predicción Benigna (0)
curl -X POST https://evaluacion-modular-flask-cancer-api3.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"features": [20.29, 14.34, 135.1, 1297.0, 0.1003, 0.1328, 0.198, 0.1043, 0.1809, 0.0588, 0.7572, 0.7813, 5.438, 94.44, 0.01149, 0.02461, 0.05688, 0.01885, 0.01756, 0.005115, 22.54, 16.67, 152.2, 1575.0, 0.1374, 0.205, 0.4, 0.1625, 0.2364, 0.07678]}'

⚠️ Predicción Maligna (1)
curl -X POST https://evaluacion-modular-flask-cancer-api3.onrender.com/predict \
-H "Content-Type: application/json" \
-d '{"features": [13.54, 14.36, 87.46, 566.3, 0.09779, 0.08129, 0.06664, 0.04781, 0.1885, 0.05766, 0.2699, 0.7886, 2.058, 23.56, 0.008462, 0.0146, 0.02387, 0.01315, 0.0198, 0.0023, 15.11, 19.26, 99.7, 711.2, 0.144, 0.1773, 0.239, 0.1288, 0.2977, 0.07259]}'

5. 🧾 Conclusión

El proyecto fue desplegado exitosamente en Render.com, con una API funcional, estable y versionada.
Se demostró su correcto funcionamiento mediante pruebas directas desde línea de comandos (curl y test_api.py).

6. ☁️ Justificación del Entorno de Despliegue y Monitoreo

Aunque la consigna sugería AWS, Azure o GCP, se eligió Render.com por su:

Simplicidad e integración nativa con GitHub.

Despliegue ágil de APIs Flask sin necesidad de VMs ni buckets.

Monitoreo básico de logs desde el dashboard.

🧭 Ideal para entornos académicos o prototipos donde la agilidad prima sobre la infraestructura compleja.

7. 📊 Monitoreo Básico del Endpoint

Desde el dashboard de Render.com se visualizan:

Logs del contenedor en tiempo real.

Estado del despliegue (éxito/error).

Historial de deploys.

Se realizaron pruebas manuales para medir latencia y estabilidad.
Para producción se recomienda integrar herramientas como Prometheus + Grafana o UptimeRobot.

8. 📈 Métricas de Uso y Desempeño (Bonus)
⏱ Latencia

Medida con PowerShell:

Measure-Command {
  Invoke-WebRequest -Uri "https://evaluacion-modular-flask-cancer-api3.onrender.com/predict" `
  -Method POST `
  -Body '{"features": [14.2, 20.0, 92.0, 640.0, 0.1, 0.15, 0.2, 0.08, 0.2, 0.06, 0.6, 1.0, 4.5, 50.0, 0.007, 0.025, 0.03, 0.01, 0.02, 0.004, 16.0, 27.0, 115.0, 800.0, 0.14, 0.3, 0.35, 0.12, 0.25, 0.08]}' `
  -ContentType "application/json"
}


Resultados: entre 0.3 y 0.8 segundos por solicitud.

🔁 Frecuencia de uso

Durante la validación se realizaron más de 10 peticiones al endpoint /predict.
Se sugiere integrar herramientas como Postman Monitor, Google Analytics API Gateway o UptimeRobot para seguimiento continuo.

9. 🖼 Capturas Clave
Sección	Descripción
📁 Estructura del Proyecto	Vista general de archivos y carpetas
🧷 Repositorio GitHub	Código fuente con CI/CD
🚀 Deploy en Render	Logs y estado de despliegue
🧪 Pruebas API	Curl o test_api.py mostrando {"prediction": 0} o 1
📊 Monitoreo y Métricas	Logs y latencias observadas
⚠️ Error Handling (opcional)	Captura de error controlado 400/415
10. 🔮 Mejoras Futuras y Escalabilidad

Aunque Render cumple perfectamente para este proyecto, una futura migración a Kubernetes permitiría:

🔁 Auto-scaling según demanda.

🧬 Despliegues canary o blue-green.

⚖️ Balanceo de carga entre réplicas.

📡 Monitoreo avanzado con Prometheus + Grafana.

Se recomienda GKE, AKS o EKS si se espera tráfico alto o múltiples servicios relacionados.

💡 Desarrollado con pasión por el aprendizaje continuo y la ingeniería de datos aplicada a la salud.


Se recomienda GKE, AKS o EKS si se espera tráfico alto o múltiples servicios relacionados.

💡 Desarrollado con pasión por el aprendizaje continuo y la ingeniería de datos aplicada a la salud.
