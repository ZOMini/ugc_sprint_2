from functools import lru_cache
from typing import Any

from bson.objectid import ObjectId
from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.database import Collection, Database
from pymongo.results import DeleteResult, InsertOneResult

from api.v1.models import PostRequestBookmark
from api.v1.pagination import PaginatedParams
from core.config import settings
from db.mongo import get_aio_motor


class BookmarkService():
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo
        self.db: Database = self.mongo[settings.mongo_db]
        self.bookmark: Collection = self.db.bookmark

    def _convert_id(self, target: dict) -> dict:
        target['_id'] = str(target['_id'])
        return target

    async def post_bookmark(self, data: PostRequestBookmark) -> HTTPException | dict[str, str]:
        if _ := await self.bookmark.find_one({'user_id': data.user_id, 'movie_id': data.movie_id}):
            return HTTPException(status.HTTP_409_CONFLICT)
        _id: InsertOneResult = await self.bookmark.insert_one(data.dict())
        return {'id': str(_id.inserted_id)}

    async def get_bookmark(self, _id: str) -> HTTPException | dict:
        res = await self.bookmark.find_one({'_id': ObjectId(_id)})
        async for doc in self.bookmark.find():
            print(doc)
        if not res:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        res = self._convert_id(res)
        return res

    async def delete_bookmark(self, data: PostRequestBookmark) -> HTTPException | dict[str, Any]:
        res: DeleteResult = await self.bookmark.delete_one(
            {'user_id': data.user_id,
             'movie_id': data.movie_id})
        if res.deleted_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return res.raw_result

    async def get_bookmark_list(self, user_id: str, pagin: PaginatedParams) -> list[dict]:
        """Метод для формирования списка закладок."""
        pipeline = [{'$match': {'user_id': user_id}},
                    {'$project': {'movie_id': 1}}]
        pipeline.append({'$skip': pagin.page * pagin.size})
        pipeline.append({'$limit': pagin.size})
        res = []
        async for docs in self.bookmark.aggregate(pipeline):
            self._convert_id(docs)
            res.append(docs)
        return res


@lru_cache()
def get_bookmark_service(
    mongo_storage: AsyncIOMotorClient = Depends(get_aio_motor),
) -> BookmarkService:
    return BookmarkService(mongo=mongo_storage)
