# Redes Scraping

## Presentación

**Redes Scraping** es un proyecto de automatización de inicio de sesión y scraping en dos plataformas populares: **Facebook** e **Instagram**. Utiliza **Selenium** junto con técnicas de simulación de comportamiento humano para evitar bloqueos por parte de las plataformas. El propósito principal de este proyecto es automatizar el proceso de inicio de sesión, gestionar cookies para autenticación persistente y realizar scraping de datos sin ser detectado como un bot.

## Propósito

El objetivo del proyecto es demostrar el uso de **Selenium** con técnicas avanzadas para emular el comportamiento humano en la automatización de navegadores, garantizando así que las interacciones con los sitios web no sean bloqueadas por medidas de seguridad. Además, el sistema guarda las cookies de sesión para automatizar futuros inicios de sesión sin necesidad de ingresar credenciales nuevamente.

## Requisitos

Para ejecutar este proyecto, necesitas tener los siguientes componentes:

- **Python 3.7+**
- **Selenium**: Para interactuar con los navegadores web.
- **webdriver-manager**: Para gestionar automáticamente la instalación de ChromeDriver.
- **dotenv**: Para manejar las variables de entorno de manera segura.
- **Chrome** (u otro navegador compatible con Selenium).

### Librerías necesarias

Es recomendable que uses un entorno virtual para evitar conflictos de dependencias. Para crear uno, ejecuta los siguientes comandos:

1. Crea un entorno virtual:
    ```bash
    python -m venv venv
    ```

2. Activa el entorno virtual:
    - En **Windows**:
      ```bash
      .\venv\Scripts\Activate.ps1
      ```
    - En **Mac/Linux**:
      ```bash
      source venv/bin/activate
      ```

3. Instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

El archivo `requirements.txt` debe contener:

```
selenium==4.10.0
webdriver-manager==4.10.0
python-dotenv==1.0.0
```

## Instrucciones de uso

### 1. Configuración de Variables de Entorno

El proyecto requiere algunas variables de entorno para el acceso a las cuentas de Facebook e Instagram. Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes variables con tus credenciales:

```env
FACEBOOK_USERNAME=tu_email
FACEBOOK_PASSWORD=tu_contraseña
INSTAGRAM_USERNAME=tu_usuario
INSTAGRAM_PASSWORD=tu_contraseña
```

### 2. Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos:

```
redes_scrape/
│
├── src/
│   ├── common/
│   │   ├── driver_manager.py         # Gestión del WebDriver con webdriver-manager
│   │   ├── human_behavior.py         # Funciones para simular comportamiento humano
│   │   ├── cookie_manager.py         # Funciones para guardar y cargar cookies
│   │   └── logger.py                 # Configuración del logger
│   │
│   ├── facebook/
│   │   └── login.py                  # Script para realizar el login en Facebook
│   │
│   ├── instagram/
│   │   └── login.py                  # Script para realizar el login en Instagram
│   │
│   └── config/
│       └── settings.py               # Configuración y variables de entorno
│
├── cookies/                          # Carpeta para almacenar las cookies guardadas
├── .env                              # Archivo de variables de entorno
├── requirements.txt                  # Dependencias del proyecto
└── README.md                         # Documentación del proyecto
```

### 3. Ejecución del Proyecto

1. Asegúrate de tener instalado **Google Chrome** (o el navegador de tu elección compatible con Selenium).
2. Crea y activa el entorno virtual como se indicó en el paso anterior.
3. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

4. Ejecuta el script de login para **Facebook** o **Instagram**:

Para **Facebook**:
```bash
python -m src.main
Seleccione opción 1
```

Para **Instagram**:
```bash
python -m src.main
Seleccione opción 2
```

### 4. Funcionamiento

- **Automatización de Login**: El script intentará hacer login en la plataforma seleccionada usando las credenciales proporcionadas.
- **Cookies de Sesión**: Después de un login exitoso, el script guardará las cookies en la carpeta `cookies/` para futuros inicios de sesión automáticos.
- **Simulación de Comportamiento Humano**: Se incluyen tiempos de espera aleatorios, movimientos de ratón, y desplazamientos (scroll) para evitar la detección como bot.

### 5. Modificaciones y Expansión

- Puedes agregar más funcionalidades de scraping en el futuro agregando nuevas funciones en los módulos `facebook/login.py` o `instagram/login.py`.
- Para evitar ser detectado como bot, puedes ajustar los tiempos de espera aleatorios y las interacciones humanas en el archivo `src/common/human_behavior.py`.

### 6. Seguridad y Buenas Prácticas

- **Uso de Variables de Entorno**: Las credenciales nunca deben estar hardcodeadas en el código. Utilizamos un archivo `.env` para manejar las credenciales de manera segura.
- **Manejo de Excepciones**: El código está preparado para manejar posibles errores de conexión o de elementos no encontrados en las páginas.
- **Cookies de Sesión**: Almacenar las cookies garantiza que el login sea automatizado sin requerir credenciales en cada ejecución.

---
