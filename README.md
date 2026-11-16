# Diseño e implementación de filtros digitales

## Descripción del proyecto

Este proyecto tiene como objetivo diseñar e implementar filtros digitales pasa bajos, pasa altos y pasa bandas utilizando Python. Se emplean las bibliotecas NumPy, SciPy y Matplotlib para generar señales, agregar ruido, aplicar filtros y visualizar los resultados.

## Objetivos

- Generar una señal compuesta por diferentes frecuencias.
- Agregar ruido blanco para simular una señal contaminada.
- Diseñar filtros digitales IIR de tipo Butterworth.
- Comparar las señales antes y después del filtrado.
- Analizar la respuesta en frecuencia de cada filtro.

## Filtros implementados

**Filtro pasa bajos:** utiliza una frecuencia de corte de 20 Hz para conservar principalmente las frecuencias bajas.

**Filtro pasa altos:** utiliza una frecuencia de corte de 40 Hz para conservar principalmente las frecuencias altas.

**Filtro pasa bandas:** permite el paso de frecuencias entre 40 y 80 Hz.

Los filtros son de orden 4 y se utiliza una frecuencia de muestreo de 1000 Hz.

## Requisitos

- Python 3.14
- NumPy
- SciPy
- Matplotlib

## Instalación

Instalar las bibliotecas necesarias con el siguiente comando:

```bash
uv pip install --python .venv\Scripts\python.exe numpy scipy matplotlib
```

## Ejecución

Desde la terminal de PowerShell, ejecutar:

```powershell
.\.venv\Scripts\python.exe filtros_digitales.py
```

## Resultados

El programa genera gráficas para comparar la señal limpia, la señal con ruido y las señales filtradas. También muestra la respuesta en frecuencia de los filtros y calcula el valor RMS de las señales para facilitar su análisis.

Los archivos gráficos generados son:

- `comparacion_senales.png`
- `respuesta_frecuencia.png`

## Conclusión

El proyecto permite observar cómo los filtros digitales seleccionan determinadas bandas de frecuencia y atenúan otras. La respuesta obtenida depende del tipo de filtro y de sus frecuencias de corte. Estas herramientas son útiles para el procesamiento de señales y la reducción de ruido.

## Tecnologías utilizadas

- Python
- NumPy
- SciPy
- Matplotlib
- Git y GitHub
