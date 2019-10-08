tables_definition = """SELECT OBJECT_NAME(c.object_id) as 'table_name',
                              c.name 'column_name',
                              t.Name 'data_type',
                              c.max_length 'max_length',
                              c.precision ,
                              c.scale ,
                              c.is_nullable,
                              ISNULL(i.is_primary_key, 0) 'primary_key'
                         FROM sys.columns c
                   INNER JOIN sys.types t ON c.user_type_id = t.user_type_id
              LEFT OUTER JOIN sys.index_columns ic ON ic.object_id = c.object_id AND ic.column_id = c.column_id
              LEFT OUTER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
                        WHERE OBJECT_NAME(c.object_id) in ({tables}) """