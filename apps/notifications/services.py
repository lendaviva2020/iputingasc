import logging
from typing import Any, Dict

import requests
from django.conf import settings

from .models import NotificationLog

logger = logging.getLogger("iputingasc.notifications")


def send_whatsapp_message(recipient: str, message: str) -> NotificationLog:
    log = NotificationLog.objects.create(
        channel=NotificationLog.Channel.WHATSAPP,
        recipient=recipient,
        payload={"message": message},
    )
    api_token = getattr(settings, "WHATSAPP_API_TOKEN", None)
    phone_id = getattr(settings, "WHATSAPP_PHONE_ID", None)
    if not api_token or not phone_id:
        log.status = NotificationLog.Status.FAILED
        log.error_message = "Credenciais do WhatsApp ausentes."
        log.save(update_fields=("status", "error_message", "updated_at"))
        logger.error("WhatsApp credentials missing")
        return log

    url = f"https://graph.facebook.com/v18.0/{phone_id}/messages"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json",
    }
    payload: Dict[str, Any] = {
        "messaging_product": "whatsapp",
        "to": recipient,
        "type": "text",
        "text": {"body": message},
    }

    response = requests.post(url, headers=headers, json=payload, timeout=15)
    if response.ok:
        data = response.json()
        log.status = NotificationLog.Status.SENT
        log.provider_message_id = data.get("messages", [{}])[0].get("id", "")
        log.save(update_fields=("status", "provider_message_id", "updated_at"))
    else:
        log.status = NotificationLog.Status.FAILED
        log.error_message = response.text
        log.save(update_fields=("status", "error_message", "updated_at"))
        logger.error("WhatsApp API error: %s", response.text)

    return log
