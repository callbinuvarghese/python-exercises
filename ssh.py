The following is a proposal to implement filters.

The main filetype view may comprise of 100s of columns.
Many of the columns need to be filtered on some simple logic.
For example
    CommonClaims.epic_cd = I 
    CommonClaims.gender != Male|Female|Other|NuLL - SELECT 'M', 'MALE' UNITON  SELECT 'F', 'FEMALE'
    CommonClaims.provider_state IN ('PA','WY') - SELECT STATE_CD, STATE FROM STATES; SELECT DISTINCT STATE_CD,STATE FROM CommonClaims.provider_state
    The above condtion is very simple and does not involve any join. So there need be additional metadata in driver tables to be configured to perform the filtering.
Some of the columns selecttion criteria is complex that involves other intermediate tables
    For example
        SELECT CommonClaims.eamie_id, CommonClaims.line
          FROM MKT.CLPSH
        INNER JOIN CommonClaims.GROUP_ID = CLNT_CLH.GROUP_ID
        WHERE CLNT_CLH.CL_N = '281129' -- Client Number as paramter = and IN operator switch etc..)
        SELECT DISTINCT GRP_CLH.CL_N     GROUP_NUMBER
  FROM (SELECT *
          FROM MKT.CLPSH
         WHERE     BPD_ID in (18)
               AND CLPS_STUS_C = 'A'
               AND CLPS_MKT_STUS_C = 100
               ) GRP_CLPSH
       JOIN
       (SELECT *
          FROM MKT.CLH
         WHERE     CL_STUS_C = 'A'
               AND CL_MKT_STUS_C = 100
               )
       GRP_CLH
           ON GRP_CLH.CL_ID = GRP_CLPSH.CL_ID
       JOIN MKT.CLCLA CLCLA
           ON     GRP_CLH.CL_ID = CLCLA.CL_ID
              AND CLCLA.CLCLA_STUS_C = 'A'
              AND CLCLA.CLCLA_TYP_C = 104
       JOIN
       (SELECT *
          FROM MKT.CLH
         WHERE     CL_STUS_C = 'A'
               )
       CLNT_CLH
           ON CLNT_CLH.CL_ID = CLCLA.PARN_CL_ID
WHERE CLNT_CLH.CL_N = '281129'
    The above scnerarios is clearly a driver and it needs to be implemented using complex SQLs and therefore the current implmentation of driver view is suitable.
To reduce confusion between the above two scenarios, let us use the terminology 'Filter' from 'Driver'.
Filters can easily be implemented on any column of the file type.
Filters can be further enhanced by allowing the user to pick the filtered values from a picklist of the column in UI and also allow users to apply the condition operator accoriding to the need.

Filters can only be applied to the columns present in columns present in the FileType.
It is better to use the column definition section of the extract to provide  values for filtering.
If you want to filter on a column that is not included in the file. Then you can select that column and define the filter for the column and then mark the column as hidden. In this case the filter is applied with column values, but the column is not included in the file creation.

On the filter definition UI for a column, the user should be able to select the operator (= !-, > !> etc) identical to the current driver criteria.

On the filter definition UI for a column, the user shall also select the values from a picklist of values for that column. For example, if the user select gender column on CommonClaims. Then the picklist can display the list as SELECT DISTINCT CommonClaims.gender FROM CommonClaims WHERE partition_key_date_logic_condition. Notice the partition key logic used here, otherwise the query will take unpredictable time.

The filter criteria could be added to the SELECT logic while the execution engine is performing the SELECT query for preparing staging table as in the following example.
    SELECT col1, col2, cols_selected.. 
    FROM CommonClaims
    WHERE
        CommonClaime.pk in (pkDriverList)
    AND
        CommonClaims.coln > 5
    AND
        CommonClaims.epic_cd IN ('I', 'P')    



[1:54 PM] Conti, David T (Highmark Health)




driver_view







[2:14 PM] Conti, David T (Highmark Health)




INSERT INTO lcef_rule.extract_driver_param(

    extract_driver_param_id, driver_param_id, extract_reg_id, driver_param_vals_count, driver_param_vals_csv, driver_param_operator, include_ind, audit_insert_ts, audit_last_upd_ts, audit_username)

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);







[2:14 PM] Conti, David T (Highmark Health)




INSERT INTO lcef_rule.driver_view(

    driver_view_id, driver_default_sql, driver_seq_num, driver_pass_num, audit_insert_ts, audit_last_upd_ts, audit_username, driver_view_name, select_column, project_file_type_id, driver_view_short_name)

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);







[2:15 PM] Conti, David T (Highmark Health)




main.edw_asnd_bpd_id
main.mexced_ld_start_dt
main.mexced_ld_end_dt
eual_enroll.cl_n
eual_main.source_file_id

--Columns that need drivers
edw_asnd_bpd_id
mexced_ld_start_dt
mexced_ld_end_dt
cl_n
source_file_id

-- All drivers can use the same view as EE is appending the dynamic WHERE clause
CREATE VIEW dv_commonclaims_generic as
SELECT
eamie_id, line_blind_key
FROM CommonClaims
--WHERE edw_asnd_bpd_id @oper @BPD_ID -- not used exec engine to prepare the where clause

INSERT INTO lcef_rule.driver_view(
    driver_view_id, 
    driver_default_sql, driver_seq_num, driver_pass_num, 
    driver_view_name, select_column, 
    project_file_type_id, 
    driver_view_short_name)
VALUES (
    nextid() -- get the next id 
    '', 1, 1,  --
    'schema.dv_commonclaims_generic', 'edw_asnd_bpd_id', 
    project_file_type_id('commonclaims')
    'bpd_id');
INSERT INTO lcef_rule.driver_view(
    driver_view_id, 
    driver_default_sql, driver_seq_num, driver_pass_num, 
    driver_view_name, select_column, 
    project_file_type_id, 
    driver_view_short_name)
VALUES (
    nextid()
    '', 2, 1, 
    'schema.dv_commonclaims_generic', 'mexced_ld_start_dt', 
    project_file_type_id('commonclaims')
    'mexced_ld_start_dt');
INSERT INTO lcef_rule.driver_view(
    driver_view_id, 
    driver_default_sql, driver_seq_num, driver_pass_num, 
    driver_view_name, select_column, 
    project_file_type_id, 
    driver_view_short_name)
VALUES (
    nextid()
    '', 3, 1, 
    'schema.dv_commonclaims_generic', 'mexced_ld_end_dt', 
    project_file_type_id('commonclaims')
    'mexced_ld_end_dt');
INSERT INTO lcef_rule.driver_view(
    driver_view_id, 
    driver_default_sql, driver_seq_num, driver_pass_num, 
    driver_view_name, select_column, 
    project_file_type_id, 
    driver_view_short_name)
VALUES (
    nextid()
    '', 4, 1, 
    'schema.dv_commonclaims_generic', 'cl_n', 
    project_file_type_id('commonclaims')
    'cl_n');
INSERT INTO lcef_rule.driver_view(
    driver_view_id, 
    driver_default_sql, driver_seq_num, driver_pass_num, 
    driver_view_name, select_column, 
    project_file_type_id, 
    driver_view_short_name)
VALUES (
    nextid()
    '', 5, 1, 
    'schema.dv_commonclaims_generic', 'source_file_id', 
    project_file_type_id('commonclaims')
    'source_file_id');


TENV1: evpssht1.highmark.com#15001
TENV3: evpssht3.highmark.com#15001
TENV5: evpssht5.highmark.com#15005
TENV7: evpssht7.highmark.com#15001
TENVA: evpsshta.highmark.com#15001
TENVB: evpsshtb.highmark.com#15001
TENVC: evpsshtc.highmark.com#15001
TENVT: evpsshtt.highmark.com#15009
TENV2: lnbrwasd04.highmark.com#15001
TENV4: lnbrwasd06.highmark.com#15001
TENV6: lnbrwasd05.highmark.com#15001
TENVD: lnbrwasd07.highmark.com#15001
TENVE: lnbrwasd08.highmark.com#15001

has context menu
Compose


Denodo Driver View Parameterization


INSERT INTO lcef_rule.driver_view(driver_view_id, driver_default_sql,driver_seq_num, driver_pass_num, 
driver_view_name, select_column, project_file_type_id, driver_view_short_name)
VALUES (
default ,'select eamee_id, line_blind_key from dept_lcef."main_dv" where edw_asnd_bpd_id &{bpd_id_parm_op} &{bpd_id_parm_val}',1, 1,  
'main_dv_bpd_id', 'edw_asnd_bpd_id', 
select project_file_type_id from FROM lcef_rule.project_file_type where file_type='COMMON_CLAIMS_STANDARD_2'
'bpd_id');

INSERT INTO lcef_rule.driver_param(driver_param_id, driver_view_id, param_name, ft_col_name, seq_num, data_type,  value_select_method, value_sql  ) 
VALUES (DEFAULT, SELECT SELECT driver_view_id  FROM lcef_rule.driver_view WHERE DRIVER_VIEW_NAME='main_dv_bpd_id',
'bpd_id_parm', 'edw_asnd_bpd_id', 1, 'text', 'pick','select distinct edw_asnd_bpd_id from dept_lcef."main_dv"');

INSERT INTO lcef_rule.driver_view(driver_view_id, driver_default_sql,driver_seq_num, driver_pass_num, 
driver_view_name, select_column, project_file_type_id, driver_view_short_name)
VALUES (
default ,'select eamee_id, line_blind_key from dept_lcef."main_dv" where MEXCED_LD_CYC_DT &{LoadCycleDate_parm_op} &{LoadCycleDate_parm_val}',2, 1,  
'main_dv_MEXCED_LD_CYC_DT', 'MEXCED_LD_CYC_DT', 
select project_file_type_id from FROM lcef_rule.project_file_type where file_type='COMMON_CLAIMS_STANDARD_2'
'LoadCycleDate');


INSERT INTO lcef_rule.driver_param(driver_param_id, driver_view_id, param_name, ft_col_name,
seq_num, data_type,  value_select_method, value_sql )
VALUES (DEFAULT, SELECT SELECT driver_view_id FROM lcef_rule.driver_view WHERE DRIVER_VIEW_NAME='main_dv_MEXCED_LD_CYC_DT',
'LoadCycleDate_parm', 'MEXCED_LD_CYC_DT', 1, 'date', 'single',NULL);

INSERT INTO lcef_rule.driver_view(driver_view_id, driver_default_sql,driver_seq_num, driver_pass_num, 
driver_view_name, select_column, project_file_type_id, driver_view_short_name)
VALUES (
default ,'select eamee_id, line_blind_key from dept_lcef."main_dv" where MEXCED_LD_CYC_DT &{EACFinalizeDate_parm_op} &{EACFinalizeDate_parm_val}',2, 1,  
'main_dv_EAC_FNLN_DT', 'edw_asnd_bpd_id', 
select project_file_type_id from FROM lcef_rule.project_file_type where file_type='COMMON_CLAIMS_STANDARD_2'
'EACFinalizeDate');

INSERT INTO lcef_rule.driver_param(driver_param_id, driver_view_id, param_name, ft_col_name,
seq_num, data_type,  value_select_method, value_sql )
VALUES (DEFAULT, SELECT SELECT driver_view_id FROM lcef_rule.driver_view WHERE DRIVER_VIEW_NAME='main_dv_EAC_FNLN_DT',
'EACFinalizeDate_parm_op', 'EAC_FNLN_DT', 1, 'date', 'single',NULL);

Departmental Store on Denodo/BigQuery

    LCEF need to store data in a database for its reporting outside of the enterprise data.
    There are several scenarios for it, few of examples are cited below.
        LCEF FSA extracts are prepared for the benefit processing agents and not for the clients directly.
        A benefit processing agent typically process data for multiple clients.
        The benefit processing agents to clients relationships are maintained in a table. 
        This table is currently maintained by the LCEF team on their departmental database.

        A particular extract needs to be prepared for a specific list of insured groups.
        The group codes are stored in a table for the client in a departmental database.
        At tome

        On rare occurrences, an extract needs to be prepared for a special scenario. 
        The person preparing the analysis needs to run several different queries from the enterprise
        data to come up with a list of eamie_ids after the analytic work.
        An extract needs to be prepared for just the specific eamie_ids selected by the analyst.
        The eamie_ids need to be uploaded and stored in a departmental table for the extract. 

    In essence, the need for a departmental database is to be fullfilled.


Denodo Interpolation String queries

    There is a need to put configurable conditions for the driver views
    An generic simple example of the query is as follows

    SELECT zip_code FROM zip_code
    WHERE zip_code {Param_ZipCode_op} {Param_ZipCode_value}

    In the example above, Param_ZipCode is used as a parameter.
    The value or values of the parameter and the operator is filled by the user in the user interface.
    If the user selects the operator, as IN and then the UI would prompt the user to select a list of zip codes.
    Those inputs by the user need to substituted in the query to make the effective query the following

    SELECT zip_code FROM zip_code
    WHERE zip_code IN ('15212','15213')

    We are able to substiture the values part of the parameter at runtime, but the operator cannot be substituted.

    The team need help from the denodo support team to get the help


    SELECT DISTINCT cl_n as data_value, cl_n as display_value FROM main_dv


SELECT CommonClaims.eamie_id, CommonClaims.line
          FROM MKT.CLPSH
        INNER JOIN CommonClaims.GROUP_ID = CLNT_CLH.GROUP_ID
        WHERE CLNT_CLH.CL_N = '281129' -- Client Number as paramter = and IN operator switch etc..)
        SELECT DISTINCT GRP_CLH.CL_N     GROUP_NUMBER
  FROM (SELECT *
          FROM MKT.CLPSH
         WHERE     BPD_ID in (18)
               AND CLPS_STUS_C = 'A'
               AND CLPS_MKT_STUS_C = 100
               ) GRP_CLPSH
       JOIN
       (SELECT *
          FROM MKT.CLH
         WHERE     CL_STUS_C = 'A'
               AND CL_MKT_STUS_C = 100
               )
       GRP_CLH
           ON GRP_CLH.CL_ID = GRP_CLPSH.CL_ID
       JOIN MKT.CLCLA CLCLA
           ON     GRP_CLH.CL_ID = CLCLA.CL_ID
              AND CLCLA.CLCLA_STUS_C = 'A'
              AND CLCLA.CLCLA_TYP_C = 104
       JOIN
       (SELECT *
          FROM MKT.CLH
         WHERE     CL_STUS_C = 'A'
               )
       CLNT_CLH
           ON CLNT_CLH.CL_ID = CLCLA.PARN_CL_ID
WHERE CLNT_CLH.CL_N = '281129'