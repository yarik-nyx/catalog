from typing import List, Optional

from sqlalchemy import ARRAY, BigInteger, Boolean, CheckConstraint, DateTime, ForeignKeyConstraint, Identity, Index, Integer, JSON, Numeric, PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
import decimal
from datetime import UTC, datetime

from core.models.base_class import Base


class AdminSession(Base):
    __tablename__ = 'admin_session'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='admin_session_pkey'),
        Index('ix_admin_session_session_id', 'session_id', unique=True),
        Index('ix_admin_session_user_id', 'user_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    session_id: Mapped[str] = mapped_column(String(36))
    ip_address: Mapped[str] = mapped_column(String(45))
    user_agent: Mapped[str] = mapped_column(String(512))
    device_info: Mapped[dict] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    last_activity: Mapped[datetime] = mapped_column(DateTime(True))
    is_active: Mapped[bool] = mapped_column(Boolean)
    session_metadata: Mapped[dict] = mapped_column(JSON)


class AdminUser(Base):
    __tablename__ = 'admin_user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='admin_user_pkey'),
        Index('ix_admin_user_username', 'username', unique=True)
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20))
    hashed_password: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    is_superuser: Mapped[bool] = mapped_column(Boolean)
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )


class AuthGroup(Base):
    __tablename__ = 'auth_group'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='auth_group_pkey'),
        UniqueConstraint('name', name='auth_group_name_key'),
        Index('auth_group_name_a6ea08ec_like', 'name')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    name: Mapped[str] = mapped_column(String(150))

    auth_user_groups: Mapped[List['AuthUserGroups']] = relationship('AuthUserGroups', back_populates='group')
    auth_group_permissions: Mapped[List['AuthGroupPermissions']] = relationship('AuthGroupPermissions', back_populates='group')


class AuthUser(Base):
    __tablename__ = 'auth_user'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='auth_user_pkey'),
        UniqueConstraint('username', name='auth_user_username_key'),
        Index('auth_user_username_6821ab7c_like', 'username')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    password: Mapped[str] = mapped_column(String(128))
    is_superuser: Mapped[bool] = mapped_column(Boolean)
    username: Mapped[str] = mapped_column(String(150))
    first_name: Mapped[str] = mapped_column(String(150))
    last_name: Mapped[str] = mapped_column(String(150))
    email: Mapped[str] = mapped_column(String(254))
    is_staff: Mapped[bool] = mapped_column(Boolean)
    is_active: Mapped[bool] = mapped_column(Boolean)
    date_joined: Mapped[datetime] = mapped_column(DateTime(True))
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(True))

    auth_user_groups: Mapped[List['AuthUserGroups']] = relationship('AuthUserGroups', back_populates='user')
    django_admin_log: Mapped[List['DjangoAdminLog']] = relationship('DjangoAdminLog', back_populates='user')
    auth_user_user_permissions: Mapped[List['AuthUserUserPermissions']] = relationship('AuthUserUserPermissions', back_populates='user')


class ClassificationFunctionalcategory(Base):
    __tablename__ = 'classification_functionalcategory'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='classification_functionalcategory_pk'),
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    classification_functionalcategory_categories: Mapped['ClassificationFunctionalcategoryCategories'] = relationship('ClassificationFunctionalcategoryCategories', uselist=False, back_populates='functionalcategory')


class ClassificationGroup(Base):
    __tablename__ = 'classification_group'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='classification_group_pk'),
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    classification_category: Mapped[List['ClassificationCategory']] = relationship('ClassificationCategory', back_populates='group')


class DjangoContentType(Base):
    __tablename__ = 'django_content_type'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='django_content_type_pkey'),
        UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    app_label: Mapped[str] = mapped_column(String(100))
    model: Mapped[str] = mapped_column(String(100))

    auth_permission: Mapped[List['AuthPermission']] = relationship('AuthPermission', back_populates='content_type')
    django_admin_log: Mapped[List['DjangoAdminLog']] = relationship('DjangoAdminLog', back_populates='content_type')


class DjangoMigrations(Base):
    __tablename__ = 'django_migrations'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='django_migrations_pkey'),
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    app: Mapped[str] = mapped_column(String(255))
    name: Mapped[str] = mapped_column(String(255))
    applied: Mapped[datetime] = mapped_column(DateTime(True))


class DjangoSession(Base):
    __tablename__ = 'django_session'
    __table_args__ = (
        PrimaryKeyConstraint('session_key', name='django_session_pkey'),
        Index('django_session_expire_date_a5c62663', 'expire_date'),
        Index('django_session_session_key_c0390e0f_like', 'session_key')
    )

    session_key: Mapped[str] = mapped_column(String(40), primary_key=True)
    session_data: Mapped[str] = mapped_column(Text)
    expire_date: Mapped[datetime] = mapped_column(DateTime(True))


class PricingPricingstrategy(Base):
    __tablename__ = 'pricing_pricingstrategy'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pricing_pricingstrategy_pk'),
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    engine: Mapped[str] = mapped_column(String(120))
    parameters: Mapped[dict] = mapped_column(JSONB)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    catalog_collection: Mapped[List['CatalogCollection']] = relationship('CatalogCollection', back_populates='pricing_strategy')


class ReferenceEnumgroup(Base):
    __tablename__ = 'reference_enumgroup'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='reference_enumgroup_pk'),
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    reference_enumentry: Mapped[List['ReferenceEnumentry']] = relationship('ReferenceEnumentry', back_populates='group')
    configurator_optiondefinition: Mapped[List['ConfiguratorOptiondefinition']] = relationship('ConfiguratorOptiondefinition', back_populates='dict_group')


class ReferenceUnitofmeasure(Base):
    __tablename__ = 'reference_unitofmeasure'
    __table_args__ = (
        CheckConstraint('"precision" >= 0', name='reference_unitofmeasure_precision_check'),
        PrimaryKeyConstraint('id', name='reference_unitofmeasure_pkey'),
        Index('reference_unitofmeasure_id_ad4f0d6e_like', 'id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    id: Mapped[str] = mapped_column(String(20), primary_key=True)
    precision: Mapped[int] = mapped_column(SmallInteger)


class AuthPermission(Base):
    __tablename__ = 'auth_permission'
    __table_args__ = (
        ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], deferrable=True, initially='DEFERRED', name='auth_permission_content_type_id_2f476e4b_fk_django_co'),
        PrimaryKeyConstraint('id', name='auth_permission_pkey'),
        UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
        Index('auth_permission_content_type_id_2f476e4b', 'content_type_id')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    content_type_id: Mapped[int] = mapped_column(Integer)
    codename: Mapped[str] = mapped_column(String(100))

    content_type: Mapped['DjangoContentType'] = relationship('DjangoContentType', back_populates='auth_permission')
    auth_group_permissions: Mapped[List['AuthGroupPermissions']] = relationship('AuthGroupPermissions', back_populates='permission')
    auth_user_user_permissions: Mapped[List['AuthUserUserPermissions']] = relationship('AuthUserUserPermissions', back_populates='permission')


class AuthUserGroups(Base):
    __tablename__ = 'auth_user_groups'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['auth_group.id'], deferrable=True, initially='DEFERRED', name='auth_user_groups_group_id_97559544_fk_auth_group_id'),
        ForeignKeyConstraint(['user_id'], ['auth_user.id'], deferrable=True, initially='DEFERRED', name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id'),
        PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
        UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq'),
        Index('auth_user_groups_group_id_97559544', 'group_id'),
        Index('auth_user_groups_user_id_6a12ed8b', 'user_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    group_id: Mapped[int] = mapped_column(Integer)

    group: Mapped['AuthGroup'] = relationship('AuthGroup', back_populates='auth_user_groups')
    user: Mapped['AuthUser'] = relationship('AuthUser', back_populates='auth_user_groups')


class ClassificationCategory(Base):
    __tablename__ = 'classification_category'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['classification_group.id'], ondelete='RESTRICT', onupdate='CASCADE', name='classification_category_classification_group_fk'),
        PrimaryKeyConstraint('id', name='classification_category_pk'),
        Index('classification_category_group_idx', 'group_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    group_id: Mapped[int] = mapped_column(Integer)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    group: Mapped['ClassificationGroup'] = relationship('ClassificationGroup', back_populates='classification_category')
    classification_functionalcategory_categories: Mapped[List['ClassificationFunctionalcategoryCategories']] = relationship('ClassificationFunctionalcategoryCategories', back_populates='category')
    classification_subcategory: Mapped[List['ClassificationSubcategory']] = relationship('ClassificationSubcategory', back_populates='category')
    configurator_configuratortemplate: Mapped[List['ConfiguratorConfiguratortemplate']] = relationship('ConfiguratorConfiguratortemplate', back_populates='category')
    catalog_collection: Mapped[List['CatalogCollection']] = relationship('CatalogCollection', back_populates='category')


class DjangoAdminLog(Base):
    __tablename__ = 'django_admin_log'
    __table_args__ = (
        CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
        ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], deferrable=True, initially='DEFERRED', name='django_admin_log_content_type_id_c4bce8eb_fk_django_co'),
        ForeignKeyConstraint(['user_id'], ['auth_user.id'], deferrable=True, initially='DEFERRED', name='django_admin_log_user_id_c564eba6_fk_auth_user_id'),
        PrimaryKeyConstraint('id', name='django_admin_log_pkey'),
        Index('django_admin_log_content_type_id_c4bce8eb', 'content_type_id'),
        Index('django_admin_log_user_id_c564eba6', 'user_id')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    action_time: Mapped[datetime] = mapped_column(DateTime(True))
    object_repr: Mapped[str] = mapped_column(String(200))
    action_flag: Mapped[int] = mapped_column(SmallInteger)
    change_message: Mapped[str] = mapped_column(Text)
    user_id: Mapped[int] = mapped_column(Integer)
    object_id: Mapped[Optional[str]] = mapped_column(Text)
    content_type_id: Mapped[Optional[int]] = mapped_column(Integer)

    content_type: Mapped[Optional['DjangoContentType']] = relationship('DjangoContentType', back_populates='django_admin_log')
    user: Mapped['AuthUser'] = relationship('AuthUser', back_populates='django_admin_log')


class ReferenceEnumentry(Base):
    __tablename__ = 'reference_enumentry'
    __table_args__ = (
        CheckConstraint('pct >= 0', name='reference_enumentry_pct_check'),
        ForeignKeyConstraint(['group_id'], ['reference_enumgroup.id'], ondelete='RESTRICT', onupdate='CASCADE', name='reference_enumentry_reference_enumgroup_fk'),
        PrimaryKeyConstraint('id', name='reference_enumentry_pk'),
        Index('reference_enumentry_dict_group_group_idx', 'group_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    extra_price: Mapped[decimal.Decimal] = mapped_column(Numeric(9, 2))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer)
    pct: Mapped[Optional[int]] = mapped_column(SmallInteger)

    group: Mapped['ReferenceEnumgroup'] = relationship('ReferenceEnumgroup', back_populates='reference_enumentry')


class AuthGroupPermissions(Base):
    __tablename__ = 'auth_group_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['group_id'], ['auth_group.id'], deferrable=True, initially='DEFERRED', name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id'),
        ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], deferrable=True, initially='DEFERRED', name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm'),
        PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
        UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq'),
        Index('auth_group_permissions_group_id_b120cbf9', 'group_id'),
        Index('auth_group_permissions_permission_id_84c5c92e', 'permission_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    group_id: Mapped[int] = mapped_column(Integer)
    permission_id: Mapped[int] = mapped_column(Integer)

    group: Mapped['AuthGroup'] = relationship('AuthGroup', back_populates='auth_group_permissions')
    permission: Mapped['AuthPermission'] = relationship('AuthPermission', back_populates='auth_group_permissions')


class AuthUserUserPermissions(Base):
    __tablename__ = 'auth_user_user_permissions'
    __table_args__ = (
        ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], deferrable=True, initially='DEFERRED', name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm'),
        ForeignKeyConstraint(['user_id'], ['auth_user.id'], deferrable=True, initially='DEFERRED', name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id'),
        PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
        UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq'),
        Index('auth_user_user_permissions_permission_id_1fbb5f2c', 'permission_id'),
        Index('auth_user_user_permissions_user_id_a95ead1b', 'user_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer)
    permission_id: Mapped[int] = mapped_column(Integer)

    permission: Mapped['AuthPermission'] = relationship('AuthPermission', back_populates='auth_user_user_permissions')
    user: Mapped['AuthUser'] = relationship('AuthUser', back_populates='auth_user_user_permissions')


class ClassificationFunctionalcategoryCategories(Base):
    __tablename__ = 'classification_functionalcategory_categories'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], ondelete='RESTRICT', onupdate='CASCADE', name='classification_functionalcategory_categories_classification_cat'),
        ForeignKeyConstraint(['functionalcategory_id'], ['classification_functionalcategory.id'], ondelete='RESTRICT', onupdate='CASCADE', name='classification_functionalcategory_categories_classification_fun'),
        PrimaryKeyConstraint('id', name='classification_functionalcategory_categories_pk'),
        UniqueConstraint('functionalcategory_id', name='classification_functionalcategory_categories_unique'),
        Index('classification_functionalcategory_category_group_idx', 'category_id'),
        Index('classification_functionalcategory_funccat_group_idx', 'functionalcategory_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    functionalcategory_id: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[int] = mapped_column(Integer)

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='classification_functionalcategory_categories')
    functionalcategory: Mapped['ClassificationFunctionalcategory'] = relationship('ClassificationFunctionalcategory', back_populates='classification_functionalcategory_categories')


class ClassificationSubcategory(Base):
    __tablename__ = 'classification_subcategory'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], ondelete='RESTRICT', onupdate='CASCADE', name='classification_subcategory_classification_category_fk'),
        PrimaryKeyConstraint('id', name='classification_subcategory_pk'),
        Index('classification_subcategory_category_idx', 'category_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_id: Mapped[int] = mapped_column(Integer)

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='classification_subcategory')
    catalog_product: Mapped[List['CatalogProduct']] = relationship('CatalogProduct', back_populates='subcategory')
    catalog_configuration: Mapped[List['CatalogConfiguration']] = relationship('CatalogConfiguration', back_populates='subcategory')


class ConfiguratorConfiguratortemplate(Base):
    __tablename__ = 'configurator_configuratortemplate'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], ondelete='RESTRICT', onupdate='CASCADE', name='configurator_configuratortemplate_classification_category_fk'),
        PrimaryKeyConstraint('id', name='configurator_configuratortemplate_pk'),
        Index('configurator_configuratortemplate_category_group_idx', 'category_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    compatible_subcategories: Mapped[list] = mapped_column(ARRAY(String(length=30)))
    constraint_dsl: Mapped[dict] = mapped_column(JSONB)
    category_id: Mapped[int] = mapped_column(Integer)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='configurator_configuratortemplate')
    catalog_collection: Mapped[List['CatalogCollection']] = relationship('CatalogCollection', back_populates='template')
    configurator_moduletype: Mapped['ConfiguratorModuletype'] = relationship('ConfiguratorModuletype', uselist=False, back_populates='template')
    configurator_optiondefinition: Mapped['ConfiguratorOptiondefinition'] = relationship('ConfiguratorOptiondefinition', uselist=False, back_populates='template')


class CatalogCollection(Base):
    __tablename__ = 'catalog_collection'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_collection_classification_category_fk'),
        ForeignKeyConstraint(['pricing_strategy_id'], ['pricing_pricingstrategy.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_collection_pricing_pricingstrategy_fk'),
        ForeignKeyConstraint(['template_id'], ['configurator_configuratortemplate.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_collection_configurator_configuratortemplate_fk'),
        PrimaryKeyConstraint('id', name='catalog_collection_pk'),
        Index('catalog_collection_category_idx', 'category_id'),
        Index('catalog_collection_pricing_strategy_idx', 'pricing_strategy_id'),
        Index('catalog_collection_template_idx', 'template_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    defaults: Mapped[dict] = mapped_column(JSONB)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    pricing_strategy_id: Mapped[int] = mapped_column(Integer)
    category_id: Mapped[int] = mapped_column(Integer)
    template_id: Mapped[int] = mapped_column(Integer)

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='catalog_collection')
    pricing_strategy: Mapped['PricingPricingstrategy'] = relationship('PricingPricingstrategy', back_populates='catalog_collection')
    template: Mapped['ConfiguratorConfiguratortemplate'] = relationship('ConfiguratorConfiguratortemplate', back_populates='catalog_collection')
    catalog_product: Mapped[List['CatalogProduct']] = relationship('CatalogProduct', back_populates='collection')


class ConfiguratorModuletype(Base):
    __tablename__ = 'configurator_moduletype'
    __table_args__ = (
        ForeignKeyConstraint(['template_id'], ['configurator_configuratortemplate.id'], ondelete='RESTRICT', onupdate='CASCADE', name='configurator_moduletype_configurator_configuratortemplate_fk'),
        PrimaryKeyConstraint('id', name='configurator_moduletype_pk'),
        UniqueConstraint('template_id', name='configurator_moduletype_unique'),
        Index('configurator_moduletype_template_idx', 'template_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    code: Mapped[str] = mapped_column(String(30))
    shape: Mapped[str] = mapped_column(String(30))
    size_rule: Mapped[dict] = mapped_column(JSONB)
    extra_flags: Mapped[list] = mapped_column(ARRAY(String(length=30)))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    template_id: Mapped[int] = mapped_column(Integer)

    template: Mapped['ConfiguratorConfiguratortemplate'] = relationship('ConfiguratorConfiguratortemplate', back_populates='configurator_moduletype')
    catalog_section: Mapped[List['CatalogSection']] = relationship('CatalogSection', back_populates='module_type')


class ConfiguratorOptiondefinition(Base):
    __tablename__ = 'configurator_optiondefinition'
    __table_args__ = (
        ForeignKeyConstraint(['dict_group_id'], ['reference_enumgroup.id'], ondelete='RESTRICT', onupdate='CASCADE', name='configurator_optiondefinition_reference_enumgroup_fk'),
        ForeignKeyConstraint(['template_id'], ['configurator_configuratortemplate.id'], ondelete='RESTRICT', onupdate='CASCADE', name='configurator_optiondefinition_configurator_configuratortemplate'),
        PrimaryKeyConstraint('id', name='configurator_optiondefinition_pk'),
        UniqueConstraint('template_id', name='configurator_optiondefinition_unique'),
        Index('configurator_optiondefinition_dict_group_group_idx', 'dict_group_id'),
        Index('configurator_optiondefinition_template_group_idx', 'template_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    code: Mapped[str] = mapped_column(String(30))
    field_type: Mapped[str] = mapped_column(String(10))
    required: Mapped[bool] = mapped_column(Boolean)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    template_id: Mapped[int] = mapped_column(Integer)
    dict_group_id: Mapped[int] = mapped_column(Integer)
    roles: Mapped[Optional[list]] = mapped_column(ARRAY(String(length=30)))

    dict_group: Mapped['ReferenceEnumgroup'] = relationship('ReferenceEnumgroup', back_populates='configurator_optiondefinition')
    template: Mapped['ConfiguratorConfiguratortemplate'] = relationship('ConfiguratorConfiguratortemplate', back_populates='configurator_optiondefinition')


class CatalogProduct(Base):
    __tablename__ = 'catalog_product'
    __table_args__ = (
        ForeignKeyConstraint(['collection_id'], ['catalog_collection.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_product_catalog_collection_fk'),
        ForeignKeyConstraint(['subcategory_id'], ['classification_subcategory.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_product_classification_subcategory_fk'),
        PrimaryKeyConstraint('id', name='catalog_product_pk'),
        Index('catalog_product_collection_idx', 'collection_id'),
        Index('catalog_product_subcategory_idx', 'subcategory_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    allowed_section_counts: Mapped[list] = mapped_column(ARRAY(SmallInteger()))
    flags: Mapped[dict] = mapped_column(JSONB)
    attributes: Mapped[dict] = mapped_column(JSONB)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    collection_id: Mapped[int] = mapped_column(Integer)
    subcategory_id: Mapped[Optional[int]] = mapped_column(Integer)

    collection: Mapped['CatalogCollection'] = relationship('CatalogCollection', back_populates='catalog_product')
    subcategory: Mapped[Optional['ClassificationSubcategory']] = relationship('ClassificationSubcategory', back_populates='catalog_product')
    catalog_configuration: Mapped[List['CatalogConfiguration']] = relationship('CatalogConfiguration', back_populates='product')
    catalog_mediaasset: Mapped[List['CatalogMediaasset']] = relationship('CatalogMediaasset', back_populates='product')


class CatalogConfiguration(Base):
    __tablename__ = 'catalog_configuration'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['catalog_product.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_configuration_catalog_product_fk'),
        ForeignKeyConstraint(['subcategory_id'], ['classification_subcategory.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_configuration_classification_subcategory_fk'),
        PrimaryKeyConstraint('id', name='catalog_configuration_pk'),
        Index('catalog_configuration_product_idx', 'product_id'),
        Index('catalog_configuration_subcat_idx', 'subcategory_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    label: Mapped[str] = mapped_column(String(120))
    options_selected: Mapped[dict] = mapped_column(JSONB)
    product_id: Mapped[int] = mapped_column(Integer)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subcategory_id: Mapped[int] = mapped_column(Integer)

    product: Mapped['CatalogProduct'] = relationship('CatalogProduct', back_populates='catalog_configuration')
    subcategory: Mapped['ClassificationSubcategory'] = relationship('ClassificationSubcategory', back_populates='catalog_configuration')
    catalog_section: Mapped['CatalogSection'] = relationship('CatalogSection', uselist=False, back_populates='configuration')


class CatalogMediaasset(Base):
    __tablename__ = 'catalog_mediaasset'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['catalog_product.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_mediaasset_catalog_product_fk'),
        PrimaryKeyConstraint('id', name='catalog_mediaasset_pk'),
        Index('catalog_mediaasset_product_idx', 'product_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    url: Mapped[str] = mapped_column(String(200))
    tag: Mapped[str] = mapped_column(String(30))
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product_id: Mapped[int] = mapped_column(Integer)

    product: Mapped['CatalogProduct'] = relationship('CatalogProduct', back_populates='catalog_mediaasset')


class CatalogSection(Base):
    __tablename__ = 'catalog_section'
    __table_args__ = (
        CheckConstraint('index >= 0', name='catalog_section_index_check'),
        CheckConstraint('size_cm >= 0', name='catalog_section_size_cm_check'),
        ForeignKeyConstraint(['configuration_id'], ['catalog_configuration.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_section_catalog_configuration_fk'),
        ForeignKeyConstraint(['module_type_id'], ['configurator_moduletype.id'], ondelete='RESTRICT', onupdate='CASCADE', name='catalog_section_configurator_moduletype_fk'),
        PrimaryKeyConstraint('id', name='catalog_section_pk'),
        UniqueConstraint('configuration_id', name='catalog_section_unique'),
        Index('catalog_configuration_idx', 'configuration_id'),
        Index('catalog_section_module_type_id_2d7d07bb', 'module_type_id')
    )

    created_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            default=datetime.now(UTC),
        )
    updated_at: Mapped[datetime] = mapped_column(
            DateTime(timezone=True),
            onupdate=datetime.now(UTC), 
            default=datetime.now(UTC),
        )
    index: Mapped[int] = mapped_column(SmallInteger)
    size_cm: Mapped[int] = mapped_column(SmallInteger)
    flags: Mapped[dict] = mapped_column(JSONB)
    module_type_id: Mapped[int] = mapped_column(Integer)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    configuration_id: Mapped[int] = mapped_column(Integer)

    configuration: Mapped['CatalogConfiguration'] = relationship('CatalogConfiguration', back_populates='catalog_section')
    module_type: Mapped['ConfiguratorModuletype'] = relationship('ConfiguratorModuletype', back_populates='catalog_section')
