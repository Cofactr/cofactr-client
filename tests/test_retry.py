"""Test retry logic."""

# 3rd Party Modules
import httpx
import pytest
from tenacity import retry, wait_none

# Local Modules
from cofactr.graph import RetrySettings


class TestRetry:
    """Test retry logic."""

    retry_settings = RetrySettings()

    def test_succeeds_immediately(self):
        """Test succeeds immediately."""

        @retry(
            reraise=self.retry_settings.reraise,
            retry=self.retry_settings.retry,
            stop=self.retry_settings.stop,
            wait=self.retry_settings.wait,
        )
        def succeeds():
            """Retried function."""

            return

        succeeds()

        assert succeeds.retry.statistics["attempt_number"] == 1

    def test_fails_immediately(self):
        """Test fails immediately."""

        @retry(
            reraise=self.retry_settings.reraise,
            retry=self.retry_settings.retry,
            stop=self.retry_settings.stop,
            wait=self.retry_settings.wait,
        )
        def fails():
            """Retried function."""

            raise Exception()

        fails.retry.wait = wait_none()

        with pytest.raises(Exception):
            fails()

        assert fails.retry.statistics["attempt_number"] == 1

    def test_fails_and_then_succeeds(self, mocker):
        """Test fails and then succeeds."""

        mock = mocker.MagicMock(
            side_effect=[httpx.ConnectTimeout(message="Test"), True]
        )

        @retry(
            reraise=self.retry_settings.reraise,
            retry=self.retry_settings.retry,
            stop=self.retry_settings.stop,
            wait=self.retry_settings.wait,
        )
        def fails_and_then_succeeds():
            """Retried function."""

            mock()

        fails_and_then_succeeds.retry.wait = wait_none()

        fails_and_then_succeeds()

        assert fails_and_then_succeeds.retry.statistics["attempt_number"] == 2

    def test_fails_for_full_retry_period(self):
        """Test fails for full retry period."""

        @retry(
            reraise=self.retry_settings.reraise,
            retry=self.retry_settings.retry,
            stop=self.retry_settings.stop,
            wait=self.retry_settings.wait,
        )
        def fails():
            """Retried function."""

            raise httpx.ConnectTimeout(message="Test")

        fails.retry.wait = wait_none()

        with pytest.raises(httpx.ConnectTimeout):
            fails()

        assert fails.retry.statistics["attempt_number"] == 3
