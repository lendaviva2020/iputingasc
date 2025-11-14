from collections import defaultdict
from typing import Any, Dict, List

from django.views.generic import TemplateView

from apps.gallery.models import GalleryImage
from apps.services.models import Service, ServiceCategory

from .content import (
    ADMIN_METRICS,
    COMMUNITY_THREADS,
    CROWDFUNDING_CAMPAIGNS,
    CULTURAL_ZONES,
    GALLERY_COLLECTIONS,
    GAMIFICATION_BADGES,
    HOME_ARTISTS,
    HOME_EVENTS,
    MUSIC_COLLAB_STEPS,
    NAV_LINKS,
    SERVICES_TIPS,
)


class BasePageView(TemplateView):
    page_title = "Iputinga Social e Cultural"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.page_title
        context["nav_links"] = NAV_LINKS
        return context


class HomePageView(BasePageView):
    template_name = "pages/home.html"
    page_title = "Bem-vindo · Iputinga Social e Cultural"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "artists": HOME_ARTISTS,
                "events": HOME_EVENTS,
                "hero_text": "Descubra a cena cultural vibrante de Iputinga. Conecte-se com artistas locais, participe de eventos e fortaleça iniciativas solidárias.",
                "metrics": [
                    {"label": "artistas ativos", "value": "58+"},
                    {"label": "eventos mapeados", "value": "120"},
                    {"label": "campanhas financiadas", "value": "24"},
                ],
            }
        )
        return context


class ServicesPageView(BasePageView):
    template_name = "pages/services.html"
    page_title = "Serviços"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        services = (
            Service.objects.select_related("category")
            .filter(is_active=True)
            .order_by("category__name", "title")
        )
        grouped: Dict[str, List[Service]] = defaultdict(list)
        for service in services:
            key = service.category.name if service.category else "Outros"
            grouped[key].append(service)
        context.update(
            {
                "service_groups": grouped,
                "has_services": services.exists(),
                "service_tips": SERVICES_TIPS,
                "categories": ServiceCategory.objects.all(),
            }
        )
        return context


class GalleryPageView(BasePageView):
    template_name = "pages/gallery.html"
    page_title = "Galeria"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        gallery_items = GalleryImage.objects.filter(is_published=True)[:9]
        context.update(
            {
                "gallery_items": gallery_items,
                "collections": GALLERY_COLLECTIONS,
                "fallback_items": [
                    {
                        "title": "Circuito Som na Rua",
                        "description": "Registro do palco colaborativo montado na Beira Rio.",
                        "static_path": "img/artist-1.jpg",
                    },
                    {
                        "title": "Residência Aurora",
                        "description": "Processo do mural coletivo no Canal da Aurora.",
                        "static_path": "img/artist-2.jpg",
                    },
                    {
                        "title": "Laboratório musical",
                        "description": "Sessão de beatmaking com instrumentos populares.",
                        "static_path": "img/artist-3.jpg",
                    },
                ],
            }
        )
        return context


class ProfilePageView(BasePageView):
    template_name = "pages/profile.html"
    page_title = "Perfil do Cliente"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["profile_sections"] = [
            {
                "title": "Minhas reservas",
                "description": "Acompanhe status de estúdio, mentorias e oficinas confirmadas.",
            },
            {
                "title": "Campanhas apoiadas",
                "description": "Recibos e recompensas digitais ficam disponíveis aqui.",
            },
            {
                "title": "Certificados",
                "description": "Baixe declarações de participação em cursos e residências.",
            },
        ]
        return context


class AuthPageView(BasePageView):
    template_name = "pages/auth.html"
    page_title = "Autenticação"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["auth_steps"] = [
            "Crie sua conta para reservar serviços e publicar na comunidade.",
            "Ative o perfil de artista para acessar o painel administrativo.",
            "Habilite 2FA e receba alertas sobre movimentações financeiras.",
        ]
        return context


class CheckoutPageView(BasePageView):
    template_name = "pages/checkout.html"
    page_title = "Checkout"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["checkout_steps"] = [
            {
                "title": "Resumo do serviço",
                "details": "Confirme duração, equipamento e custo.",
            },
            {
                "title": "Pagamento seguro",
                "details": "Stripe com confirmação instantânea e PIX.",
            },
            {
                "title": "Status em tempo real",
                "details": "Webhook retorna recibo e atualiza a reserva.",
            },
        ]
        return context


class CommunityPageView(BasePageView):
    template_name = "pages/community.html"
    page_title = "Comunidade"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["threads"] = COMMUNITY_THREADS
        context["engagement_stats"] = [
            ("Posts ativos", "312"),
            ("Voluntários cadastrados", "94"),
            ("Editais compartilhados", "38"),
        ]
        return context


class CommunityVotingPageView(BasePageView):
    template_name = "pages/community_voting.html"
    page_title = "Votações"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["polls"] = [
            {
                "title": "Agenda colaborativa 2025",
                "description": "Escolha as prioridades para o circuito Som na Rua.",
                "deadline": "Votação até 12/12",
            },
            {
                "title": "Residência artística Baronesa",
                "description": "Seleção de propostas para murais e ocupações.",
                "deadline": "Resultado em 05/01",
            },
        ]
        return context


class CrowdfundingPageView(BasePageView):
    template_name = "pages/crowdfunding.html"
    page_title = "Crowdfunding"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        campaigns = []
        for campaign in CROWDFUNDING_CAMPAIGNS:
            data = campaign.copy()
            data["percent"] = int(data["progress"] * 100)
            campaigns.append(data)
        context["campaigns"] = campaigns
        return context


class CulturalMapPageView(BasePageView):
    template_name = "pages/cultural_map.html"
    page_title = "Mapa Cultural"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["zones"] = CULTURAL_ZONES
        return context


class GamificationPageView(BasePageView):
    template_name = "pages/gamification.html"
    page_title = "Gamificação"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["badges"] = GAMIFICATION_BADGES
        return context


class MusicCollaborationPageView(BasePageView):
    template_name = "pages/music_collaboration.html"
    page_title = "Laboratório Musical"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["workflow_steps"] = MUSIC_COLLAB_STEPS
        return context


class AdminDashboardPageView(BasePageView):
    template_name = "pages/admin/dashboard.html"
    page_title = "Admin · Dashboard"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["metrics"] = ADMIN_METRICS
        context["recent_activity"] = [
            "Nova campanha 'Residência Rio Doce' cadastrada",
            "Reserva do Estúdio Social confirmada para 12/11",
            "3 novos artistas aguardando aprovação de perfil",
        ]
        return context


class AdminLandingPageView(BasePageView):
    template_name = "pages/admin/index.html"
    page_title = "Admin · Hub"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["admin_shortcuts"] = [
            ("Serviços e produtos", "website:admin-services"),
            ("Eventos e agenda", "website:admin-events"),
            ("Artistas e coletivos", "website:admin-artists"),
            ("Campanhas de financiamento", "website:crowdfunding"),
        ]
        return context


class AdminServicesPageView(BasePageView):
    template_name = "pages/admin/services.html"
    page_title = "Admin · Serviços"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pending_services = (
            Service.objects.filter(is_active=False)
            .select_related("category")
            .order_by("title")
        )
        context["pending_services"] = pending_services
        return context


class AdminEventsPageView(BasePageView):
    template_name = "pages/admin/events.html"
    page_title = "Admin · Eventos"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["events_pipeline"] = [
            {
                "name": "Festival Som na Rua",
                "status": "Aguardando licença",
                "next_step": "Enviar documentação à PCR",
            },
            {
                "name": "Oficina de beatmaking",
                "status": "Confirmado",
                "next_step": "Divulgar convocatória",
            },
        ]
        return context


class AdminArtistsPageView(BasePageView):
    template_name = "pages/admin/artists.html"
    page_title = "Admin · Artistas"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["artist_requests"] = [
            {
                "name": "Coletivo Cais do Barro",
                "focus": "esculturas em barro + oficinas infantis",
                "needs": "Acesso ao estúdio e agenda de mentorias",
            },
            {
                "name": "DJ Liane",
                "focus": "mixagens afrocaribenhas",
                "needs": "Certificação de oficina + slot nos eventos",
            },
        ]
        return context


class NotFoundPageView(BasePageView):
    template_name = "pages/not_found.html"
    page_title = "Página não encontrada"


def not_found_view(request, exception):
    response = NotFoundPageView.as_view()(request)
    response.status_code = 404
    return response
