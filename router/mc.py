from fastapi import APIRouter, Query
from mcstatus import JavaServer

router = APIRouter()

@router.get("/")
async def root(ip = Query(None)):
    server = JavaServer.lookup(ip)
    status = server.status()
    return {"players":status.players.online, "maxplayers":status.players.max,"latency":status.latency}


