from sqlalchemy import select, update

from db.connection import async_session


class BaseCRUD:
    MODEL = None

    async def _create(self, **kwargs):
        model_obj = self.MODEL(**kwargs)
        async with async_session() as session:
            session.add(model_obj)
            await session.commit()
            return model_obj

    async def _get_one(self, search_fields):
        sql = select(self.MODEL).filter_by(**search_fields)
        async with async_session() as session:
            query = await session.execute(sql)
            return query.scalar_one()

    async def _get_many(self, search_fields):
        sql = select(self.MODEL).filter_by(**search_fields)
        async with async_session() as session:
            query = await session.execute(sql)
            return query.scalars().all()

    async def _update(self, search_fields, **kwargs):
        sql = update(self.MODEL).filter_by(**search_fields).values(**kwargs).execution_options(
            synchronize_session="fetch"
        )
        async with async_session() as session:
            await session.execute(sql)
            await session.commit()
            return await self._get_one(search_fields)

    async def _delete(self, search_fields):
        obj = await self._get_one(search_fields)
        async with async_session() as session:
            await session.delete(obj)
