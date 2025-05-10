# 🎞 Cómo Instalar FFmpeg en Windows (para usar con yt-dlp)

`yt-dlp` necesita FFmpeg para realizar tareas de postprocesamiento como convertir vídeos a audio (`.mp3`, `.wav`, etc.). A continuación te explico cómo instalarlo y configurarlo correctamente en tu sistema Windows.

---

## ✅ Paso 1: Descargar FFmpeg

1. Visita la siguiente página web oficial: 👉 https://www.gyan.dev/ffmpeg/builds/
    
2. Descarga el archivo `.zip` que dice:
    
    ```
    Release full build
    ```
    

---

## 📂 Paso 2: Extraer los archivos

1. Extrae el archivo ZIP descargado.
    
2. Renombra la carpeta extraída (si lo deseas) a algo como `ffmpeg`.
    
3. Mueve esa carpeta a una ubicación permanente, por ejemplo:
    
    ```
    C:\ffmpeg
    ```
    

> Asegúrate de que dentro de la ruta exista:  
> `C:\ffmpeg\bin\ffmpeg.exe`  
> `C:\ffmpeg\bin\ffprobe.exe`

---

## ⚙️ Paso 3: Agregar FFmpeg al PATH

Esto permitirá que cualquier programa o script encuentre FFmpeg desde cualquier terminal o entorno de desarrollo.

1. Abre el menú de inicio de Windows y busca:
    
    ```
    Editar las variables de entorno del sistema
    ```
    
2. En la ventana que se abre, haz clic en:
    
    ```
    Variables de entorno...
    ```
    
3. En la sección **"Variables del sistema"**, selecciona `Path` y pulsa **Editar**.
    
4. Añade una nueva entrada:
    
    ```
    C:\ffmpeg\bin
    ```
    
5. Guarda todos los cambios y **reinicia tu terminal o IDE**.
    

---

## 🧪 Paso 4: Verificar la instalación

Abre una terminal y ejecuta los siguientes comandos para comprobar que FFmpeg está disponible:

```
ffmpeg -version
ffprobe -version
```

Si ves información sobre la versión, ¡todo está listo!

---

## 🏁 Listo para usar

Ahora puedes usar herramientas como `yt-dlp` o cualquier otro script en Python que necesite FFmpeg sin problemas.