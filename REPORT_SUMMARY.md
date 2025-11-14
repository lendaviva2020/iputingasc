# REPORT_SUMMARY

## Top 10 Issues
1. Serviços e categorias podem ser alterados por qualquer usuário autenticado (`apps/services/views.py`).
2. CMS da galeria exposto sem permissão administrativa (`apps/gallery/views.py`).
3. Webhook do Stripe não vincula pagamentos às reservas (`apps/payments/views.py`).
4. Ausência de endpoint de refresh/rotação de tokens (`apps/accounts/views.py`).
5. Cobertura de testes restrita a 3 cenários básicos (`tests/`).
6. Migrações ainda não aplicadas em nenhum ambiente (`apps/*/migrations`).
7. Falhas de rede no WhatsApp derrubam o request (`apps/notifications/services.py`).
8. Reservas aceitam serviços desativados (`apps/bookings/serializers.py`).
9. Dependências de Celery/Storage instaladas porém sem configuração (`requirements.txt`, `iputingasc/settings.py`).
10. Flags HSTS/SECURE ativas mesmo com `DEBUG=True` (`iputingasc/settings.py`).

## Próximas ações imediatas
- Bloquear métodos de escrita em serviços e galeria apenas para staff.
- Definir estratégia de tokens (ex.: JWT com refresh) e atualizar clientes.
- Aplicar `python manage.py migrate` e configurar pipelines para não executar app sem banco migrado.
- Mapear metadados do Stripe para atualizar `Payment.booking` e status das reservas.
- Adicionar suíte mínima de testes para auth, bookings (transições), Stripe webhook e WhatsApp mockado.
- Documentar/remover dependências não usadas (Celery, storage) para evitar falsas expectativas.

## Comandos executados durante a auditoria
```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python manage.py check
.venv\Scripts\python manage.py makemigrations
.venv\Scripts\python manage.py makemigrations --dry-run
.venv\Scripts\python manage.py migrate --plan
# runserver smoke-test (finalizado após 5s)
.venv\Scripts\python manage.py runserver --noreload
.venv\Scripts\python -m pytest --maxfail=1 --disable-warnings -q
.venv\Scripts\ruff check .
.venv\Scripts\python -m black --check .
.venv\Scripts\python -m isort --check-only .
```

