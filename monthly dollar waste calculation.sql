<?xml version="1.0" encoding="UTF-8"?><sqlb_project><db path="kubernetes.db" readonly="0" foreign_keys="1" case_sensitive_like="0" temp_store="0" wal_autocheckpoint="1000" synchronous="2"/><attached/><window><main_tabs open="structure browser pragmas query" current="3"/></window><tab_structure><column_width id="0" width="300"/><column_width id="1" width="0"/><column_width id="2" width="100"/><column_width id="3" width="1279"/><column_width id="4" width="0"/><expanded_item id="0" parent="1"/><expanded_item id="1" parent="1"/><expanded_item id="2" parent="1"/><expanded_item id="3" parent="1"/></tab_structure><tab_browse><table title="cluster_metrics" custom_title="0" dock_id="1" table="4,15:maincluster_metrics"/><dock_state state="000000ff00000000fd0000000100000002000002480000020bfc0100000001fb000000160064006f0063006b00420072006f00770073006500310100000000000002480000012d00ffffff000002480000000000000004000000040000000800000008fc00000000"/><default_encoding codec=""/><browse_table_settings><table schema="main" name="cluster_metrics" show_row_id="0" encoding="" plot_x_axis="" unlock_view_pk="_rowid_" freeze_columns="0"><sort/><column_widths><column index="1" value="85"/><column index="2" value="117"/><column index="3" value="163"/><column index="4" value="124"/><column index="5" value="91"/><column index="6" value="103"/><column index="7" value="116"/><column index="8" value="129"/></column_widths><filter_values/><conditional_formats/><row_id_formats/><display_formats/><hidden_columns/><plot_y_axes/><global_filter/></table></browse_table_settings></tab_browse><tab_sql><sql name="cpu and memory waste by each team" filename="C:/Users/AARTI YADAV/OneDrive/Desktop/kubernetes_finops/data/kubernetes_quiries.sql">-- Reference to file &quot;C:/Users/AARTI YADAV/OneDrive/Desktop/kubernetes_finops/data/kubernetes_quiries.sql&quot; (not supported by this version) --</sql><sql name="monthaly dollar waste calculate">-- Har team ka monthly dollar waste nikalo

SELECT
    namespace,
    -- team ka naam

    ROUND(AVG(cpu_requested - cpu_actual_peak), 3) as cpu_waste_cores,
    -- CPU waste cores mein

    ROUND(AVG(memory_requested - memory_actual_peak), 3) as mem_waste_gb,
    -- Memory waste GB mein

    ROUND((AVG(cpu_actual_peak) / AVG(cpu_requested)) * 100, 1) as cpu_utilization_pct,
    -- CPU utilization % = (use kiya / manga) * 100
    -- agar 30% aa raha hai matlab 70% waste!

    ROUND((AVG(memory_actual_peak) / AVG(memory_requested)) * 100, 1) as mem_utilization_pct,
    -- Memory utilization %

    ROUND(AVG(cpu_requested - cpu_actual_peak) * 0.048 * 720, 2) as monthly_cpu_waste_usd,
    -- Monthly CPU waste dollars mein
    -- waste cores × $0.048 per core per hour × 720 hours (1 mahina)

    ROUND(AVG(memory_requested - memory_actual_peak) * 0.006 * 720, 2) as monthly_mem_waste_usd,
    -- Monthly Memory waste dollars mein
    -- waste GB × $0.006 per GB per hour × 720 hours

    ROUND(
        (AVG(cpu_requested - cpu_actual_peak) * 0.048 * 720) +
        (AVG(memory_requested - memory_actual_peak) * 0.006 * 720)
    , 2) as total_monthly_waste_usd
    -- Total waste = CPU waste + Memory waste

FROM cluster_metrics

GROUP BY namespace

ORDER BY total_monthly_waste_usd DESC;
-- sabse zyada waste karne wali team pehle</sql><current_tab id="0"/></tab_sql></sqlb_project>
