# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class DynamicList(Model):
    """Defines an extension for a list entity.

    All required parameters must be populated in order to send to Azure.

    :param list_entity_name: Required. The name of the list entity to extend.
    :type list_entity_name: str
    :param request_lists: Required. The lists to append on the extended list
     entity.
    :type request_lists:
     list[~azure.cognitiveservices.language.luis.runtime.models.RequestList]
    """

    _validation = {
        'list_entity_name': {'required': True},
        'request_lists': {'required': True},
    }

    _attribute_map = {
        'list_entity_name': {'key': 'listEntityName', 'type': 'str'},
        'request_lists': {'key': 'requestLists', 'type': '[RequestList]'},
    }

    def __init__(self, *, list_entity_name: str, request_lists, **kwargs) -> None:
        super(DynamicList, self).__init__(**kwargs)
        self.list_entity_name = list_entity_name
        self.request_lists = request_lists


class Error(Model):
    """Represents the error that occurred.

    All required parameters must be populated in order to send to Azure.

    :param error: Required.
    :type error:
     ~azure.cognitiveservices.language.luis.runtime.models.ErrorBody
    """

    _validation = {
        'error': {'required': True},
    }

    _attribute_map = {
        'error': {'key': 'error', 'type': 'ErrorBody'},
    }

    def __init__(self, *, error, **kwargs) -> None:
        super(Error, self).__init__(**kwargs)
        self.error = error


class ErrorException(HttpOperationError):
    """Server responsed with exception of type: 'Error'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorException, self).__init__(deserialize, response, 'Error', *args)


class ErrorBody(Model):
    """Represents the definition of the error that occurred.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. The error code.
    :type code: str
    :param message: Required. The error message.
    :type message: str
    """

    _validation = {
        'code': {'required': True},
        'message': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
    }

    def __init__(self, *, code: str, message: str, **kwargs) -> None:
        super(ErrorBody, self).__init__(**kwargs)
        self.code = code
        self.message = message


class ExternalEntity(Model):
    """Defines a user perdicted entity that extends an already existing one.

    All required parameters must be populated in order to send to Azure.

    :param entity_name: Required. The name of the entity to extend.
    :type entity_name: str
    :param start_index: Required. The start character index of the predicted
     entity.
    :type start_index: int
    :param entity_length: Required. The length of the predicted entity.
    :type entity_length: int
    :param resolution: A user supplied custom resolution to return as the
     entity's prediction.
    :type resolution: object
    """

    _validation = {
        'entity_name': {'required': True},
        'start_index': {'required': True},
        'entity_length': {'required': True},
    }

    _attribute_map = {
        'entity_name': {'key': 'entityName', 'type': 'str'},
        'start_index': {'key': 'startIndex', 'type': 'int'},
        'entity_length': {'key': 'entityLength', 'type': 'int'},
        'resolution': {'key': 'resolution', 'type': 'object'},
    }

    def __init__(self, *, entity_name: str, start_index: int, entity_length: int, resolution=None, **kwargs) -> None:
        super(ExternalEntity, self).__init__(**kwargs)
        self.entity_name = entity_name
        self.start_index = start_index
        self.entity_length = entity_length
        self.resolution = resolution


class Intent(Model):
    """Represents an intent prediction.

    :param score: The score of the fired intent.
    :type score: float
    :param child_app: The prediction of the dispatched application.
    :type child_app:
     ~azure.cognitiveservices.language.luis.runtime.models.Prediction
    """

    _attribute_map = {
        'score': {'key': 'score', 'type': 'float'},
        'child_app': {'key': 'childApp', 'type': 'Prediction'},
    }

    def __init__(self, *, score: float=None, child_app=None, **kwargs) -> None:
        super(Intent, self).__init__(**kwargs)
        self.score = score
        self.child_app = child_app


class Prediction(Model):
    """Represents the prediction of a query.

    All required parameters must be populated in order to send to Azure.

    :param normalized_query: Required. The query after pre-processing and
     normalization.
    :type normalized_query: str
    :param altered_query: The query after spell checking. Only set if spell
     check was enabled and a spelling mistake was found.
    :type altered_query: str
    :param top_intent: Required. The name of the top scoring intent.
    :type top_intent: str
    :param intents: Required. A dictionary representing the intents that
     fired.
    :type intents: dict[str,
     ~azure.cognitiveservices.language.luis.runtime.models.Intent]
    :param entities: Required. The dictionary representing the entities that
     fired.
    :type entities: dict[str, object]
    :param sentiment: The result of the sentiment analysis.
    :type sentiment:
     ~azure.cognitiveservices.language.luis.runtime.models.Sentiment
    """

    _validation = {
        'normalized_query': {'required': True},
        'top_intent': {'required': True},
        'intents': {'required': True},
        'entities': {'required': True},
    }

    _attribute_map = {
        'normalized_query': {'key': 'normalizedQuery', 'type': 'str'},
        'altered_query': {'key': 'alteredQuery', 'type': 'str'},
        'top_intent': {'key': 'topIntent', 'type': 'str'},
        'intents': {'key': 'intents', 'type': '{Intent}'},
        'entities': {'key': 'entities', 'type': '{object}'},
        'sentiment': {'key': 'sentiment', 'type': 'Sentiment'},
    }

    def __init__(self, *, normalized_query: str, top_intent: str, intents, entities, altered_query: str=None, sentiment=None, **kwargs) -> None:
        super(Prediction, self).__init__(**kwargs)
        self.normalized_query = normalized_query
        self.altered_query = altered_query
        self.top_intent = top_intent
        self.intents = intents
        self.entities = entities
        self.sentiment = sentiment


class PredictionRequest(Model):
    """Represents the prediction request parameters.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The query to predict.
    :type query: str
    :param options: The custom options defined for this request.
    :type options:
     ~azure.cognitiveservices.language.luis.runtime.models.PredictionRequestOptions
    :param external_entities: The externally predicted entities for this
     request.
    :type external_entities:
     list[~azure.cognitiveservices.language.luis.runtime.models.ExternalEntity]
    :param dynamic_lists: The dynamically created list entities for this
     request.
    :type dynamic_lists:
     list[~azure.cognitiveservices.language.luis.runtime.models.DynamicList]
    """

    _validation = {
        'query': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'options': {'key': 'options', 'type': 'PredictionRequestOptions'},
        'external_entities': {'key': 'externalEntities', 'type': '[ExternalEntity]'},
        'dynamic_lists': {'key': 'dynamicLists', 'type': '[DynamicList]'},
    }

    def __init__(self, *, query: str, options=None, external_entities=None, dynamic_lists=None, **kwargs) -> None:
        super(PredictionRequest, self).__init__(**kwargs)
        self.query = query
        self.options = options
        self.external_entities = external_entities
        self.dynamic_lists = dynamic_lists


class PredictionRequestOptions(Model):
    """The custom options for the prediction request.

    :param datetime_reference: The reference DateTime used for predicting
     datetime entities.
    :type datetime_reference: datetime
    :param override_predictions: Whether to make the external entities
     resolution override the predictions if an overlap occurs.
    :type override_predictions: bool
    """

    _attribute_map = {
        'datetime_reference': {'key': 'datetimeReference', 'type': 'iso-8601'},
        'override_predictions': {'key': 'overridePredictions', 'type': 'bool'},
    }

    def __init__(self, *, datetime_reference=None, override_predictions: bool=None, **kwargs) -> None:
        super(PredictionRequestOptions, self).__init__(**kwargs)
        self.datetime_reference = datetime_reference
        self.override_predictions = override_predictions


class PredictionResponse(Model):
    """Represents the prediction response.

    All required parameters must be populated in order to send to Azure.

    :param query: Required. The query used in the prediction.
    :type query: str
    :param prediction: Required. The prediction of the requested query.
    :type prediction:
     ~azure.cognitiveservices.language.luis.runtime.models.Prediction
    """

    _validation = {
        'query': {'required': True},
        'prediction': {'required': True},
    }

    _attribute_map = {
        'query': {'key': 'query', 'type': 'str'},
        'prediction': {'key': 'prediction', 'type': 'Prediction'},
    }

    def __init__(self, *, query: str, prediction, **kwargs) -> None:
        super(PredictionResponse, self).__init__(**kwargs)
        self.query = query
        self.prediction = prediction


class RequestList(Model):
    """Defines a sub-list to append to an existing list entity.

    All required parameters must be populated in order to send to Azure.

    :param name: The name of the sub-list.
    :type name: str
    :param canonical_form: Required. The canonical form of the sub-list.
    :type canonical_form: str
    :param synonyms: The synonyms of the canonical form.
    :type synonyms: list[str]
    """

    _validation = {
        'canonical_form': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'canonical_form': {'key': 'canonicalForm', 'type': 'str'},
        'synonyms': {'key': 'synonyms', 'type': '[str]'},
    }

    def __init__(self, *, canonical_form: str, name: str=None, synonyms=None, **kwargs) -> None:
        super(RequestList, self).__init__(**kwargs)
        self.name = name
        self.canonical_form = canonical_form
        self.synonyms = synonyms


class Sentiment(Model):
    """The result of the sentiment analaysis.

    All required parameters must be populated in order to send to Azure.

    :param label: The label of the sentiment analysis result.
    :type label: str
    :param score: Required. The sentiment score of the query.
    :type score: float
    """

    _validation = {
        'score': {'required': True},
    }

    _attribute_map = {
        'label': {'key': 'label', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
    }

    def __init__(self, *, score: float, label: str=None, **kwargs) -> None:
        super(Sentiment, self).__init__(**kwargs)
        self.label = label
        self.score = score
