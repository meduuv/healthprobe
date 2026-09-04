import unittest
from healthprobe import healthy

class HealthProbeTests(unittest.TestCase):
    def test_healthy(self): self.assertTrue(healthy({"status":"healthy"}))
    def test_unhealthy(self): self.assertFalse(healthy({"status":"down"}))

if __name__ == "__main__": unittest.main()
