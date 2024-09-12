import io
import qrcode
import uuid
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import status, HTTPException

import source.crud.invitation_codes as codes_crud
from source.models.invitation_code import InvitationCode
from source.config.secret import secret_config

def generate_random_code() -> str:
    unique_id: str = str(uuid.uuid4()).replace('-', '')

    return unique_id[:9]

async def _create_code(code:str, event_id: int, session: AsyncSession) -> None:
    expiration: datetime = datetime.now() + timedelta(minutes=secret_config.INVITATION_TOKEN_EXPIRE_MINUTES)
    code = InvitationCode(code=code, event_id=event_id, expiration_date=expiration)
    await codes_crud.create(code, session)

async def create_qr_code(code: str, session: AsyncSession) -> io.BytesIO:
    if not await codes_crud.get_by_code(code, session):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Code not found')
    link: str = f'http://127.0.0.1:8000/events/join/{code}'
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return img_io

async def create_codes(event_id: int, session: AsyncSession) -> str:
    code: str = generate_random_code()
    await _create_code(code, event_id, session)

    return code