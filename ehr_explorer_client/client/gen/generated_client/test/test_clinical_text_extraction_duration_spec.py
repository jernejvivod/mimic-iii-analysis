# coding: utf-8

"""
    EHR Explorer Processor API

    API for the EHR Explorer Processor microservice  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: vivod.jernej@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import generated_client
from generated_client.models.clinical_text_extraction_duration_spec import ClinicalTextExtractionDurationSpec  # noqa: E501
from generated_client.rest import ApiException

class TestClinicalTextExtractionDurationSpec(unittest.TestCase):
    """ClinicalTextExtractionDurationSpec unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ClinicalTextExtractionDurationSpec
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = generated_client.models.clinical_text_extraction_duration_spec.ClinicalTextExtractionDurationSpec()  # noqa: E501
        if include_optional :
            return ClinicalTextExtractionDurationSpec(
                first_minutes = 56
            )
        else :
            return ClinicalTextExtractionDurationSpec(
                first_minutes = 56,
        )

    def testClinicalTextExtractionDurationSpec(self):
        """Test ClinicalTextExtractionDurationSpec"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
