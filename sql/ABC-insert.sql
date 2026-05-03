insert into ABC
(
/*$SHAIN_CD*/     SHAIN_CD
/*$SHIMEI*/     , SHIMEI
/*$UMARE*/      , UMARE
/*$SEX*/        , SEX
)
values
(
/*$SHAIN_CD*/     :SHAIN_CD
/*$SHIMEI*/     , :SHIMEI
/*$UMARE*/      , TO_DATE(:UMARE, 'YYYY/MM/DD')
/*$SEX*/        , :SEX
)
