# TODOS

| Prioridade | Item | Responsável sugerido |
|------------|------|----------------------|
| Alta | Restringir `ServiceViewSet` e `GalleryImageViewSet` a staff e criar testes de permissão | Backend |
| Alta | Implementar fluxo de refresh/rotação de tokens (ex.: JWT) e atualizar o frontend | Backend / Frontend |
| Alta | Aplicar `python manage.py migrate` em todos os ambientes e garantir execução em pipelines | DevOps |
| Alta | Integrar Stripe metadata para associar `Payment.booking` e atualizar status das reservas | Backend (Pagamentos) |
| Média | Envolver chamadas WhatsApp com `try/except` e mover envio para Celery | Backend / DevOps |
| Média | Validar `service.is_active` no serializer de `Booking` e adicionar testes cobrindo o cenário | Backend |
| Média | Documentar ou remover dependências Celery/Storage não configuradas; adicionar `Procfile` para workers se necessário | DevOps |
| Média | Expandir suíte de testes (payments, notificações, admin bookings, templates) | QA / Backend |
| Baixa | Condicionar flags `SECURE_*` e HSTS ao modo produção e atualizar `.env.example` | Backend |

