-------------------------------------------------------------------------------
-- chapter4/oml4sql_model_query.sql
-- OML4SQL로 생성된 모델, 예측값을 쿼리 
-------------------------------------------------------------------------------

select case_id "date", round(value,2) actual_cpu, round(prediction,2) forcast_cpu, round(lower,2) lower_bound, round(upper,2) upper_bound
 from  dm$vpocidemo_cpu_forecast
 order by 1 ;
