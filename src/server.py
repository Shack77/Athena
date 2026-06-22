from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pathlib import Path
from datetime import datetime
import json

app = FastAPI()

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def log(message):

    filename = LOG_DIR / f"{datetime.now():%Y%m%d}.log"

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    line = f"[{timestamp}] {message}"

    print(line)

    with open(
        filename,
        "a",
        encoding="utf-8"
    ) as f:

        f.write(line + "\n")


@app.get("/")
async def root():

    log("HTTP Request Received")

    return {
        "status": "running"
    }


@app.websocket("/media-stream")
async def media_stream(
    websocket: WebSocket
):

    log("WebSocket Attempt")

    await websocket.accept()

    log("WebSocket Accepted")

    stream_sid = None

    try:

        while True:

            data = await websocket.receive_text()

            try:

                payload = json.loads(data)

                event = payload.get(
                    "event",
                    "unknown"
                )

                if event == "connected":

                    log(
                        "Twilio Stream Connected"
                    )

                elif event == "start":

                    stream_sid = (
                        payload["start"]
                        .get(
                            "streamSid"
                        )
                    )

                    log(
                        f"Stream Started: "
                        f"{stream_sid}"
                    )

                elif event == "media":

                    log(
                        "Media Packet Received"
                    )

                elif event == "stop":

                    log(
                        "Stream Stopped"
                    )

                else:

                    log(
                        f"Event: {event}"
                    )

            except Exception as e:

                log(
                    f"JSON Parse Error: {e}"
                )

    except WebSocketDisconnect:

        log(
            "WebSocket Disconnected"
        )

    except Exception as e:

        log(
            f"WebSocket Error: {e}"
        )