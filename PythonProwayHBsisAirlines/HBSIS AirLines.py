from classe_fortwo import fortwo
fortwo = fortwo(['piloto','oficial','oficial','chefe','comissaria','comissaria','policial','presidiario'],[])

fortwo.ida('chefe','piloto')
fortwo.volta('piloto')

fortwo.ida('piloto','oficial')
fortwo.volta('piloto')

fortwo.ida('piloto','oficial')
fortwo.volta('chefe')

fortwo.ida('chefe','comissaria')
fortwo.volta('chefe')

fortwo.ida('chefe','comissaria')
fortwo.volta('chefe')

fortwo.ida('policial','presidiario')
fortwo.volta('piloto')

fortwo.ida('piloto','chefe')
