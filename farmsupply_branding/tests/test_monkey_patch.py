import unittest
from odoo.addons.account.tests.test_tour import TestUi
from odoo.addons.base.tests.test_form_create import TestFormCreate

@unittest.skip('Tour is broken by default')
def test_01_account_tour(self):
    pass

TestUi.test_01_account_tour = test_01_account_tour

@unittest.skip('Test conflicts with business flow')
def test_create_res_partner(self):
    pass

TestFormCreate.test_create_res_partner = test_create_res_partner
