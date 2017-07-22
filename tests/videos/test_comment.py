import pytest
from model_mommy import mommy

from src.videos.models import Comment


@pytest.mark.django_db
class TestComment:
    '''
    Suite of tests for comments features
    '''

    @pytest.mark.parametrize('is_positive', [
        (True),
        (False),
    ])
    def test_comment_creation(
        self, client, is_positive,
    ):
        '''
        POST on /videos/comment/create/{video_pk}/ must create a comment
        '''

        # Create a video
        video = mommy.make('videos.Video')

        # Make the request
        resp = client.post(
            f'/videos/comment/create/{video.pk}/',
            {'is_positive': is_positive, 'message': 'Message about video.'},
        )

        # Check database state
        comment = Comment.objects.first()
        assert comment.is_positive == is_positive

        # Check status code
        assert resp.status_code == 302
