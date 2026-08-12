create table tbl ("abc" number, xxx varchar2(30))
/
select 'A' as FM, COM, SHAIN,    JN, decode(B.COM, NULL, 0, 1) as BEXISTS
   from TRAN_A -- 勤務実績テーブル(社員番号)休暇日数、
   inner join MAST_B -- 社員マスタ(社員の名前)兼務(別組織),出向(出向先の会社コード)
      on B.COM=A.COM   -- 会社マスタ(会社の名前)
      and B.JYUGYOIN=A.SHAIN
   left join MAST_C  -- 組織マスタ（組織コード、組織名、上長の番号)
      on B.COM=A.COM
      and B.JYUGYOIN=A.SHAIN
   inner join MAST_D -- 役職マスタ（役職名）
      on B.COM=A.COM
      and B.JYUGYOIN=A.SHAIN
where FM='A'
-- order by FM, COM, JN
order by 1, 3
/

/*
COM,   JN       BEXISTS
---    --       -----
A'CCC', '5333', 1
B'CCC', 'x333'  0

'KIC', '3333'
'KIC', '4333'
'KIC', '5333'
*/

select
col
from tbl
where rownum <= 10
/
--/*$名前*/   and  名前   = :名前
--/*$L名前*/   and  名前  LIKE '%'||:L名前||'%'
--/*$色*/     and  色     = :色
--/*$大きさ*/ and  大きさ = :大きさ
--/*$会社*/   and  会社   = :会社

select * from ABC
/

select * from SEISEKI
/