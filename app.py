import asyncio
import random
from typing import AsyncGenerator
from uuid import uuid4

import uvicorn
from faker import Faker
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from tqdm import trange

app = FastAPI()
fake = Faker()


@app.get("/drawing/{rows}")
async def play_ball(rows: int) -> StreamingResponse:
    """
    :param rows:
    :return: N rows of data
    """

    async def generate() -> AsyncGenerator[str, None]:
        """
        Async generate mock data
        """
        for _ in trange(rows):
            await asyncio.sleep(0.0001)
            transaction_id = uuid4()
            first_name = fake.first_name()
            last_name = fake.last_name()
            city = fake.city()
            state = fake.state_abbr(include_territories=False)
            customer_id = uuid4()
            powerball_1 = (random.randint(1, 69),)
            powerball_2 = (random.randint(1, 69),)
            powerball_3 = (random.randint(1, 69),)
            powerball_4 = (random.randint(1, 69),)
            powerball_5 = (random.randint(1, 69),)
            powerball_number = random.randint(1, 26)
            yield f"('{transaction_id}', '{first_name}', '{last_name}', '{city}', '{state}', '{customer_id}', {powerball_1}, {powerball_2}, {powerball_3}, {powerball_4}, {powerball_5}, {powerball_number})\n"

    return StreamingResponse(generate(), media_type="text/plain")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
