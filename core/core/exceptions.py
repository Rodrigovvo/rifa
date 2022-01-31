from rest_framework.exceptions import APIException


class ExceedMaxNumberTicketsInRaffle(APIException):
    status_code = 400
    default_detail = 'Número requisitado é maior que o número de tickets máximo nesta Rifa.'
    default_code = 'bad_request'
