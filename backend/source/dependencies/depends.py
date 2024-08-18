from fastapi import Query


class Dependencies:
    def pagination(self, skip: int = Query(0, ge=0), limit: int = Query(10, ge=0)) -> tuple[int, int]:
        capped_limit = min(100, limit)
        return skip, capped_limit
