# AUDIT_ISSUES

Cada item lista severidade, arquivos afetados, evidências e recomendação.

## CRITICAL

1. **Catálogo de serviços exposto para escrita por qualquer usuário autenticado**
   - Arquivos: `apps/services/views.py`
   - Evidência: `ServiceViewSet` e `ServiceCategoryViewSet` usam `IsAuthenticatedOrReadOnly`, permitindo que qualquer usuário logado crie/edite/exclua serviços e categorias administrativas.
   - Impacto: Usuários comuns podem alterar preços, descrições e categorias sem aprovação, comprometendo operações e receita.
   - Ação: Restringir métodos de escrita a `IsAdminUser` (ou permissão customizada) e manter `AllowAny` apenas para leitura pública.

2. **CMS de galeria sem controle administrativo**
   - Arquivos: `apps/gallery/views.py`
   - Evidência: `GalleryImageViewSet` também usa `IsAuthenticatedOrReadOnly`, permitindo upload/alteração de imagens por qualquer usuário autenticado.
   - Impacto: Risco de conteúdo inapropriado ou malicioso publicado na galeria pública.
   - Ação: Aplicar permissão restrita (ex.: `IsAdminUser`) para `create/update/destroy` e mover uploads para fluxo moderado.

## HIGH

3. **Stripe webhook não reconcilia reservas**
   - Arquivos: `apps/payments/views.py`
   - Evidência: `handle_stripe_event()` apenas cria/atualiza `Payment` sem associar `booking` ou atualizar status da reserva.
   - Impacto: Pagamentos ficam sem vínculo com reservas, impedindo automação de confirmação/cancelamento financeiro.
   - Ação: Enviar `booking_id` em `metadata` nas intents e, no webhook, localizar a reserva para atualizar status e campo `booking`.

4. **Fluxo de autenticação sem refresh/rotação de token**
   - Arquivos: `apps/accounts/views.py`, `apps/accounts/urls.py`
   - Evidência: Há endpoints de `register`, `login` e `me`, porém não existe endpoint para refresh/rotina de expiração apesar do requisito.
   - Impacto: Tokens permanentes (`TokenAuthentication`) não podem ser rotacionados, elevando risco em caso de vazamento.
   - Ação: Adotar JWT (ex.: `SimpleJWT`) ou implementar endpoint de refresh/blacklist, documentando tempo de expiração.

5. **Cobertura de testes insuficiente para fluxos críticos**
   - Arquivos: `tests/`
   - Evidência: Apenas 3 testes (health, registro e criação básica de booking). Não há testes para pagamentos, notificações, serviços, admin actions ou erros.
   - Impacto: Regressões em endpoints críticos passarão despercebidas; não há validação de permissões.
   - Ação: Priorizar suíte cobrindo auth, transições de booking, webhook Stripe, WhatsApp mockado e permissões admin.

6. **Migrações pendentes não aplicadas em nenhum ambiente**
   - Arquivos: `apps/*/migrations/0001_initial.py`
   - Evidência: `python manage.py migrate --plan` lista todas as operações pendentes; `db.sqlite3` não está migrado.
   - Impacto: Sem `migrate`, tabelas inexistem e o servidor quebra ao tentar acessar banco.
   - Ação: Rodar `python manage.py migrate` (idealmente em pipelines) e versionar o estado do banco apenas via migrations.

## MEDIUM

7. **Envio WhatsApp pode quebrar requisição ao falhar rede**
   - Arquivos: `apps/notifications/services.py`
   - Evidência: Chamada `requests.post` não está envolvida em `try/except`, logo `RequestException` gera 500 antes de registrar log/estado.
   - Impacto: Operador não recebe feedback amigável e o serviço cai em falhas transientes de rede.
   - Ação: Envolver request em `try/except`, marcar log como `FAILED` e retornar erro amigável; idealmente delegar ao Celery.

8. **Reservas aceitam serviços inativos**
   - Arquivos: `apps/bookings/serializers.py`
   - Evidência: `validate_scheduled_for` existe, porém não há validação que o `service` esteja `is_active=True`.
   - Impacto: Clientes conseguem agendar serviços que foram desativados/cancelados.
   - Ação: Adicionar validação antes de salvar e emitir erro claro quando o serviço estiver inativo ou `None`.

9. **Dependências de Celery/Storage sem configuração**
   - Arquivos: `requirements.txt`, `iputingasc/settings.py`
   - Evidência: Pacotes `celery`, `redis`, `django-storages` e var `STORAGE_BUCKET_URL` estão presentes, porém não há configuração de broker, backend, nem `DEFAULT_FILE_STORAGE`.
   - Impacto: Equipe pode assumir que filas e storage já estão prontos; chamadas a features inexistentes lançarão exceções em runtime.
   - Ação: Remover deps não usadas ou adicionar configuração/documentação de como habilitar (broker URL, tasks, storage backend).

## LOW

10. **Flags de segurança ativas mesmo em desenvolvimento**
    - Arquivos: `iputingasc/settings.py`
    - Evidência: `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_SSL_REDIRECT` são aplicados independentemente do `DEBUG`, o que quebra navegação local sem HTTPS.
    - Impacto: Novos contribuidores podem enfrentar redirects infinitos ou mensagens HSTS ao testar localmente.
    - Ação: Envolver flags em condicionais (`if not DEBUG`) e documentar variáveis necessárias para produção.

