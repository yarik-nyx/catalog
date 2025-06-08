from typing import List, Optional

from sqlalchemy import ARRAY, BigInteger, Boolean, CheckConstraint, DateTime, ForeignKeyConstraint, Identity, Index, Integer, Numeric, PrimaryKeyConstraint, SmallInteger, String, Text, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedAsDataclass, mapped_column, relationship
import datetime
import decimal
from core.models.base_class import Base

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
    date_joined: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    last_login: Mapped[Optional[datetime.datetime]] = mapped_column(DateTime(True))

    auth_user_groups: Mapped[List['AuthUserGroups']] = relationship('AuthUserGroups', back_populates='user')
    django_admin_log: Mapped[List['DjangoAdminLog']] = relationship('DjangoAdminLog', back_populates='user')
    auth_user_user_permissions: Mapped[List['AuthUserUserPermissions']] = relationship('AuthUserUserPermissions', back_populates='user')


class ClassificationFunctionalcategory(Base):
    __tablename__ = 'classification_functionalcategory'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='classification_functionalcategory_pkey'),
        Index('classification_functionalcategory_id_c21b6f36_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))

    classification_functionalcategory_categories: Mapped[List['ClassificationFunctionalcategoryCategories']] = relationship('ClassificationFunctionalcategoryCategories', back_populates='functionalcategory')


class ClassificationGroup(Base):
    __tablename__ = 'classification_group'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='classification_group_pkey'),
        Index('classification_group_id_93829d14_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))

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
    applied: Mapped[datetime.datetime] = mapped_column(DateTime(True))


class DjangoSession(Base):
    __tablename__ = 'django_session'
    __table_args__ = (
        PrimaryKeyConstraint('session_key', name='django_session_pkey'),
        Index('django_session_expire_date_a5c62663', 'expire_date'),
        Index('django_session_session_key_c0390e0f_like', 'session_key')
    )

    session_key: Mapped[str] = mapped_column(String(40), primary_key=True)
    session_data: Mapped[str] = mapped_column(Text)
    expire_date: Mapped[datetime.datetime] = mapped_column(DateTime(True))


class PricingPricingstrategy(Base):
    __tablename__ = 'pricing_pricingstrategy'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='pricing_pricingstrategy_pkey'),
        Index('pricing_pricingstrategy_id_b1ec80e3_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    engine: Mapped[str] = mapped_column(String(120))
    parameters: Mapped[dict] = mapped_column(JSONB)

    catalog_collection: Mapped[List['CatalogCollection']] = relationship('CatalogCollection', back_populates='pricing_strategy')


class ReferenceEnumgroup(Base):
    __tablename__ = 'reference_enumgroup'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='reference_enumgroup_pkey'),
        Index('reference_enumgroup_id_3dfd9b30_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(30), primary_key=True)

    reference_enumentry: Mapped[List['ReferenceEnumentry']] = relationship('ReferenceEnumentry', back_populates='group')
    configurator_optiondefinition: Mapped[List['ConfiguratorOptiondefinition']] = relationship('ConfiguratorOptiondefinition', back_populates='dict_group')


class ReferenceUnitofmeasure(Base):
    __tablename__ = 'reference_unitofmeasure'
    __table_args__ = (
        CheckConstraint('"precision" >= 0', name='reference_unitofmeasure_precision_check'),
        PrimaryKeyConstraint('id', name='reference_unitofmeasure_pkey'),
        Index('reference_unitofmeasure_id_ad4f0d6e_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
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
        ForeignKeyConstraint(['group_id'], ['classification_group.id'], deferrable=True, initially='DEFERRED', name='classification_categ_group_id_712bed98_fk_classific'),
        PrimaryKeyConstraint('id', name='classification_category_pkey'),
        Index('classification_category_group_id_712bed98', 'group_id'),
        Index('classification_category_group_id_712bed98_like', 'group_id'),
        Index('classification_category_id_b059b8db_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    group_id: Mapped[str] = mapped_column(String(30))

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
    action_time: Mapped[datetime.datetime] = mapped_column(DateTime(True))
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
        ForeignKeyConstraint(['group_id'], ['reference_enumgroup.id'], deferrable=True, initially='DEFERRED', name='reference_enumentry_group_id_4bc9d56a_fk_reference_enumgroup_id'),
        PrimaryKeyConstraint('id', name='reference_enumentry_pkey'),
        Index('reference_enumentry_group_id_4bc9d56a', 'group_id'),
        Index('reference_enumentry_group_id_4bc9d56a_like', 'group_id'),
        Index('reference_enumentry_id_82c30a71_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    extra_price: Mapped[decimal.Decimal] = mapped_column(Numeric(9, 2))
    group_id: Mapped[str] = mapped_column(String(30))
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
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], deferrable=True, initially='DEFERRED', name='classification_funct_category_id_8da9c8c5_fk_classific'),
        ForeignKeyConstraint(['functionalcategory_id'], ['classification_functionalcategory.id'], deferrable=True, initially='DEFERRED', name='classification_funct_functionalcategory_i_030d04b3_fk_classific'),
        PrimaryKeyConstraint('id', name='classification_functionalcategory_categories_pkey'),
        UniqueConstraint('functionalcategory_id', 'category_id', name='classification_functiona_functionalcategory_id_ca_99ee9057_uniq'),
        Index('classification_functiona_category_id_8da9c8c5_like', 'category_id'),
        Index('classification_functiona_functionalcategory_id_030d04b3_like', 'functionalcategory_id'),
        Index('classification_functionalc_category_id_8da9c8c5', 'category_id'),
        Index('classification_functionalc_functionalcategory_id_030d04b3', 'functionalcategory_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    functionalcategory_id: Mapped[str] = mapped_column(String(30))
    category_id: Mapped[str] = mapped_column(String(30))

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='classification_functionalcategory_categories')
    functionalcategory: Mapped['ClassificationFunctionalcategory'] = relationship('ClassificationFunctionalcategory', back_populates='classification_functionalcategory_categories')


class ClassificationSubcategory(Base):
    __tablename__ = 'classification_subcategory'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], deferrable=True, initially='DEFERRED', name='classification_subca_category_id_4ce6fd71_fk_classific'),
        PrimaryKeyConstraint('id', name='classification_subcategory_pkey'),
        Index('classification_subcategory_category_id_4ce6fd71', 'category_id'),
        Index('classification_subcategory_category_id_4ce6fd71_like', 'category_id'),
        Index('classification_subcategory_id_ed16b667_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    category_id: Mapped[str] = mapped_column(String(30))

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='classification_subcategory')
    catalog_product: Mapped[List['CatalogProduct']] = relationship('CatalogProduct', back_populates='subcategory')
    catalog_configuration: Mapped[List['CatalogConfiguration']] = relationship('CatalogConfiguration', back_populates='subcategory')


class ConfiguratorConfiguratortemplate(Base):
    __tablename__ = 'configurator_configuratortemplate'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], deferrable=True, initially='DEFERRED', name='configurator_configu_category_id_e3598cb3_fk_classific'),
        PrimaryKeyConstraint('id', name='configurator_configuratortemplate_pkey'),
        Index('configurator_configuratortemplate_category_id_e3598cb3', 'category_id'),
        Index('configurator_configuratortemplate_category_id_e3598cb3_like', 'category_id'),
        Index('configurator_configuratortemplate_id_4f9df2fe_like', 'id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    compatible_subcategories: Mapped[list] = mapped_column(ARRAY(String(length=30)))
    constraint_dsl: Mapped[dict] = mapped_column(JSONB)
    category_id: Mapped[str] = mapped_column(String(30))

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='configurator_configuratortemplate')
    catalog_collection: Mapped[List['CatalogCollection']] = relationship('CatalogCollection', back_populates='template')
    configurator_moduletype: Mapped[List['ConfiguratorModuletype']] = relationship('ConfiguratorModuletype', back_populates='template')
    configurator_optiondefinition: Mapped[List['ConfiguratorOptiondefinition']] = relationship('ConfiguratorOptiondefinition', back_populates='template')


class CatalogCollection(Base):
    __tablename__ = 'catalog_collection'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['classification_category.id'], deferrable=True, initially='DEFERRED', name='catalog_collection_category_id_c4160d03_fk_classific'),
        ForeignKeyConstraint(['pricing_strategy_id'], ['pricing_pricingstrategy.id'], deferrable=True, initially='DEFERRED', name='catalog_collection_pricing_strategy_id_36dec0fa_fk_pricing_p'),
        ForeignKeyConstraint(['template_id'], ['configurator_configuratortemplate.id'], deferrable=True, initially='DEFERRED', name='catalog_collection_template_id_deef7965_fk_configura'),
        PrimaryKeyConstraint('id', name='catalog_collection_pkey'),
        Index('catalog_collection_category_id_c4160d03', 'category_id'),
        Index('catalog_collection_category_id_c4160d03_like', 'category_id'),
        Index('catalog_collection_id_3c887ce7_like', 'id'),
        Index('catalog_collection_pricing_strategy_id_36dec0fa', 'pricing_strategy_id'),
        Index('catalog_collection_pricing_strategy_id_36dec0fa_like', 'pricing_strategy_id'),
        Index('catalog_collection_template_id_deef7965', 'template_id'),
        Index('catalog_collection_template_id_deef7965_like', 'template_id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(30), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    defaults: Mapped[dict] = mapped_column(JSONB)
    category_id: Mapped[str] = mapped_column(String(30))
    pricing_strategy_id: Mapped[str] = mapped_column(String(40))
    template_id: Mapped[str] = mapped_column(String(40))

    category: Mapped['ClassificationCategory'] = relationship('ClassificationCategory', back_populates='catalog_collection')
    pricing_strategy: Mapped['PricingPricingstrategy'] = relationship('PricingPricingstrategy', back_populates='catalog_collection')
    template: Mapped['ConfiguratorConfiguratortemplate'] = relationship('ConfiguratorConfiguratortemplate', back_populates='catalog_collection')
    catalog_product: Mapped[List['CatalogProduct']] = relationship('CatalogProduct', back_populates='collection')


class ConfiguratorModuletype(Base):
    __tablename__ = 'configurator_moduletype'
    __table_args__ = (
        ForeignKeyConstraint(['template_id'], ['configurator_configuratortemplate.id'], deferrable=True, initially='DEFERRED', name='configurator_modulet_template_id_bb5d1316_fk_configura'),
        PrimaryKeyConstraint('id', name='configurator_moduletype_pkey'),
        UniqueConstraint('template_id', 'code', name='configurator_moduletype_template_id_code_15f9e836_uniq'),
        Index('configurator_moduletype_template_id_bb5d1316', 'template_id'),
        Index('configurator_moduletype_template_id_bb5d1316_like', 'template_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    code: Mapped[str] = mapped_column(String(30))
    shape: Mapped[str] = mapped_column(String(30))
    size_rule: Mapped[dict] = mapped_column(JSONB)
    extra_flags: Mapped[list] = mapped_column(ARRAY(String(length=30)))
    template_id: Mapped[str] = mapped_column(String(40))

    template: Mapped['ConfiguratorConfiguratortemplate'] = relationship('ConfiguratorConfiguratortemplate', back_populates='configurator_moduletype')
    catalog_section: Mapped[List['CatalogSection']] = relationship('CatalogSection', back_populates='module_type')


class ConfiguratorOptiondefinition(Base):
    __tablename__ = 'configurator_optiondefinition'
    __table_args__ = (
        ForeignKeyConstraint(['dict_group_id'], ['reference_enumgroup.id'], deferrable=True, initially='DEFERRED', name='configurator_optiond_dict_group_id_5a010d3c_fk_reference'),
        ForeignKeyConstraint(['template_id'], ['configurator_configuratortemplate.id'], deferrable=True, initially='DEFERRED', name='configurator_optiond_template_id_ddd07ed4_fk_configura'),
        PrimaryKeyConstraint('id', name='configurator_optiondefinition_pkey'),
        UniqueConstraint('template_id', 'code', name='configurator_optiondefinition_template_id_code_8e7d84d0_uniq'),
        Index('configurator_optiondefinition_dict_group_id_5a010d3c', 'dict_group_id'),
        Index('configurator_optiondefinition_dict_group_id_5a010d3c_like', 'dict_group_id'),
        Index('configurator_optiondefinition_template_id_ddd07ed4', 'template_id'),
        Index('configurator_optiondefinition_template_id_ddd07ed4_like', 'template_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    code: Mapped[str] = mapped_column(String(30))
    field_type: Mapped[str] = mapped_column(String(10))
    required: Mapped[bool] = mapped_column(Boolean)
    template_id: Mapped[str] = mapped_column(String(40))
    roles: Mapped[Optional[list]] = mapped_column(ARRAY(String(length=30)))
    dict_group_id: Mapped[Optional[str]] = mapped_column(String(30))

    dict_group: Mapped[Optional['ReferenceEnumgroup']] = relationship('ReferenceEnumgroup', back_populates='configurator_optiondefinition')
    template: Mapped['ConfiguratorConfiguratortemplate'] = relationship('ConfiguratorConfiguratortemplate', back_populates='configurator_optiondefinition')


class CatalogProduct(Base):
    __tablename__ = 'catalog_product'
    __table_args__ = (
        ForeignKeyConstraint(['collection_id'], ['catalog_collection.id'], deferrable=True, initially='DEFERRED', name='catalog_product_collection_id_ddea8d85_fk_catalog_collection_id'),
        ForeignKeyConstraint(['subcategory_id'], ['classification_subcategory.id'], deferrable=True, initially='DEFERRED', name='catalog_product_subcategory_id_b1a50afa_fk_classific'),
        PrimaryKeyConstraint('id', name='catalog_product_pkey'),
        Index('catalog_product_collection_id_ddea8d85', 'collection_id'),
        Index('catalog_product_collection_id_ddea8d85_like', 'collection_id'),
        Index('catalog_product_id_6a6f4293_like', 'id'),
        Index('catalog_product_subcategory_id_b1a50afa', 'subcategory_id'),
        Index('catalog_product_subcategory_id_b1a50afa_like', 'subcategory_id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    allowed_section_counts: Mapped[list] = mapped_column(ARRAY(SmallInteger()))
    flags: Mapped[dict] = mapped_column(JSONB)
    attributes: Mapped[dict] = mapped_column(JSONB)
    collection_id: Mapped[str] = mapped_column(String(30))
    subcategory_id: Mapped[Optional[str]] = mapped_column(String(30))

    collection: Mapped['CatalogCollection'] = relationship('CatalogCollection', back_populates='catalog_product')
    subcategory: Mapped[Optional['ClassificationSubcategory']] = relationship('ClassificationSubcategory', back_populates='catalog_product')
    catalog_configuration: Mapped[List['CatalogConfiguration']] = relationship('CatalogConfiguration', back_populates='product')
    catalog_mediaasset: Mapped[List['CatalogMediaasset']] = relationship('CatalogMediaasset', back_populates='product')


class CatalogConfiguration(Base):
    __tablename__ = 'catalog_configuration'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['catalog_product.id'], deferrable=True, initially='DEFERRED', name='catalog_configuration_product_id_e9c42209_fk_catalog_product_id'),
        ForeignKeyConstraint(['subcategory_id'], ['classification_subcategory.id'], deferrable=True, initially='DEFERRED', name='catalog_configuratio_subcategory_id_17f1c83b_fk_classific'),
        PrimaryKeyConstraint('id', name='catalog_configuration_pkey'),
        Index('catalog_configuration_id_f510e364_like', 'id'),
        Index('catalog_configuration_product_id_e9c42209', 'product_id'),
        Index('catalog_configuration_product_id_e9c42209_like', 'product_id'),
        Index('catalog_configuration_subcategory_id_17f1c83b', 'subcategory_id'),
        Index('catalog_configuration_subcategory_id_17f1c83b_like', 'subcategory_id')
    )

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    id: Mapped[str] = mapped_column(String(50), primary_key=True)
    label: Mapped[str] = mapped_column(String(120))
    options_selected: Mapped[dict] = mapped_column(JSONB)
    subcategory_id: Mapped[str] = mapped_column(String(30))
    product_id: Mapped[str] = mapped_column(String(40))

    product: Mapped['CatalogProduct'] = relationship('CatalogProduct', back_populates='catalog_configuration')
    subcategory: Mapped['ClassificationSubcategory'] = relationship('ClassificationSubcategory', back_populates='catalog_configuration')
    catalog_section: Mapped[List['CatalogSection']] = relationship('CatalogSection', back_populates='configuration')


class CatalogMediaasset(Base):
    __tablename__ = 'catalog_mediaasset'
    __table_args__ = (
        ForeignKeyConstraint(['product_id'], ['catalog_product.id'], deferrable=True, initially='DEFERRED', name='catalog_mediaasset_product_id_688c3afe_fk_catalog_product_id'),
        PrimaryKeyConstraint('id', name='catalog_mediaasset_pkey'),
        Index('catalog_mediaasset_product_id_688c3afe', 'product_id'),
        Index('catalog_mediaasset_product_id_688c3afe_like', 'product_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    url: Mapped[str] = mapped_column(String(200))
    tag: Mapped[str] = mapped_column(String(30))
    product_id: Mapped[str] = mapped_column(String(40))

    product: Mapped['CatalogProduct'] = relationship('CatalogProduct', back_populates='catalog_mediaasset')


class CatalogSection(Base):
    __tablename__ = 'catalog_section'
    __table_args__ = (
        CheckConstraint('index >= 0', name='catalog_section_index_check'),
        CheckConstraint('size_cm >= 0', name='catalog_section_size_cm_check'),
        ForeignKeyConstraint(['configuration_id'], ['catalog_configuration.id'], deferrable=True, initially='DEFERRED', name='catalog_section_configuration_id_0a226347_fk_catalog_c'),
        ForeignKeyConstraint(['module_type_id'], ['configurator_moduletype.id'], deferrable=True, initially='DEFERRED', name='catalog_section_module_type_id_2d7d07bb_fk_configura'),
        PrimaryKeyConstraint('id', name='catalog_section_pkey'),
        UniqueConstraint('configuration_id', 'index', name='catalog_section_configuration_id_index_54f37387_uniq'),
        Index('catalog_section_configuration_id_0a226347', 'configuration_id'),
        Index('catalog_section_configuration_id_0a226347_like', 'configuration_id'),
        Index('catalog_section_module_type_id_2d7d07bb', 'module_type_id')
    )

    id: Mapped[int] = mapped_column(BigInteger, Identity(start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), primary_key=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime(True))
    index: Mapped[int] = mapped_column(SmallInteger)
    size_cm: Mapped[int] = mapped_column(SmallInteger)
    flags: Mapped[dict] = mapped_column(JSONB)
    configuration_id: Mapped[str] = mapped_column(String(50))
    module_type_id: Mapped[int] = mapped_column(BigInteger)

    configuration: Mapped['CatalogConfiguration'] = relationship('CatalogConfiguration', back_populates='catalog_section')
    module_type: Mapped['ConfiguratorModuletype'] = relationship('ConfiguratorModuletype', back_populates='catalog_section')
