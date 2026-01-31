#!/bin/sh
set -e

ollama serve &

# Esperar a que ollama esté listo
sleep 5

echo "Descargando modelo phi3:mini..."
ollama pull phi3:mini

wait
