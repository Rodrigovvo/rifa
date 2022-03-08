import os

from mailjet_rest import Client
from core.settings import MAILJET_KEY_API, MAILJET_SECRET_API, EMAIL_HOST_NAME, EMAIL_HOST_USER


class MailjetEmailSender():
	"""
	Classe para envio de email através da API do MailJet.
	"""

	def __init__(self):
		self.mailjet = Client(
			auth=(MAILJET_KEY_API, MAILJET_SECRET_API), 
			version='v3.1'
		)

	def send_mail(
		self,
		to_name, 
		to_email, 
		subject, 
		text_content=None, 
		html_content=None, 
		customID=None
	):
		"""
		Função que efetiva o envio de email através da API da MailJet <doc: mailjet.com>
		Os parâmetros text_content e html_content são conflitantes, 
		sendo apresentados ambos será encaminhado o conteúdo do html_content.

		:param to_name: (string) Nome do destinatário.
		:param to_email: (string) Email do Destinatário.
		:param subject: (string) Campo 'assunto' do email.
		:param text_content: (string) Conteúdo do email em texto.
		:param html_content: (string) Conteúdo do email em Html.
		:param CustomID: (string) Id customizado para controle do envio.

		:returns: (Response) Retorno HTTP da requisição.
		
		"""
		data = {
		  'Messages': [
		    {
		      "From": {
		        "Email": EMAIL_HOST_USER,
		        "Name": EMAIL_HOST_NAME
		      },
		      "To": [
		        {
		          "Email": to_email,
		          "Name": to_name
		        }
		      ],
		      "Subject": subject,
		      "TextPart": text_content,
		      "HTMLPart": html_content,
		      "CustomID": customID
		    }
		  ]
		}
		result = self.mailjet.send.create(data=data)
		return result
