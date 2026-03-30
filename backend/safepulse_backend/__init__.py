import pymysql

pymysql.version_info = (2, 2, 1, 'final', 0)
pymysql.install_as_MySQLdb()

# Patch for Django's MariaDB version check
try:
    from django.db.backends.mysql.base import DatabaseWrapper
    DatabaseWrapper.check_database_version_supported = lambda self: None
    
    # Bypass RETURNING clause for older MariaDB
    from django.db.backends.mysql.features import DatabaseFeatures
    DatabaseFeatures.can_return_rows_from_bulk_insert = property(lambda self: False)
    DatabaseFeatures.can_return_columns_from_insert = property(lambda self: False)
except ImportError:
    pass
