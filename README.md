# TechSecure Solution: Agente RAG para Triaje Dinámico de Vulnerabilidades

Este repositorio contiene el código fuente, la configuración del pipeline RAG y la arquitectura de agentes inteligentes diseñada para automatizar el triaje, priorización y generación de reportes de mitigación ante alertas de seguridad (CVE).

La solución optimiza los tiempos de respuesta del SOC, reduciendo hasta en un 40% el análisis manual y entregando planes de acción adaptados a las políticas de cada cliente en menos de 2 minutos.

**Requisitos Técnicos e Infraestructura**

El sistema está desarrollado en Python y utiliza frameworks modernos de orquestación de IA para garantizar el aislamiento de datos y el cumplimiento de normativas de privacidad (ISO 27001).

- **Lenguaje:** Python 3.10+
- **Orquestación de Agentes:** LangChain / CrewAI
- **Base de Datos Vectorial:** ChromaDB (Local y persistente)
- **Modelos de Lenguaje:** LLM Local o API Comercial con políticas empresariales de No Retención de Datos (ZDR).

**Instrucciones de Instalación y Configuración**

Siga estos pasos para replicar el entorno técnico y validar el funcionamiento del sistema:

# 1. Clonar el repositorio
```bash
git clone https://github.com/Bronboiii/agente-rag-techsecure.git
cd agente-rag-techsecure

```
# 2. Crear el entorno virtual
```
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```
# 3. Instalacion dependencias
```
pip install -r requirements.txt
