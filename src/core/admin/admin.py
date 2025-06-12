from crudadmin import CRUDAdmin
from core.config import settings
from core.models.models import PricingPricingstrategy
from core.schemas.prices_schema import PriceCreateSchema, PriceUpdateSchema
from core.models.db_helper import db_helper


admin = CRUDAdmin(
    session = db_helper.session_getter,
    SECRET_KEY = settings.AdminConfig.SECRET_KEY,
    admin_db_url= settings.AdminConfig.admin_db_url,
    initial_admin= {
        "username": settings.AdminConfig.initial_username,
        "password": settings.AdminConfig.initial_password
    },
    mount_path = settings.AdminConfig.mount_path,
    track_events = settings.AdminConfig.track_events,
    session_timeout_minutes = 30,
    max_sessions_per_user = 5,
    # csrf_protection = True,
    cleanup_interval_minutes = 15
    # secure_cookies = settings.AdminConfig.secure_cookies,
    # enforce_https = settings.AdminConfig.enforce_https
)

admin.add_view(
    model = PricingPricingstrategy,
    create_schema = PriceCreateSchema,
    update_schema = PriceUpdateSchema,
    allowed_actions = {"view", "create", "update", "delete"}
)