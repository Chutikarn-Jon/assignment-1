def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    actions = []
    x, y, z = s

    #Pour from the 8-liter bottle to the 5-litter bottle
    if x>0 and y<5 ;
        amount = min(x,5-y);
        actions.append(((x-amount,y+amount,z),amount))
    #Pour from the 5-liter bottle to the 3-litter bottle
    if y>0 and z<3;
         amount = min(y,3-z);
        actions.append(((x,y-amount,z+amount),amount))
    #Pour from the 3-liter bottle to the 8 -liter bottle
    if z>0 and x<8;
        amount = min(z,8-x);
        actions.append(((x+amount,y,z-amount),amount))
    #Pour from the 5-liter bottle to the 3-liter bottle
    if y>0 and z<3;
        amount = min(y,3-z);
        actions.append(((x,y-amount,z+amount),amount))
    #Pour from the 8-liter bottle to the 5-liter bottle
    if x>0 and y<5;
        amount = min(x,5-y);
        actions.append(((x-amount,y+amount,z),amount))
    #Pour from the 5-liter bottle to the 3-liter bottle
    if y>0 and z<3;
        amount = min(y,3-z);
        actions.append(((x,y-amount,z+amount),amount))
    #Pour from the 3-liter bottle to the 8-liter bottle
    if z>0 and x<8;
        amount = min(z,8-x);
        actions.append(((x+amount,y,z-amount),amount))
    return actions
