from __future__ import annotations

NAV_LINKS = [
    ("Início", "website:home"),
    ("Serviços", "website:services"),
    ("Galeria", "website:gallery"),
    ("Comunidade", "website:community"),
    ("Mapa cultural", "website:cultural-map"),
    ("Admin", "website:admin-home"),
]

HOME_ARTISTS = [
    {
        "name": "DJ Oxente",
        "style": "Afrobeat / Manguebeat",
        "bio": "Pesquisa ritmos periféricos e transforma bailes comunitários em experiências sonoras imersivas.",
    },
    {
        "name": "Coletivo Aurora",
        "style": "Artes visuais",
        "bio": "Residência artística focada em muralismo e intervenções urbanas nos canais de Iputinga.",
    },
    {
        "name": "Banda Baronesa",
        "style": "Samba-reggae",
        "bio": "Formada por mulheres instrumentistas que levam oficinas musicais para escolas públicas.",
    },
]

HOME_EVENTS = [
    {
        "title": "Circuito Som na Rua",
        "date": "Sáb • 19h • Praça do Engenho",
        "description": "Line-up com 6 artistas independentes e feira de criadores.",
    },
    {
        "title": "Laboratório de Colaboração Musical",
        "date": "Qua • 14h • Estúdio Social",
        "description": "Sessão guiada por produtores para criar beats com instrumentos populares.",
    },
    {
        "title": "Vivência Mapa Cultural",
        "date": "Dom • 9h • Sede Iputinga",
        "description": "Cartografia afetiva, trilhas e registro de memórias do bairro.",
    },
]

SERVICES_TIPS = [
    {
        "title": "Crie seu catálogo",
        "items": [
            "Cadastre produtos físicos, experiências e formações.",
            "Defina slots de agenda para aluguel de estúdio.",
        ],
    },
    {
        "title": "Gerencie reservas",
        "items": [
            "O painel admin confirma, reagenda ou cancela solicitações.",
            "Pagamentos e status ficam sincronizados com o webhook do Stripe.",
        ],
    },
    {
        "title": "Amplifique campanhas",
        "items": [
            "Transforme serviços em recompensas para crowdfunding.",
            "Integre notificações via WhatsApp e e-mail comunitário.",
        ],
    },
]

GALLERY_COLLECTIONS = [
    {
        "title": "Encontros e eventos",
        "description": "Registros dos saraus, batalhas de rimas e festivais itinerantes.",
    },
    {
        "title": "Retratos de artistas",
        "description": "Ensaio autoral destacando instrumentos, oficinas e bastidores.",
    },
    {
        "title": "Intervenções urbanas",
        "description": "Grafites colaborativos nos muros da Beira Rio e painéis têxteis.",
    },
]

COMMUNITY_THREADS = [
    {
        "author": "Lia Moreira",
        "topic": "Chamado para voluntariado",
        "text": "Precisamos de fotógrafas para registrar o Circuito Som na Rua. Comentem disponibilidade!",
    },
    {
        "author": "Coletivo Aurora",
        "topic": "Moodboard mural 2025",
        "text": "Subimos o esboço do novo mural na rua Monsenhor Fabrício. Sugestões de paleta?",
    },
]

CROWDFUNDING_CAMPAIGNS = [
    {
        "title": "Estúdio móvel de podcast",
        "goal": "Meta R$ 45 mil",
        "progress": 0.62,
        "description": "Equipamentos itinerantes para registrar memórias e entrevistas nos territórios.",
    },
    {
        "title": "Residência artística Rio Doce",
        "goal": "Meta R$ 28 mil",
        "progress": 0.41,
        "description": "Manutenção de espaço compartilhado para artistas plásticos e cênicos.",
    },
]

CULTURAL_ZONES = [
    {
        "name": "Canal da Aurora",
        "highlights": [
            "Grafites mapeados via QR code",
            "Eco-trilha guiada com registros fotográficos",
        ],
    },
    {
        "name": "Baronesa",
        "highlights": [
            "Luthieria comunitária",
            "Biblioteca aberta e clube de leitura",
        ],
    },
]

GAMIFICATION_BADGES = [
    {
        "name": "Guardião da Memória",
        "criteria": "5 contribuições no mapa cultural",
    },
    {
        "name": "Produtor Solidário",
        "criteria": "3 campanhas apoiadas ou mentorias entregues",
    },
    {
        "name": "MC do Bairro",
        "criteria": "Organizou 2 eventos confirmados via plataforma",
    },
]

MUSIC_COLLAB_STEPS = [
    "Envie stems e referências diretamente do painel.",
    "Combine horários de estúdio com confirmação automática.",
    "Receba versões, feedbacks e arquivos finais no mesmo espaço.",
]

ADMIN_METRICS = {
    "bookings": 37,
    "pending_services": 4,
    "campaigns_live": 3,
    "artists_active": 58,
}
