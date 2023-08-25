%script

------------------------------------------------------------------------------
-- chapter4/oml4sql_analysis.py
-- OML4SQL을 활용한 분석 스크립트, ADB의 OML노트북에서 호출
------------------------------------------------------------------------------


BEGIN dbms_data_mining.drop_model('ocidemo_cpu_forecast');
END;
/

DECLARE 
     v_setlst dbms_data_mining.SETTING_LIST;
BEGIN 
     v_setlst(dbms_data_mining.ALGO_NAME)  := dbms_data_mining.ALGO_EXPONENTIAL_SMOOTHING;
     v_setlst(dbms_data_mining.EXSM_INTERVAL) := dbms_data_mining.EXSM_INTERVAL_MONTH; 
     v_setlst(dbms_data_mining.EXSM_PREDICTION_STEP)  := '6';
     v_setlst(dbms_data_mining.EXSM_MODEL) := dbms_data_mining.EXSM_HOLT;
     v_setlst(dbms_data_mining.EXSM_ACCUMULATE) :=  dbms_data_mining.EXSM_ACCU_AVG;    
     
     dbms_data_mining.create_model2(
            model_name => 'ocidemo_cpu_forecast', mining_function => 'TIME_SERIES', data_query => 'select time,cpu from ocidemo_ml', set_list => v_setlst, case_id_column_name => 'TIME', target_column_name => 'CPU');
END;
/
