import os
from flask import Flask, render_template_string

app = Flask(__name__)

# Le code magique qui téléporte vers le nouveau site !
HTML_REDIRECT = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="2;url=https://pixel-ia-dev-1.onrender.com">
    <title>Redirection...</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; background: #0f0c20; color: white; text-align: center; padding-top: 100px; }
        .loader { color: #00d2ff; font-size: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h2>🤖 Ancienne version obsolète</h2>
    <p class="loader">Mise à niveau en cours... On t'amène vers la super IA v1.2.6 dans un instant ! ⚡</p>
    <p>Si la magie ne marche pas, <a href="https://pixel-ia-dev-1.onrender.com" style="color: #00ffaa;">clique ici</a>.</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_REDIRECT)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
