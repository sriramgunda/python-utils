import json

styles = "<link rel='stylesheet' href='styles.css'>"
stylescss = """
<style>
table, td, th {
  border: 1px solid black;
}

table {
  width: 100%;
  border-collapse: collapse;
}
</style>
"""
html_header = "<!DOCTYPE html><html>"
head = "<head><meta name='viewport' content='width=device-width, initial-scale=1.0'>"+ stylescss +"</head>"
body_start = "<body>"
body_ended = "</body>"
html_end = "</html>"
table_caption = ""
table_start = "<table class='tablecss' style='border:1'><caption>" + table_caption + "</caption>"
table_end = "</table>"

htmlpage_start = html_header + head + body_start
body_content = ""
htmlpage_end = body_ended + html_end



def to_htmltable(data):
    with open('index.html', 'w+') as ht:
        ht.write(htmlpage_start)
        body_content = "<div>" + table_start
        trdata = []
        if len(data) > 0:
            header_count = 0
            columns = []
            for row in data:
                if header_count == 0:
                    for key in row.keys():
                        columns.append(key)
                    #print(columns)
                    thdata = ""
                    for col in columns:
                       thdata += "<th>" + col + "</th>"
                    trdata.append("<tr>" + thdata + "</tr>")
                    header_count = 1
                else:
                    thdata = ""
                    for col in columns:
                        thdata += "<td>" + row[col] + "</td>"
                    trdata.append("<tr>" + thdata + "</tr>")
        #print(trdata)
        trdata = ''.join(trdata)
        body_content += trdata + "</tr>"
        body_content += "</div>"        
        ht.write(body_content + table_end + htmlpage_end)
    return body_content

if __name__ == '__main__':
    data = [{'firstname': 'John', 'lastname':'Walker'},
	    {'firstname': 'Clark', 'lastname':'Alex'},
	    {'firstname': 'Scott', 'lastname':'Ben'},
            {'lastname':'Sean', 'firstname':'Goldman'}]
    print(to_htmltable(data))
