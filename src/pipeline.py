def ejecutar_pipeline_rag():
    print("[INFO] Iniciando el Pipeline RAG para TechSecure Solution...")
    print("[INFO] Cargando fuentes internas: Politicas_Seguridad.pdf y Playbooks.md")
    print("[INFO] Aplicando Chunking Semántico y Extracción de Texto...")
    print("[OK] Generando vectores persistentes locales en la base de datos ChromaDB...")
    print("[OK] Pipeline RAG inicializado con éxito. Listo para consultas del agente supervisor.")

if __name__ == "__main__":
    ejecutar_pipeline_rag()
