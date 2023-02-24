from functools import lru_cache
from typing import Any

from bson.objectid import ObjectId
from fastapi import Depends, HTTPException, status
from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase
)
from pymongo.results import InsertOneResult, UpdateResult

from api.v1.models import PostRequestReview, PostRequestReviewLike
from api.v1.pagination import PaginatedParams
from core.config import settings
from db.mongo import get_aio_motor
from services.like import LikeService, PostRequestLike


class ReviewService():
    def __init__(self, mongo: AsyncIOMotorClient):
        self.mongo = mongo
        self.db: AsyncIOMotorDatabase = self.mongo[settings.mongo_db]
        self.review: AsyncIOMotorCollection = self.db.review
        self.review_like: AsyncIOMotorCollection = self.db.review_like

    async def post_review(self, data: PostRequestReview) -> InsertOneResult:
        """Постит ревью. При создании пост получает рейтинг 5.0(count=1, summ=5)."""
        data_dict = data.dict()
        _id: InsertOneResult = await self.review.insert_one(data_dict)
        if data_dict['value']:
            like = LikeService(self.mongo)
            await like.post_like(PostRequestLike(user_id=data_dict['user_id'],
                                                 movie_id=data_dict['movie_id'],
                                                 value=data_dict['value']))
        return _id

    async def get_review(self, data: str) -> dict:
        """Ручка вне задания, но нужна."""
        res = await self.review.find_one({'_id': ObjectId(data)})
        if not res:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return res

    async def post_review_like(self, data: PostRequestReviewLike) -> HTTPException | dict[str, Any]:
        """Постит лайк на ревью, доbавляет сумму и количество в модель review,
        для расчета среднего рейтинга при формировании списка ревью для фильма."""
        if _ := await self.review_like.find_one({'user_id': data.user_id, 'review_id': data.review_id}):
            raise HTTPException(status.HTTP_409_CONFLICT)
            # return await self.put_review_like(data)
        data_dict = data.dict()
        _id: InsertOneResult = await self.review_like.insert_one(data_dict)
        # Ниже увеличиваем количество и сумму bалов для rewiew, получившего оценку.
        await self.review.update_one({'_id': ObjectId(data.review_id)}, {'$inc': {'summ_like': data.value, 'count_like': 1}})
        return {'id': _id.inserted_id}

    async def _put_review_like(self, data: PostRequestReviewLike) -> HTTPException | dict[str, Any]:
        """Пока не раbочий метод. Лайкнуть ревьюв можно один раз."""
        res: UpdateResult = await self.review_like.update_one(
            {'user_id': data.user_id,
             'review_id': data.review_id},
            {'$set': {'value': data.value}})
        if res.matched_count == 0:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return res.raw_result

    async def get_review_list(self, movie_id: str, sort_rating: int, sort_count: int, pagin: PaginatedParams) -> list[dict]:
        """Метод для формирования списка ревью, summ_like и count_like в ревью для отладки."""
        pipeline = [{'$match': {'movie_id': movie_id}},
                    {'$project': {'summ_like': 1, 'count_like': 1, 'user_id': 1, 'text': 1, 'rating': {'$divide': ['$summ_like', '$count_like']}}},
                    {'$skip': pagin.page * pagin.size},
                    {'$limit': pagin.size}]
        pipeline.append({'$sort': {'rating': sort_rating}}) if sort_rating else {}
        pipeline.append({'$sort': {'count_like': sort_count}}) if sort_count else {}
        res = []
        async for docs in self.review.aggregate(pipeline):
            res.append(docs)
        return res

    async def clear_all(self) -> None:
        """Ручка для разраbотки. Удалю после ревью. Кнопка b сломалась - кофе разлил:)"""
        self.review.drop()
        self.review_like.drop()


@lru_cache()
def get_review_service(
    mongo_storage: AsyncIOMotorClient = Depends(get_aio_motor),
) -> ReviewService:
    return ReviewService(mongo=mongo_storage)
