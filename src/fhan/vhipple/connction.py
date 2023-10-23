from typing import Optional
from requests import Session

from fhan.client.utils.http_utils import (
    join_urls,
    _make_get_request,
    make_post_request,
    make_put_request,
)
from fhan.models.R4 import Bundle
from fhan.vhipple.schema import Dataset


class VhippleConnection(object):
    endpoints = {
        "get_datasets": "datasets/",
        "create_empty_dataset": "datasets/",
        "add_bundles": "datasets/{id}/add-bundles/",
    }

    def __init__(self):
        self.session = Session()

    def connect(self):
        self.vhipple_url = "http://localhost:8000/api/v1"

    def close(self):
        pass

    def _get(self, endpoint, params=None):
        url = join_urls(self.vhipple_url, endpoint)
        return _make_get_request(url, session=self.session, params=params)

    def _post(self, endpoint, data=None, headers=None):
        url = join_urls(self.vhipple_url, endpoint)
        return make_post_request(url, session=self.session, data=data, headers=headers)

    def _put(self, endpoint, data=None, headers=None):
        url = join_urls(self.vhipple_url, endpoint)
        return make_put_request(url, session=self.session, data=data, headers=headers)

    def create_empty_dataset(self, name: str, description: Optional[str]):
        dataset = {
            "name": name,
            "description": description,
        }
        response = self._post(self.endpoints["create_empty_dataset"], data=dataset)
        res_dataset = Dataset(**response.json())
        return res_dataset

    def list_datasets(self, skip=0, limit=100):
        params = {"skip": skip, "limit": limit}
        response = self._get(self.endpoints["get_datasets"], params=params)
        return response.json()

    def add_bundles_to_dataset(self, dataset_id: int, bundles: list[Bundle]):
        response = self._put(
            self.endpoints["add_bundles"].format(id=dataset_id), data=bundles
        )
        return response.json()


if __name__ == "__main__":
    import json

    con = VhippleConnection()
    con.connect()
    with open(
        "/Users/tillrostalski/Git/old_whipple/oldwebapp/server/data/synthea_1/synthea_sample_data_fhir_r4_sep2019/Aaron697_Stiedemann542_41166989-975d-4d17-b9de-17f94cb3eec1.json"
    ) as f:
        bundle = json.load(f)
        dataset = con.create_empty_dataset("test", "test")
        con.add_bundles_to_dataset(dataset_id=dataset.id, bundles=[bundle])
