for line in input:
    datalist = line.strip().split(",")
    app, category,rating, review, size, installations, type, price, contentrating, genres, lastupdate, currentversion, androidversion = datalist
    output.write(category + "\t" + rating + "\n")

input.close()
output.close()