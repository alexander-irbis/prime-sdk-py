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
from .base_response import BaseResponse
from .client import Client
from typing import List
from .credentials import Credentials
from .utils import append_query_param


@dataclass
class GetWalletDepositInstructionsRequest:
    portfolio_id: str
    wallet_id: str
    deposit_type: str
    allowed_status_codes: List[int] = None


@dataclass
class GetWalletDepositInstructionsResponse(BaseResponse):
    request: GetWalletDepositInstructionsRequest


class PrimeClient:
    def __init__(self, credentials: Credentials):
        self.client = Client(credentials)

    def get_wallet_deposit_instructions(
            self,
            request: GetWalletDepositInstructionsRequest) -> GetWalletDepositInstructionsResponse:
        path = f"/portfolios/{request.portfolio_id}/wallets/{request.wallet_id}/deposit_instructions"

        query_params = append_query_param("", 'deposit_type', request.deposit_type)

        response = self.client.request("GET", path, query=query_params,
                                       allowed_status_codes=request.allowed_status_codes)
        return GetWalletDepositInstructionsResponse(response.json(), request)
