insert into OPERATE_LOG
(
/*$USE_TABLE*/        USE_TABLE
/*$OPERATION*/      , OPERATION
/*$KEYS*/           , KEYS
/*$RESULT*/         , RESULT
/*$OPERATION_USER*/ , OPERATION_USER
)
values
(
/*$USE_TABLE*/        :USE_TABLE
/*$OPERATION*/      , :OPERATION
/*$KEYS*/           , :KEYS
/*$RESULT*/         , :RESULT
/*$OPERATION_USER*/ , :OPERATION_USER
)
