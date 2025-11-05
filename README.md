# 🚀 Algoritmos de Ruta Más Corta - Bellman-Ford & Dijkstra

## 📍 Implementación de Algoritmos de Búsqueda de Rutas Óptimas

Una herramienta visual e interactiva para comparar y aplicar dos de los algoritmos más importantes en teoría de grafos: **Bellman-Ford** y **Dijkstra**.

## ✨ Características Principales

### 🔍 **Algoritmo de Bellman-Ford**
- **Aplicación**: Grafos con pesos negativos
- **Ventaja**: Detecta ciclos de peso negativo
- **Complejidad**: O(V*E)
- **Caso de uso**: Sistema de rutas con costos variables

### ⚡ **Algoritmo de Dijkstra**
- **Aplicación**: Grafos con pesos no negativos
- **Ventaja**: Más eficiente para grafos densos
- **Complejidad**: O(E + V log V)
- **Caso de uso**: Redes de transporte, navegación GPS

## 🛠️ Tecnologías Utilizadas

- **Python 3** - Lenguaje principal
- **NetworkX** - Manipulación y visualización de grafos
- **Matplotlib** - Visualización de grafos
- **Colorama** - Interfaz de colores en consola
- **Heapq** - Colas de prioridad para Dijkstra

## 📊 Visualizaciones Implementadas

### Para Bellman-Ford:
- 🕸️ Grafo dirigido con pesos positivos y negativos
- 📍 Nodos etiquetados con distancias
- 🎨 Diseño claro de la topología del grafo

### Para Dijkstra:
- 🗺️ Grafo de ruta con nodos START y FINISH
- 📏 Pesos no negativos en todas las aristas
- 🎯 Visualización de la ruta óptima

## 🚀 Cómo Ejecutar

```bash
python Python_Bellman_Ford_Dijkstra.py
```

## 🎮 Funcionalidades del Menú

1. **Bellman-Ford** - Para grafos con pesos negativos
2. **Dijkstra** - Para grafos con pesos no negativos  
3. **Salir** - Finalizar el programa

## 🔧 Características de Interfaz

### Entrada de Usuario:
- 🎯 Selección interactiva de nodo inicial y final
- ✅ Validación de entrada de datos
- 🔄 Manejo de errores robusto

### Resultados:
- 📋 Lista completa de todas las rutas posibles
- 🟢 Destacado de la ruta solicitada por el usuario
- ⚠️ Mensajes informativos para casos especiales

## 📈 Ejemplos de Aplicación

### Bellman-Ford:
- **Finanzas**: Arbitraje en tipos de cambio
- **Redes**: Enrutamiento con costos variables
- **Logística**: Optimización con descuentos y penalizaciones

### Dijkstra:
- **Transporte**: Navegación GPS y planificación de rutas
- **Redes**: Enrutamiento en redes de computadoras
- **Juegos**: Pathfinding en videojuegos

## 🎯 Resultados que Proporciona

### Para Cada Algoritmo:
- ✅ Costo mínimo entre nodos seleccionados
- ✅ Ruta específica a seguir
- ✅ Comparación con todas las rutas posibles
- ✅ Visualización gráfica del grafo

## ⚠️ Consideraciones Importantes

### Bellman-Ford:
- ❗ Detecta y reporta ciclos de peso negativo
- ⏱️ Menos eficiente para grafos grandes
- 📉 Funciona con pesos negativos

### Dijkstra:
- 🚫 No funciona con pesos negativos
- ⚡ Más rápido para grafos con pesos no negativos
- 🎯 Siempre encuentra la solución óptima en sus condiciones

---

**¡Herramienta esencial para entender y comparar algoritmos fundamentales de grafos!** 🌟

*Perfecto para estudiantes de ciencias de la computación, investigación de operaciones y análisis de redes*
