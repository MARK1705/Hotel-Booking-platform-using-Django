
from django.db import models

class OTP(models.Model):
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=40)

    def __str__(self):
        return f"OTP {self.code} for session {self.session_key}"
