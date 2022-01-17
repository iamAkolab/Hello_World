market_2nd = {'ns':'green', 'ew':'red'}

#assert statements are from programmmers errors not user errors
#its enforces that a value must be true

def switchLights(intersection):
    """Traffic Simulation 
     
      Args:
        assert(string) : The string to assert

     Returns:
        string
  
     # Add a section detailing what errors might be raised
  
     Raises:
       ValueError: .
    """
    
    for key in intersection.keys():
        
        if intersection[key] == 'green':
            intersection[key] == 'yellow'
            
        elif intersection[key] == 'yellow':
            intersection[key] == 'red'
            
        elif intersection[key] == 'red':
            intersection[key] == 'green'

    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)


switchLights(market_2nd)



