select
    SHAIN_CD,
    SSK_CD,
    KBN
from ZOKU
where 1=1
/*$SHAIN_CD*/ AND SHAIN_CD = :SHAIN_CD
/*$SSK_CD*/   AND SSK_CD   = :SSK_CD
/*$KBN*/      AND KBN      = :KBN
