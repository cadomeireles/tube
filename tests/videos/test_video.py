from datetime import datetime

import pytest
from dateutil.relativedelta import relativedelta
from model_mommy import mommy

from src.videos.models import Video


@pytest.mark.django_db
class TestVideo:
    '''
    Suite of tests for videos features
    '''

    # Dates
    today = datetime.now().date()
    one_year_ago = str(today - relativedelta(years=1))
    one_year_day_ago = str(today - relativedelta(years=1, days=1))

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

    @pytest.mark.parametrize('date_uploaded, successful, status_code', [
        (one_year_ago, True, 302),
        (one_year_day_ago, False, 200),
    ])
    def test_video_cdate(
        self, client, date_uploaded, successful, status_code, video_data,
    ):
        '''
        A theme cannot be saved if date uploaded is older than one year
        '''

        # Create themes and add PKs list to request data
        themes = mommy.make('videos.Theme', make_m2m=True, _quantity=3)
        video_data.update({'themes': [theme.pk for theme in themes]})

        # Change date
        video_data['date_uploaded'] = date_uploaded

        # Make the request
        resp = client.post('/videos/video/create/', video_data)

        # Check database state
        assert Video.objects.exists() == successful

        # Check status code
        assert resp.status_code == status_code
