# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate
from datetime import datetime, timedelta, date
from dateutil import relativedelta
#Get the logger
_logger = logging.getLogger(__name__)

class res_partner(models.Model):
	_inherit = 'res.partner'

	@api.model
	def process_due_payments(self):
		partners = self.search([('customer','=',True),('credit','>',0)])
		partner_list = []
		for partner in partners:
			move_lines = self.env['account.move.line'].search([('days_overdue','>',0)])
			if move_lines:
				partner_list.append(partner)
		if partner_list:
			for partner in partner_list:
				partner.do_partner_mail()
		return None



