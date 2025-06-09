-- %%VIEW_TRANSACTIONS%%
-- Join the credit card and customer table, query only the credit card data
SELECT
    cc.TRANSACTION_ID 'Transaction ID',
    cc.TRANSACTION_VALUE 'Value',
    cc.TRANSACTION_TYPE 'Type',
    cc.BRANCH_CODE 'Branch Code',
    cc.CUST_SSN 'SSN',
    cc.TIMEID 'Date',
    cc.CUST_CC_NO 'CCN'
FROM
    cdw_sapp_credit_card cc
LEFT JOIN
    cdw_sapp_customer cust
ON
    cc.cust_ssn = cust.ssn
WHERE
    cust.cust_zip = %s
    AND cc.timeid LIKE '%s%';