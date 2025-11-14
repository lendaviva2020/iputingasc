from django.urls import path

from .views import (
    AdminArtistsPageView,
    AdminDashboardPageView,
    AdminEventsPageView,
    AdminLandingPageView,
    AdminServicesPageView,
    AuthPageView,
    CheckoutPageView,
    CommunityPageView,
    CommunityVotingPageView,
    CrowdfundingPageView,
    CulturalMapPageView,
    GalleryPageView,
    GamificationPageView,
    HomePageView,
    MusicCollaborationPageView,
    NotFoundPageView,
    ProfilePageView,
    ServicesPageView,
)

app_name = "website"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("services/", ServicesPageView.as_view(), name="services"),
    path("gallery/", GalleryPageView.as_view(), name="gallery"),
    path("profile/", ProfilePageView.as_view(), name="profile"),
    path("auth/", AuthPageView.as_view(), name="auth"),
    path("checkout/", CheckoutPageView.as_view(), name="checkout"),
    path("community/", CommunityPageView.as_view(), name="community"),
    path(
        "community/voting/", CommunityVotingPageView.as_view(), name="community-voting"
    ),
    path("crowdfunding/", CrowdfundingPageView.as_view(), name="crowdfunding"),
    path("cultural-map/", CulturalMapPageView.as_view(), name="cultural-map"),
    path("gamification/", GamificationPageView.as_view(), name="gamification"),
    path(
        "music-collaboration/",
        MusicCollaborationPageView.as_view(),
        name="music-collaboration",
    ),
    path("admin/", AdminLandingPageView.as_view(), name="admin-home"),
    path("admin/dashboard/", AdminDashboardPageView.as_view(), name="admin-dashboard"),
    path("admin/services/", AdminServicesPageView.as_view(), name="admin-services"),
    path("admin/events/", AdminEventsPageView.as_view(), name="admin-events"),
    path("admin/artists/", AdminArtistsPageView.as_view(), name="admin-artists"),
    path("404/", NotFoundPageView.as_view(), name="not-found"),
]
