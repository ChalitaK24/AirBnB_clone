#!/usr/bin/python3
"""Review class defn"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review rep
    """
    place_id = ""
    user_id = ""
    text = ""
