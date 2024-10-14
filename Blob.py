import requests

def show_blob_message():
    """
    Zeigt die Nachricht 'Blob' auf der Konsole an.
    """
    print("Blob")

def send_blob_to_webhook(webhook_url):
    """
    Sendet die Nachricht 'Blob' an einen Webhook.

    Args:
        webhook_url: Die URL des Webhooks.
    """
    # Nachricht, die an den Webhook gesendet wird
    data = {
        'content': 'Blob'
    }

    # HTTP POST-Anfrage an den Webhook
    response = requests.post(webhook_url, json=data)

    if response.status_code == 200:
        print("Nachricht erfolgreich an den Webhook gesendet.")
    else:
        print(f"Fehler beim Senden der Nachricht: {response.status_code}, {response.text}")

# Webhook-URL hier eingeben
webhook_url = "https://discord.com/api/webhooks/1295464413821927516/Wlsp6qLBLCPDfOaAc4cvtSZbxwtZPCpvGOvDintnv38WH2p25XWvDRDzYKoZ11Vyrm4r"

# Zeige die 'Blob' Nachricht an
show_blob_message()

# Sende die 'Blob' Nachricht an den Webhook
send_blob_to_webhook(webhook_url)
