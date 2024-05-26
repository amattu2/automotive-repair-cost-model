--- This script was used to generate the data for the dataset
USE
    udb_1;
SELECT
    TRIM(i.EstDesc) AS "Description",
    i.Mileage AS "Mileage",
    TRIM(v.Make) AS "Make",
    TRIM(v.Model) AS "Model",
    v.ModYear AS "ModelYear",
    FLOOR(i.Total) AS "Total"
FROM
    Invoices i
LEFT JOIN Vehicles v ON
    v.CarId = i.CarId
WHERE
    i.Deleted = 0 AND i.TicketType = "Invoice" AND i.Private = 0
ORDER BY
    EstDate ASC;
