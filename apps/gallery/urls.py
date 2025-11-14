from rest_framework.routers import DefaultRouter

from .views import GalleryImageViewSet

router = DefaultRouter()
router.register("", GalleryImageViewSet, basename="gallery")

urlpatterns = router.urls
