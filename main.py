import argparse

def buscar_activo_en_inventario(software_alerta):
    # Simulación de la base de datos de TechSecure
    inventario_clientes = [
        {"host": "srv-produccion-web", "ip": "192.168.1.50", "software": "Apache httpd", "version": "2.4.41", "entorno": "DMZ"},
        {"host": "srv-desarrollo-bd", "ip": "10.0.2.15", "software": "PostgreSQL", "version": "12.1", "entorno": "Desarrollo"}
    ]
    for activo in inventario_clientes:
        if activo["software"].lower() in software_alerta.lower():
            return activo
    return None

def ejecutar_triaje_agente(cve_id, software_alerta):
    print(f"\n--- [AGENTE SUPERVISOR] PROCESANDO ALERTA: {cve_id} ---")
    activo_afectado = buscar_activo_en_inventario(software_alerta)

    if not activo_afectado:
        print("[SALIDA AGENTE]: Falso Positivo - El software reportado no está activo en ningún cliente.")
        return

    print(f"[OK] Activo vulnerable detectado: {activo_afectado['host']} ({activo_afectado['ip']}) en entorno {activo_afectado['entorno']}.")

    # Lógica basada en el entorno del cliente
    if activo_afectado["entorno"] == "DMZ":
        prioridad_final = "CRÍTICA / INMEDIATA"
    else:
        prioridad_final = "MEDIA"

    print("\n========================================================")
    print(f"🔴 REPORTE TÉCNICO PRIORIZADO - TECHSECURE SOLUTIONS")
    print("========================================================")
    print(f"Identificador: {cve_id}")
    print(f"Host Afectado: {activo_afectado['host']} ({activo_afectado['ip']})")
    print(f"Prioridad Recalculada: {prioridad_final}")
    print(f"Origen de la Regla: [Fuente: Politica_Seguridad_TechSecure.pdf]")
    print("--------------------------------------------------------")
    print(f"📝 PLAN DE MITIGACIÓN SUGERIDO (LENGUAJE NATURAL):")
    print(f"Se ha detectado {cve_id} afectando al servicio {software_alerta} en producción.")
    print(f"Acción recomendada: Actualizar paquete mediante gestor oficial o aplicar regla de Firewall perimetral.")
    print("========================================================\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Agente de Triaje de Vulnerabilidades - TechSecure")
    parser.add_argument("--cve", default="CVE-2024-1234", help="ID de la vulnerabilidad")
    parser.add_argument("--software", default="Apache httpd", help="Software afectado")
    args = parser.parse_args()
    ejecutar_triaje_agente(args.cve, args.software)
