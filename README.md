# 🔐 Generador de Contraseñas Seguro (Python)

Este proyecto es un **generador de contraseñas seguro**, escrito en Python, diseñado para crear contraseñas fuertes y personalizables mediante una interfaz de consola clara y amigable.

Incluye:

- Selección de longitud predefinida  
- Inclusión opcional de minúsculas, mayúsculas, números y símbolos  
- Validación inteligente (evita configuraciones inválidas)  
- Generación segura usando `secrets`  
- Garantía de incluir al menos un carácter de cada categoría seleccionada  
- Interfaz visual limpia y consistente  

---

## 🚀 Características principales

### ✔️ Seguridad real
El generador utiliza el módulo `secrets`, recomendado para generar contraseñas criptográficamente seguras.

### ✔️ Contraseñas garantizadas
Si el usuario activa varias categorías (por ejemplo, números y símbolos), el programa garantiza que la contraseña final incluya **al menos un carácter de cada tipo**.

### ✔️ Interfaz visual clara
El programa muestra menús y mensajes con un estilo visual consistente:

- Encabezados con separadores  
- Mensajes de error amigables  
- Ajustes automáticos explicados  
- Contraseña resaltada con marco visual  

### ✔️ Validación estricta
El usuario no puede avanzar si ingresa valores inválidos.  
El programa corrige automáticamente configuraciones imposibles (por ejemplo, si elige “no” en todas las categorías).

---

## 📦 Requisitos

- Python 3.8 o superior

No requiere librerías externas.

---

## ▶️ Cómo ejecutar el programa

1. Clona este repositorio o descárgalo como ZIP.
2. Abre una terminal dentro de la carpeta del proyecto.
3. Entra a la carpeta `src`:

```bash
cd src
