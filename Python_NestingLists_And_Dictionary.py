#Nesting
capitals = {
    "France":"Paris",
    "Germany":"Berlin"
}

#Nesting List Inside Dictionary example

travel_log ={
"France": {"Cities Visited":["Paris","Lille","Dijon"],
            "Total_No_Visits":12},
'Germany':["Berlin","Hambury","Stuttgart"],

}

#Nesting Dictionary with List

travel_log_list =[
{
    "Country":"France",
    "Cities_Visited": ["Paris","Lille","Dijon"],
    "total_vists":12
},
{
    "Country":"India",
    "Cities_Visited": ["Delhi","Gurgaon","Mumbai"],
    "total_vists":5
},

]

print(travel_log_list)

#write a function will allow new record to be added to next dictionary
def add_new_country(country_visited,times_visited,cities_visited):
    new_country= {}
    new_country["Country"]=country_visited;
    new_country["total_vists"]=times_visited;
    new_country["Cities_Visited"]=cities_visited;
    travel_log_list.append(new_country)


add_new_country("Russia",2,["Moscow","Saint Petersburg"]);
print(travel_log_list)