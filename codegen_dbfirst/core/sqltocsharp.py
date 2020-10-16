def get_type(sql_date_type, is_nullable):
     nullable = ''
     if True == is_nullable:
         nullable = '?'
         
     if 'int' == sql_date_type:
         return 'int' + nullable
     elif 'varchar' in sql_date_type:
         return 'string'
     elif 'float' == sql_date_type:
         return 'double' + nullable
     elif 'decimal' == sql_date_type:
         return 'decimal' + nullable
     elif 'datetime' == sql_date_type:
         return 'System.DateTime' + nullable
     elif 'datetime2' == sql_date_type:
         return 'System.DateTime' + nullable
     elif 'bit' == sql_date_type:
         return 'bool' + nullable
     elif 'bigint' == sql_date_type:
         return 'bigint' + nullable
     return 'UNSUPPROTED'

def get_configuration(data_type, is_nullable, max_length, primary_key):
    field = '.HasColumnType("{}")'.format(data_type)

    if 'varchar' == data_type:
        field += ".HasMaxLength({})".format(max_length)

    if True == is_nullable:
        field += ".IsOptional()"
    else:
        field += ".IsRequired()"

    if True == primary_key:
        field += ".HasDatabaseGeneratedOption(DatabaseGeneratedOption.Identity)"

    return field
