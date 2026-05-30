select
    SHAIN_CD AS 社員コード,
    SHIMEI AS 氏名,
    TO_CHAR(UMARE, 'YYYY/MM/DD') AS 生年月日,
    DECODE(SEX, '1', '男性', '2', '女性', '不明') AS 性別
from ABC
where 1=1
/*$SHAIN_CD*/       AND SHAIN_CD =    :SHAIN_CD
/*$SHIMEI*/         AND SHIMEI   =    :SHIMEI
/*$LIKE_SHIMEI*/    AND SHIMEI   LIKE :LIKE_SHIMEI
/*$UMARE*/          AND UMARE    =    TO_DATE(:UMARE, 'YYYY/MM/DD')
/*$UMARE_FROM*/     AND UMARE    >=   TO_DATE(:UMARE_FROM, 'YYYY/MM/DD')
/*$UMARE_TO*/       AND UMARE    <=   TO_DATE(:UMARE_TO, 'YYYY/MM/DD')
/*$SEX*/            AND SEX       =   :SEX
order by SHAIN_CD
