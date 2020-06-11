# coding: utf-8

"""
    Finnhub API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from finnhub.configuration import Configuration


class Split(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'symbol': 'str',
        'date': 'date',
        'from_factor': 'float',
        'to_factor': 'float'
    }

    attribute_map = {
        'symbol': 'symbol',
        'date': 'Date',
        'from_factor': 'fromFactor',
        'to_factor': 'toFactor'
    }

    def __init__(self, symbol=None, date=None, from_factor=None, to_factor=None, local_vars_configuration=None):  # noqa: E501
        """Split - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._symbol = None
        self._date = None
        self._from_factor = None
        self._to_factor = None
        self.discriminator = None

        if symbol is not None:
            self.symbol = symbol
        if date is not None:
            self.date = date
        if from_factor is not None:
            self.from_factor = from_factor
        if to_factor is not None:
            self.to_factor = to_factor

    @property
    def symbol(self):
        """Gets the symbol of this Split.  # noqa: E501

        Symbol.  # noqa: E501

        :return: The symbol of this Split.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this Split.

        Symbol.  # noqa: E501

        :param symbol: The symbol of this Split.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def date(self):
        """Gets the date of this Split.  # noqa: E501

        Split date.  # noqa: E501

        :return: The date of this Split.  # noqa: E501
        :rtype: date
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Split.

        Split date.  # noqa: E501

        :param date: The date of this Split.  # noqa: E501
        :type: date
        """

        self._date = date

    @property
    def from_factor(self):
        """Gets the from_factor of this Split.  # noqa: E501

        From factor.  # noqa: E501

        :return: The from_factor of this Split.  # noqa: E501
        :rtype: float
        """
        return self._from_factor

    @from_factor.setter
    def from_factor(self, from_factor):
        """Sets the from_factor of this Split.

        From factor.  # noqa: E501

        :param from_factor: The from_factor of this Split.  # noqa: E501
        :type: float
        """

        self._from_factor = from_factor

    @property
    def to_factor(self):
        """Gets the to_factor of this Split.  # noqa: E501

        To factor.  # noqa: E501

        :return: The to_factor of this Split.  # noqa: E501
        :rtype: float
        """
        return self._to_factor

    @to_factor.setter
    def to_factor(self, to_factor):
        """Sets the to_factor of this Split.

        To factor.  # noqa: E501

        :param to_factor: The to_factor of this Split.  # noqa: E501
        :type: float
        """

        self._to_factor = to_factor

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Split):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Split):
            return True

        return self.to_dict() != other.to_dict()
