# Prueba de Entrada CC3S2
Creación del repositorio Prueba de Entrada, en el Curso CC3S2 \
Con la siguiente estructura:
```
Prueba_entrada_CC3S2/
├─ README.md
├─ seccion1_cli_automatizacion/
│  ├─ Makefile
│  ├─ scripts/syscheck.sh
│  └─ reports/{http.txt,dns.txt,tls.txt,sockets.txt}
├─ seccion2_python_git/
│  ├─ app/app.py
│  ├─ tests/test_app.py
│  ├─ coverage.txt    (se genera al correr pytest con cobertura)
│  └─ git_log.txt     (se genera con git log)
└─ seccion3_redes_api/
   ├─ example.html
   ├─ dig_output.txt
   ├─ api_response.json
   ├─ api_title.txt
   ├─ network_answers.txt
   └─ deploy_scenario.txt
```
## Sección 1-CLI y Automatización
- Se verifica el funcionamiento de make all y con ello se creo los siguientes archivos:
  ![Funcionamiento de make all](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image1.png?raw=true)
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image2.png?raw=true)
- En dns.txt se comento sobre TTL.
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image6.png?raw=true)
- En http.txt se explica el código http.
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image4.png?raw=true)
- En sockets.txt se explico el rieso de tener innecesariamiente los puertos abiertos
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image5.png?raw=true)
- En tls.txt se vio la version
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image3.png?raw=true)
- El archivo Makefile: /
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image7.png?raw=true)

## Sección 2- Python + Tests y Git
- Se implemento la función summarize en app.py, así como el CLI python -m app "1,2,3"
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image8.png?raw=true)

## Sección 3- HTTP/TLS - API
- Se genero el example.html y el dig_putput.txt
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image9.png?raw=true)
- Descarga de la respuesta API y extraer el tittle jq
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image10.png?raw=true)
- El API responde con el header Content-Type: application/json y charset=utf-8 (contenido es json y la codificación es utf=8)
  ![Make all - Archivos](https://github.com/Odsmar11/Curso-CC3S2/blob/main/Prueba_Entrada_CC3S2/images/image11.png?raw=true)
- En network_answers.txt se desarrollo algunas preguntas de instrucciones.md