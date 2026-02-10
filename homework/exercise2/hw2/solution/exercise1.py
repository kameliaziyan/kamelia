def analyze_log_content(log_content: str) -> dict :

    count_error = 0
    count_warning = 0
    count_info = 0
    dict_count = {}

    for i in range(len(log_content)):
        if log_content[i] == "E" and log_content[i+1] == "R" and log_content[i+2] == "R" and log_content[i+3] == "O" and log_content[i+1] == "R" :
            count_error += 1

        if log_content[i] == "W" and log_content[i+1] == "A" and log_content[i+2] == "R" and log_content[i+3] == "N" and log_content[i+4] == "I" and log_content[i+5] == "N" and log_content[i+6] == "G" :

            count_warning += 1

        if log_content[i] == "I" and log_content[i+1] == "N" and log_content[i+2] == "F" and log_content[i+3] == "O"  :
            count_info += 1


    dict_count["Error"] = count_error
    dict_count["Warning"] = count_warning
    dict_count["Info"] = count_info




#count_error , count_warning , count_info 


    return  dict_count





log_content = """
2024-04-29 15:45:00,089 INFO [name:starwars_engine][pid:2995] Message one
2024-04-29 15:45:05,123 WARNING [name:starwars_engine][pid:2996] Check disk space
2024-04-29 15:45:08,111 /var/log/apache2/server.access.log 172.18.0.12 - - "POST /api/command/?201dfd68-e48d-587b-e715-3ff83ef3af19 HTTP/1.1" 200
2024-04-29 15:45:10,456 ERROR [name:starwars_engine][pid:2997] Failed to start engine
2024-04-29 15:46:00,789 INFO [name:starwars_engine][pid:2998] All systems go
"""

result = analyze_log_content(log_content)
print(result)

#{
#   'Error': 1, 
#    'Warning': 1, 
#    'Info': 2
#}