# Actividad 2 - CC3S2
- Se creo el archivo app.py:
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/app-py.png?raw=true)
- Se creo el entorno virtual venv, se activo y se levantó la app con variables de entorno (12-factor):
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/image1.png?raw=true)
- Se ejectuo comando de inspección y de puertos abiertos:
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/image2.png?raw=true)
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/image3.png?raw=true)
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/image4.png?raw=true)
- ¿Qué campos de respuesta cambian si actualizas MESSAGE/RELEASE sin reiniciar el proceso?
  No deberían cambiar ya que la app sigue en proceso, si se reiniciara ahi si cambiarian los mensajes.
- Demuestra que los logs salen por stdout. Explica por qué no se escriben en archivo (12-Factor).
  ```
  [INFO] Starting app on port 8080
   * Serving Flask app 'app'
   * Debug mode: off
  ```
  Los logs se imprimen en stdout, no se escriben en archivo porque siguen el principio 12-factor.
  ## Preguntas HTTP:
    -  Explica idempotencia de métodos y su impacto en retries/health checks. Da un ejemplo con curl -X PUT vs POST.
        Un método idempotente es que al ejecutar una o varias veces tiene el mismo efecto en el servidor(Métodos GET, PUT y DELETE).En retries/health check se suele usar los métodos idempotentes ya que a diferencia de los no idempotentes com un método POST puede generar problemas, por ejemplo si envio un mensaje repetido se puede generar dos veces el mismo.
        ```
        PUT: curl -i -X PUT http://127.0.0.1:8080/resource/1 -d '{"name":"Odsmar"}' -H "Content-Type: application/json"
        Se envia por segunda vez actualiza y no hay cambios, mantiene el mismo id.
        POST: curl -i -X POST http://127.0.0.1:8080/resource -d '{"name":"Odsmar"}' -H "Content-Type: application/json"
        Se envia por segunda vez y se generan dos mensajes con los mismos datos, id=1 e id=2.
        ```
- Ahora se añadio a /etc/host nueva entrada como miapp.local:8080
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/image5.png?raw=true)
- Se verifico el cambio y si se puede accder a traves de la nueva ruta
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Actividad_2/images/image6.png?raw=true)
- ¿Qué diferencia hay entre /etc/hosts y una zona DNS autoritativa? ¿Por qué el hosts sirve para laboratorio? Explica en 3–4 líneas.
  En etc/host solo permite el cambio de manera local, y en una zona DNS si se podria para todos los dispositivos de la misma red.
  El host siento que sirve ya que es una manera rápida el cambio de nombres de la ip.
- 
  
