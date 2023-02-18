from fastapi import APIRouter, Depends, Query

from api.v1.models import PostRequestReview, PostRequestReviewLike
from api.v1.pagination import PaginatedParams
from services.review import ReviewService, get_review_service

router = APIRouter()
RESP404 = {404: {"description": "Item not found"}}


@router.post('/', responses=RESP404)
async def post_review(data: PostRequestReview,
                      review_serv: ReviewService = Depends(get_review_service)):
    """Постит рецензию."""
    res = await review_serv.post_review(data)
    return {'id': str(res.inserted_id)}


@router.get('/{review_id}', responses=RESP404)
async def get_review(review_id: str,
                     review_serv: ReviewService = Depends(get_review_service)):
    """Отдает рецензию."""
    res = await review_serv.get_review(review_id)
    return res


@router.post('/like', responses=RESP404)
async def post_review_like(data: PostRequestReviewLike,
                           review_serv: ReviewService = Depends(get_review_service)):
    """Постит лайк на рецензию. """
    res = await review_serv.post_review_like(data)
    return res


@router.get('/list/{movie_id}', responses=RESP404)
async def get_review_list(movie_id: str,
                          sort_rating: int = Query(default=None, alias='sort[rating]', ge=-1, le=1),
                          sort_count: int = Query(default=None, alias='sort[count]', ge=-1, le=1),
                          pagin: PaginatedParams = Depends(),
                          review_serv: ReviewService = Depends(get_review_service)):
    """Отдает список рецензий. Есть пагинация. Сортировка по количеству лайков/дизлайков,
    сортировка по средниму рейтингу, """
    res = await review_serv.get_review_list(movie_id, sort_rating, sort_count, pagin)
    return res


@router.delete('/clear_all', responses=RESP404)
async def get_review_list(review_serv: ReviewService = Depends(get_review_service)):
    """Очищает все review. Уbеру после ревью."""
    await review_serv.clear_all()
    return
