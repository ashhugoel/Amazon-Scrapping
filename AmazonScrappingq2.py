from more_itertools import unique_everseen
with open('AmazonWebscarppeddata.csv' ,'r') as f, open('main.csv', 'w') as out_file:
    out_file.writelines(unique_everseen(f))


print("EOF") #end of file
