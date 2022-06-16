from math import lcm as mcm

from fastapi import HTTPException


class Controller:
    @staticmethod
    async def calMcm(numbers) -> int:
        for item in numbers:
            if type(item) is str:
                raise HTTPException(
                    status_code=403, detail="The element {item} cannot be a string")
        return mcm(*numbers)

    async def incNumber(number) -> int:
        if number is str:
            raise HTTPException(
                status_code=403, detail="{number} cannot be a string")

        return number + 1
