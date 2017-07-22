import pytest

from src.videos.models import Theme


@pytest.mark.django_db
class TestTheme:
    '''
    Suite of tests for themes features
    '''

    @pytest.mark.parametrize('uses_data, successful, status_code', [
        (True, True, 302),
        (False, False, 200),
    ])
    def test_theme_creation(
        self, client, uses_data, successful, status_code, theme_data,
    ):
        """
        POST with correct data on /videos/theme/create/ must create a theme
        """
        data = theme_data if uses_data else {}

        # Make the request
        resp = client.post('/videos/theme/create/', data)

        # Check database state
        assert Theme.objects.exists() == successful

        # Check status code
        assert resp.status_code == status_code
