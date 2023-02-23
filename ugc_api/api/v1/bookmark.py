from fastapi import APIRouter, Depends

from api.v1.models import PostRequestBookmark
from api.v1.pagination import PaginatedParams
from services.bookmark import BookmarkService, get_bookmark_service

router = APIRouter()
RESP404 = {"detail": "Not found"}


@router.post('/', responses={404: RESP404})
async def post_bookmark(data: PostRequestBookmark,
                        bookmark_serv: BookmarkService = Depends(get_bookmark_service)):
    """Постит закладку."""
    res = await bookmark_serv.post_bookmark(data)
    return res


@router.get('/{bookmark_id}', responses={404: RESP404})
async def get_bookmark(bookmark_id: str,
                       bookmark_serv: BookmarkService = Depends(get_bookmark_service)):
    """Отдает закладку по id."""
    res = await bookmark_serv.get_bookmark(bookmark_id)
    return res


@router.delete('/', responses={404: RESP404})
async def delete_bookmark(data: PostRequestBookmark,
                          bookmark_serv: BookmarkService = Depends(get_bookmark_service)):
    """Удаляет закладку."""
    res = await bookmark_serv.delete_bookmark(data)
    return res


@router.get('/list/{user_id}', responses={404: RESP404})
async def get_list_bookmark(user_id: str,
                            pagin: PaginatedParams = Depends(),
                            bookmark_serv: BookmarkService = Depends(get_bookmark_service)):
    """Отдает список закладок по id пользователя."""
    res = await bookmark_serv.get_bookmark_list(user_id, pagin)
    return res
