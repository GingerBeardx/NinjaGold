def init_vals():
    try:
        session['total_gold']
        session['activities']
    except KeyError:
        session['total_gold'] = 0
        session['activities'] = []

def update_strings(location, add_gold):
    if add_gold >= 0:
        netted = "Earned"
        effect = "green"
    else:
        netted = "Ouch! Played the odds and lost"
        effect = "red"
    time = datetime.datetime.now().strftime("%Y-%m-%d[-]%H:%M:%S")
    string = "{} {} gold from the {}! ({})".format(netted, abs(add_gold), location, time)
    session['activities'].append([effect, string])
        

def gold_update(location):
    if location == 'farm':
        add_gold = random.randrange(10, 21)
    elif location == 'cave':
        add_gold = random.randrange(5, 11)
    elif location == 'house':
        add_gold = random.randrange(2, 6)
    elif location == 'casino':
        add_gold = random.randrange(-50, 51)
    update_strings(location, add_gold)
    session['total_gold'] += add_gold