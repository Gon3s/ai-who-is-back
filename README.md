# ...existing code...

## Configuration de l'environnement

1. Copiez le fichier `.env.example` en `.env`:
```bash
cp .env.example .env
```

2. Modifiez le fichier `.env` avec vos paramètres:
- Remplacez `gsk_votre_cle_api_ici` par votre clé API Groq
- Ajustez les autres paramètres selon vos besoins (optionnel)

Les variables d'environnement disponibles sont:
- `AIWHO_API_KEY`: Votre clé API Groq (requis)
- `AIWHO_MODEL_NAME`: Le modèle à utiliser (optionnel)
- `AIWHO_TEMPERATURE`: La température pour la génération (optionnel)
- `AIWHO_MAX_TOKENS`: Le nombre maximum de tokens pour la réponse (optionnel)

# ...existing code...
