create or replace PROCEDURE SEISEKI_SUM
/*
    プロシージャ名: SEISEKI_SUM
    説明: 成績の集計を行うプロシージャ
    作成者: 浦新
    作成日: 2024-06-01
*/
IS
    -- 変数宣言部
    v_message VARCHAR2(50);
    v_math_sum NUMBER(3);
    v_english_sum NUMBER(3);
    v_japanese_sum NUMBER(3);
BEGIN
    -- 実行する処理（SQLやPL/SQL）
    v_message := 'Hello, Oracle!';
    DBMS_OUTPUT.PUT_LINE(v_message);
    for rec in (select * from SEISEKI) loop
        DBMS_OUTPUT.PUT_LINE('GAKUSEKI_NO: ' || rec.GAKUSEKI_NO || ', MATH_SCORE: ' || rec.MATH_SCORE ||
            ', ENGLISH_SCORE: ' || rec.ENGLISH_SCORE || ', JAPANESE_SCORE: ' || rec.JAPANESE_SCORE);
    end loop;
    select max(MATH_SCORE), max(ENGLISH_SCORE), max(JAPANESE_SCORE) into v_math_sum, v_english_sum, v_japanese_sum from SEISEKI;
    update SEISEKI_SUMMARY set MATH_SCORE = v_math_sum, ENGLISH_SCORE = v_english_sum, JAPANESE_SCORE = v_japanese_sum where KIND='MAX';
END SEISEKI_SUM;