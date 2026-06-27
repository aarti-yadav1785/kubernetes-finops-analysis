-- Har namespace (team) ka average CPU aur Memory waste nikalo

SELECT 
    namespace,
    -- team ka naam

    COUNT(DISTINCT pod_name) as total_pods,
    -- kitne pods hain us team mein

    ROUND(AVG(cpu_requested), 3) as avg_cpu_requested,
    -- average CPU jo manga

    ROUND(AVG(cpu_actual_peak), 3) as avg_cpu_used,
    -- average CPU jo actually use hua

    ROUND(AVG(cpu_requested - cpu_actual_peak), 3) as avg_cpu_waste,
    -- CPU waste = manga - use kiya

    ROUND(AVG(memory_requested), 3) as avg_mem_requested,
    -- average memory jo mangi

    ROUND(AVG(memory_actual_peak), 3) as avg_mem_used,
    -- average memory jo actually use hui

    ROUND(AVG(memory_requested - memory_actual_peak), 3) as avg_mem_waste
    -- memory waste = mangi - use ki

FROM cluster_metrics

GROUP BY namespace
-- har team ke liye alag calculate karo

ORDER BY avg_cpu_waste DESC;
-- sabse zyada waste karne wali team pehle