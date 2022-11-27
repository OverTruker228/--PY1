OUTPUT_FILE = "output.csv"

def to_csv_file(filename, headers, rows, delimiter = None, new_line = None):
    if new_line is None:
        new_line = '\n'
    if delimiter is None:
        delimiter = ','
    with open(filename, "w") as output_c:
        output_c.write(delimiter.join(headers))
        output_c.write(new_line)
        for rows_i in rows:
            output_c.write(delimiter.join(rows_i))
            output_c.write(new_line)
        output_c.close()
    return 0



headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']
data = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]


with open(OUTPUT_FILE) as f:
    for line in f:
        print(line, end="")
