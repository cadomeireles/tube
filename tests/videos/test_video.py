import pytest
from model_mommy import mommy

from src.videos.models import Video


@pytest.mark.django_db
class TestVideo:
    '''
    Suite of tests for videos features
    '''

    @pytest.mark.parametrize('uses_data, successful, status_code', [
        (True, True, 302),
        (False, False, 200),
    ])
    def test_video_creation(
        self, client, uses_data, successful, status_code, video_data,
    ):
        """
        POST with correct data on /videos/video/create/ must create a video
        """
        data = video_data if uses_data else {}

        if uses_data:
            # Create themes and add PKs list to request data
            themes = mommy.make('videos.Theme', make_m2m=True, _quantity=3)
            data.update({'themes': [theme.pk for theme in themes]})

        # Make the request
        resp = client.post('/videos/video/create/', data)

        # Check database state
        assert Video.objects.exists() == successful

        # Check status code
        assert resp.status_code == status_code
