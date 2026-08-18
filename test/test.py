import unittest
from unittest.mock import patch
from access.access import Credentials, BiometricScan


# noinspection global-undefined
class TestCredentials(unittest.TestCase):

    @patch("builtins.input", side_effect=["username"])
    @patch("builtins.input", side_effect=["password"])
    def testValidLogin(self, mock_pass, mock_input):
        c = Credentials()
        result = c.userPassCredentials()
        self.assertTrue(result)

    @patch("builtins.input", side_effect=["Unknown username"])
    @patch("builtins.input", side_effect=["Unknown password"])

    def testInvalidLogin(self, mock_pass, mock_input):
        c = Credentials()
        result = c.userPassCredentials()
        self.assertFalse(result)

    def testFingerprintPass(self):
      scan = BiometricScan()
      result = scan.biometric()
      self.assertTrue(result)

    def testFingerprintFail(self):
      # scan result self
      global fingerprint
      result = fingerprint()
      self.assertTrue(result)





