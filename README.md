#  Automatización de pruebas con Selenium para Urban Routes App

## 📌 Descripción

Proyecto de automatización de pruebas para la aplicación **Urban Routes**.
El proyecto utiliza **Python, Selenium y Pytest** para automatizar el proceso completo de solicitud de un taxi, desde la configuración de la ruta hasta la asignación de un conductor.

---

## 🎯 Objetivo

El objetivo del proyecto es verificar mediante pruebas automatizadas que el proceso de pedir un taxi funciona correctamente y que los diferentes elementos de la interfaz responden según lo esperado.

---

## 🧪 Casos de prueba automatizados

| # | Acción automatizada |
|---|---|
| 1 | Configurar la dirección de origen y destino |
| 2 | Seleccionar la tarifa Comfort |
| 3 | Rellenar el número de teléfono |
| 4 | Agregar una tarjeta de crédito |
| 5 | Escribir un mensaje para el conductor |
| 6 | Solicitar una manta y pañuelos |
| 7 | Solicitar 2 helados |
| 8 | Abrir el modal para buscar un taxi |
| 9 | Esperar a que aparezca la información del conductor en el modal |

---

## ⚙️ Funciones implementadas

Se implementaron métodos utilizando el patrón **Page Object Model (POM)** para interactuar con los elementos de Urban Routes.

Entre las principales funciones se encuentran:

- Configuración de la ruta.
- Selección de tarifa Comfort.
- Ingreso del número de teléfono.
- Confirmación del código telefónico.
- Agregar tarjeta de crédito.
- Ingreso del CVV.
- Cambio de foco del campo CVV.
- Ingreso del mensaje para el conductor.
- Activación de manta y pañuelos.
- Solicitud de 2 helados.
- Apertura del modal para pedir taxi.
- Espera de la información del conductor.

También se utilizó `WebDriverWait` con condiciones esperadas de Selenium para manejar elementos que aparecen dinámicamente.

---

## 📁 Estructura del proyecto

```text
qa-project-Urban-Routes-es/
├── .gitignore
├── README.md
├── requirements.txt
├── data.py
├── helpers.py
├── urban_routes_page.py
└── test_urban_routes.py
```

---

## 📚 Lo que aprendí

Durante el desarrollo de este proyecto aprendí y reforcé diferentes conceptos relacionados con la automatización de pruebas:

- Utilización de **Selenium WebDriver** para automatizar la interacción con una aplicación web.
- Creación de **localizadores** utilizando `ID`, `CSS Selector` y `XPath`.
- Validación de los localizadores para asegurarme de que sean únicos.
- Implementación del patrón **Page Object Model (POM)** para organizar los localizadores y métodos de la página.
- Implementación de métodos get, set y click para interactuar con los elementos de la aplicación.
- Utilización de **WebDriverWait** y `Expected Conditions` para trabajar con elementos que aparecen dinámicamente.
- Realizar las importaciones necesarias para la configuración y ejecución de las pruebas automatizadas.
- Uso de **Pytest** para ejecutar y validar pruebas automatizadas.
- Uso de **Git y GitHub** para versionar y documentar el proyecto.


## Tecnologías utilizadas
Python 3.12.6
pytest 9.1.1
Selenium 4.46.0
Git
GitHub
Visual Studio Code