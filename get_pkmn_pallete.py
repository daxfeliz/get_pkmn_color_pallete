def get_pkmn_pallete(pkmn_name):
    from urllib.request import Request, urlopen
    import urllib
    import io
    from colorthief import ColorThief
    
    #check for upper case spelling, must be lowercase for Pokemon Database
    if pkmn_name[0].isupper()==True:
        pkmn_name=pkmn_name.lower()
    
    sprite_url = 'https://img.pokemondb.net/artwork/large/'+str(pkmn_name)+'.jpg'

#     fd = urlopen(sprite_url)
    req = Request(sprite_url, headers={'User-Agent': 'Mozilla/5.0'})
    fd = urlopen(req).read()
    #
    f = io.BytesIO(fd)
    color_thief = ColorThief(f)
    #
    # print(color_thief.get_color(quality=1))
    # print(color_thief.get_palette(quality=1))
    #
    #divide by 255 to get RGB ranging from 0-1
    return np.array(color_thief.get_palette(quality=1))/255
