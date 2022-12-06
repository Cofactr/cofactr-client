"""Test GraphAPI retry logic."""
# Standard Modules
from pathlib import Path
import pickle

# 3rd Party Modules
from deepdiff import DeepDiff
from dotenv import dotenv_values
import httpx
import pytest
from tenacity import wait_none

# Local Modules
from cofactr.graph import GraphAPI
from cofactr.schema import OfferSchemaName, ProductSchemaName

CONFIG = dotenv_values(Path(__file__).parent / "../.env.test")

CLIENT_ID = CONFIG["CLIENT_ID"]
API_KEY = CONFIG["API_KEY"]


class TestGraphAPIRetry:
    """Test GraphAPI retry logic."""

    graph = GraphAPI(client_id=CLIENT_ID, api_key=API_KEY)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "test_case,method,kwargs,expected_result,attempt_number",
        [
            (
                "succeeds_immediately",
                graph.get_products_by_ids,
                {
                    "ids": [
                        "CCI8TPV75AW2",
                        "CCEEPYIYIALK",
                        "CCV1F7A8UIYH",
                        "INY4PO7KBQNY",
                    ],
                    "external": False,
                    "schema": ProductSchemaName.FLAGSHIP_V3,
                },
                pickle.load(
                    open(
                        Path(__file__).parent
                        / "./data/test_graph_retry/get_products_by_ids.pkl",
                        "rb",
                    )
                ),
                1,
            ),
            (
                "reraises_exceptions_for_full_retry_period",
                graph.get_offers,
                {
                    "product_id": "invalid_cpid",
                    "external": False,
                    "schema": OfferSchemaName.FLAGSHIP,
                },
                httpx.HTTPStatusError,
                graph.retry_settings.stop.max_attempt_number,
            ),
        ],
    )
    def test_graphapi_retry(
        self, test_case, method, kwargs, expected_result, attempt_number
    ):
        """Test GraphAPI retry logic."""

        if test_case == "succeeds_immediately":
            response = method(**kwargs)
            assert not DeepDiff(t1=expected_result, t2=response)
        elif test_case == "reraises_exceptions_for_full_retry_period":
            method.retry.wait = wait_none()

            with pytest.raises(expected_result):
                method(**kwargs)

        assert method.retry.statistics["attempt_number"] == attempt_number
