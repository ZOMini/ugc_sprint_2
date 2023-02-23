from fastapi import APIRouter, Depends

from api.v1.models import DeleteRequestLike, PostRequestLike
from services.like import LikeService, get_like_service

router = APIRouter()
RESP404 = {"detail": "Not found"}


@router.post('/', responses={404: RESP404})
async def post_like(data: PostRequestLike,
                    like_serv: LikeService = Depends(get_like_service)):
    """Постит лайк. Если для пары id уже есть лайк, то апдейтит."""
    res = await like_serv.post_like(data)
    return res


@router.get('/{like_id}', responses={404: RESP404})
async def get_like(like_id: str,
                   like_serv: LikeService = Depends(get_like_service)):
    """Отдает лайк по id лайка."""
    res = await like_serv.get_like(like_id)
    return res


@router.get('/count_likes/{movie_id}', responses={404: RESP404})
async def get_count_likes(movie_id: str,
                          like_serv: LikeService = Depends(get_like_service)):
    """Отдает количество лайков/дизлайков."""
    res = await like_serv.get_count_likes(movie_id)
    return res


@router.get('/avg_likes/{movie_id}', responses={404: RESP404})
async def get_avg_likes(movie_id: str,
                        like_serv: LikeService = Depends(get_like_service)):
    """Отдает средний рейтинг."""
    res = await like_serv.get_avg_likes(movie_id)
    return res


@router.put('/', responses={404: RESP404})
async def put_like(data: PostRequestLike,
                   like_serv: LikeService = Depends(get_like_service)):
    """Апдейтит лайк."""
    res = await like_serv.put_like(data)
    return res


@router.delete('/', responses={404: RESP404})
async def delete_like(data: DeleteRequestLike,
                      like_serv: LikeService = Depends(get_like_service)):
    """Удаляет лайк."""
    res = await like_serv.delete_like(data)
    return res
