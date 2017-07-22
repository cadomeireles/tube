import pytest
from model_mommy import mommy

from src.videos.models import Thumb


@pytest.mark.django_db
class TestThumb:
    '''
    Suite of tests for thumbs features
    '''

    @pytest.mark.parametrize('is_positive', [
        (True),
        (False),
    ])
    def test_thumb_creation(
        self, client, is_positive,
    ):
        '''
        POST on /videos/thumb/create/{video_pk}/ must create a thumb
        '''

        # Create a video
        video = mommy.make('videos.Video')

        # Make the request
        resp = client.post(
            f'/videos/thumb/create/{video.pk}/', {'is_positive': is_positive})

        # Check database state
        thumb = Thumb.objects.first()
        assert thumb.is_positive == is_positive

        # Check status code
        assert resp.status_code == 302
