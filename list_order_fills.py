# Copyright 2024-present Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass
from base_response import BaseResponse
from client import Client
from credentials import Credentials
from utils import PaginationParams, append_pagination_params
from typing import Optional, List


@dataclass
class ListOrderFillsRequest:
    portfolio_id: str
    order_id: str
    pagination: Optional[PaginationParams] = None
    allowed_status_codes: List[int] = None


@dataclass
class ListOrderFillsResponse(BaseResponse):
    request: ListOrderFillsRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def list_order_fills(self, request: ListOrderFillsRequest) -> ListOrderFillsResponse:
        path = f"/portfolios/{request.portfolio_id}/orders/{request.order_id}/fills"

        query_params = append_pagination_params("", request.pagination)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return ListOrderFillsResponse(response.json(), request)