from typing import List
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List


class Bhlog_data(BaseModel):
    title: str = Field(..., title="Title", description="Title of your Bhlog",
                       example="Title of the Bhlog")
    content: str = Field(..., title="Content",
                         description="Content of your Bhlog. ", example="Content of example Bhlog. Dhaga khol ke likhe hai bhai.")
    feature_image: str = Field(None, title="Feature Image URL",
                               description="URL of Bhlog's feature image", example="google.com")
    tags: List[str] = Field(
        "bhlog", title="Tags", description="Tags for your bhlogs", example=["E_ka_Bawasir_bana_diye_ho", "bhlog"])


class Bhlog_DB(Bhlog_data):
    id: int = Field(..., ge=1, title="Bhlog ID",
                    description="ID of the bhlog", example="16")
    created_at: datetime
    updated_at: datetime = Field(None)


class Bhlog_response(Bhlog_data):
    id: int = Field(..., ge=1, title="Bhlog ID",
                    description="ID of the bhlog", example="16")
