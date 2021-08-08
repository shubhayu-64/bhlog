from fastapi import FastAPI, Path
from fastapi.responses import RedirectResponse
from schemas import *


desc = """
## This is IIC bhlog backend. 🍑🤚

### #E_ka_Bawasir_bana_diye_ho 💩🚀

"""

DB = []

bhlog = FastAPI(title="Bhlog API",
                description=desc,
                openapi_url="/bhlog_api/v1.1/openapi.json",
                version="0.1.1",
                docs_url="/bhlog_api/v1.1/documentation"
                )


@bhlog.get("/")
async def redirect():
    return RedirectResponse("/bhlog_api/v1.1/documentation")


@bhlog.get("/bhlog_api/v1.1/home/", description="**Welcome to Bhlog API**")
async def home():
    return {
        "Welcome": "Welcome to IIC Bhlog",
        "#": "E_ka_Bawasir_bana_diye_ho"
    }


@bhlog.get("/bhlog_api/v1.1/bhlogs", response_model=List[Bhlog_response], description="Shows all Bhlogs avilable. Injoy <3")
async def get_all_bhlogs():
    return DB


@bhlog.get("/bhlog_api/v1.1/bhlog/{id}", response_model=Bhlog_response, response_model_exclude={"id"}, description="Shows Bhlog of given ID. Injoy <3")
async def get_bhlog(id: int = Path(..., ge=1, title="Bhlog ID",
                                   description="ID of the bhlog", example="16")):
    id = id-1
    return DB[id]


@ bhlog.put("/bhlog_api/v1.1/add_bhlog", response_model=Bhlog_response, description="**Add your bhlogs** from here.\nCheck the **Bhlog Data Schema** for more information")
async def Add_Bhlog(bhlog: Bhlog_data):
    cur_id = len(DB) + 1
    time = datetime.now()
    data = Bhlog_DB(**bhlog.dict(), id=cur_id, created_at=time)
    DB.append(data)
    return data


@ bhlog.put("/bhlog_api/v1.1/update_bhlog", response_model=Bhlog_response, description="**Update your bhlogs** from here.\nCheck the **Bhlog Data Schema** for more information")
async def update_bhlog(bhlog: Bhlog_data, id: int = Path(..., ge=1, title="Bhlog ID",
                                                         description="ID of the bhlog", example="16")):
    data = DB[id-1]
    data.title = bhlog.title
    data.content = bhlog.content
    data.feature_image = bhlog.feature_image
    data.tags = bhlog.tags
    data.updated_at = datetime.now()
    return data


@ bhlog.delete("/bhlog_api/v1.1/delete_bhlog/{id}", description="Delete Bhlog based on ID")
async def delete_bhlog(id: int = Path(..., ge=1, title="Bhlog ID",
                                      description="ID of the bhlog", example="16")):
    id = id-1
    DB.pop(id)
    return {"Bhlog was deleted"}
