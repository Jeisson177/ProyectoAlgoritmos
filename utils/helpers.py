def mostrar_mensaje(mensaje, tipo="info"):
    """Muestra mensajes formateados según su tipo"""
    formatos = {
        "error": "⚠️ Error: {}",
        "exito": "✅ {}",
        "info": "ℹ️ {}",
        "advertencia": "⚠️ {}"
    }
    print(formatos.get(tipo, "{}").format(mensaje))