from functools import lru_cache

from bson.objectid import ObjectId
from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Collection, Database
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult

from api.v1.models import DeleteRequestLike, PostRequestLike
from core.config import settings
from db.mongo import get_aio_motor


class LikeService():
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo
        self.db: Database = self.mongo[settings.mongo_db]
        self.like: Collection = self.db.like

    def _convert_id(self, target: dict) -> dict:
        target['_id'] = str(target['_id'])
        return target

    async def post_like(self, data: PostRequestLike) -> InsertOneResult:
        if _ := await self.like.find_one({'user_id': data.user_id, 'movie_id': data.movie_id}):
            return await self.put_like(data)
        _id: InsertOneResult = await self.like.insert_one(data.dict())
        return {'id': str(_id.inserted_id)}

    async def get_like(self, data: str) -> dict:
        res = await self.like.find_one({'_id': ObjectId(data)})
        if not res:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        res = self._convert_id(res)
        return res

    async def get_count_likes(self, movie_id: str) -> dict:
        l = await self.like.count_documents({'movie_id': movie_id, 'value': 10})
        d = await self.like.count_documents({'movie_id': movie_id, 'value': 0})
        if await self.like.count_documents({'movie_id': movie_id}) == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return {'like': l, 'dislike': d}

    async def get_avg_likes(self, movie_id: str) -> dict:
        sum, cnt = 0, 0 
        pipeline = [{'$match': {'movie_id': movie_id}}]
        async for docs in self.like.aggregate(pipeline):
            sum += docs['value']
            cnt += 1
        if sum == 0 and cnt > 0:
            return {'avg': 0}
        elif sum == 0 and cnt == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return {'avg': round(sum / cnt, 2)}

    async def put_like(self, data: PostRequestLike) -> UpdateResult:
        res: UpdateResult = await self.like.update_one(
            {'user_id': data.user_id,
             'movie_id': data.movie_id},
            {'$set': {'value': data.value}})
        if res.matched_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return res.raw_result

    async def delete_like(self, data: DeleteRequestLike) -> DeleteResult:
        res: DeleteResult = await self.like.delete_one(
            {'user_id': data.user_id,
             'movie_id': data.movie_id})
        if res.deleted_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return res.raw_result

@lru_cache()
def get_like_service(
    mongo_storage: AsyncIOMotorClient = Depends(get_aio_motor),
) -> LikeService:
    return LikeService(mongo=mongo_storage)
